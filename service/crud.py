from sqlalchemy.orm import Session

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
        db_card = models.Card(desk_id=new_game.id,value=i)
        db.add(db_card)
        db.commit()
    db.refresh(new_game)
    return new_game

def get_player_best_score(db:Session,user:str):
    score = db.query(models.Game).filter_by(solved=True, user_id=user.id).order_by(models.Game.clicks)
    return score[0].clicks if len(score) > 0 else 0

def get_global_best_score(db:Session):
    score = db.query(models.Game).filter_by(solved=True).order_by(models.Game.clicks)
    return score[0].clicks if len(score) > 0 else 0