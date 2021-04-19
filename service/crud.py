from sqlalchemy.orm import Session
from random import shuffle
from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserBase):
    db_user = models.User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def start_game(db: Session, user: schemas.UserBase):
    last_game = db.query(models.Game).filter_by(
        user_id=user.id, active=True).first()

    if last_game is not None:
        last_game.active = False
        db.commit()

    new_game = models.Game(user_id=user.id)
    db.add(new_game)
    db.commit()
    db.refresh(new_game)
    cards = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    shuffle(cards)

    for i in cards:
        db_card = models.Card(game_id=new_game.id,value=i)
        db.add(db_card)
        db.commit()

    db.refresh(new_game)
    return new_game

def get_player_best_score(db:Session,user:str):
    return db.query(models.Game).filter_by(solved=True, user_id=user.id).order_by(models.Game.clicks)[0].clicks

def get_global_best_score(db:Session):
    return db.query(models.Game).filter_by(solved=True).order_by(models.Game.clicks)[0].clicks


def card_click(db, user, pos):
    # ดึงค่า game ที่เล่น
    game = db.query(models.Game).filter_by(user_id=user.id, active=True).first()
    # ถ้ายังไม่มีการสร้างเกม ให้สร้างเกมใหม่
    if game is None:
        game = crud.new_game(db, user)
    # ดึงการ์ดทั้งหมดของเกมนี้
    cards = db.query(models.Card).filter_by(game_id=game.id).order_by(models.Card.id)
    # ดึงค่าการ์ดที่เลือก
    clicked_card = cards[pos]
    value = clicked_card.value
    # ดักกรณีที่ส่งค่าการ์ดที่เปิดอยู่แล้ว
    if clicked_card.shown:
        return value, game.clicks, False
    # เพิ่มจำนวนคลิก
    game.clicks += 1
    # เช็คว่ามีการที่เปิดให้เทียบก่อนหน้านี้ไหม
    open_card_check = list(filter(lambda card: card.shown and not card.correct, game.cards))
    # กรณีที่การ์ดที่เปิดเป็นใบเริ่ม ให้เปิด
    if len(open_card_check) == 0:
        clicked_card.shown = True
        db.commit()
        return value, game.clicks, False
    # กรณีที่การ์ดที่เปิดเป็นใบเทียบ
    else:
        # ดึงค่าการที่เปิด (ซึ่งควรมีใบเดียว ><)
        opened_card = open_card_check[0]
        # อัพเดทกรณีที่ค่าของการ์ดทั้งคู่จำนวนเท่ากัน
        if opened_card.value == value:
            opened_card.correct = True
            clicked_card.correct = True
            clicked_card.shown = True
            db.commit()
            db.refresh(game)
            # กรณีที่การ์ดเปิดทุกใบแล้ว
            if len(list(filter(lambda card: card.correct, game.cards))) == 12:
                game.solved = True
                game.active = False
                db.commit()
                return value, game.clicks, True
            # กรณีที่การ์ดเปิดยังไม่ครบ
            return value, game.clicks, False
        # กรณีที่การ์ดสองใบค่าไม่เท่ากัน
        else:
            # ปิดการ์ดที่เปิดก่อนหน้านี้
            opened_card.shown = False
            db.commit()
            return value, game.clicks, False
    