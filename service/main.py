from typing import List, Optional
from fastapi import Depends, FastAPI,  WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from . import crud, models, schemas, auth
from .database import SessionLocal, engine, get_db
from datetime import timedelta, datetime
from .settings import ACCESS_TOKEN_EXPIRE_MINUTES

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


"""================== Api Zone ================== """


@app.post("/get_token", response_model=schemas.Token)
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if not db_user:
        crud.create_user(db=db, user=user)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/start_new_game")
def new_game(user=Depends(auth.get_current_user), db: Session = Depends(get_db)):
    crud.start_game(db, user)
    return {"message": "ready"}


""" ================== Web socket Zone ================== """


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


async def update_best_score(websocket, user, db):
    try:
        player_best_score = crud.get_player_best_score(db, user)
        global_best_score = crud.get_global_best_score(db)
        await manager.broadcast(f"Global:{global_best_score}")
        await manager.send_personal_message(f"Score:{player_best_score}", websocket)
    except:
        pass


@app.websocket("/playgame")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)):
    await manager.connect(websocket)
    try:
        # เช็ค Token และ ผู้เล่น
        token = await websocket.receive_text()
        user = await auth.get_current_user(token, db)
        # อัพเดทคะแนนสูงสุดของผู้เล่นและ Global
        await update_best_score(websocket, user, db)
        # เริ่มเกม
        while True:
            # รับข้อมูลจาก client
            data = await websocket.receive_text()
            # แยกส่วนข้อมูลเพื่อทำการเช็ค
            split_data = data.split(":")
            if split_data[0] == "click":
                # ข้อมุลตำแหน่งที่คลิก
                pos = int(split_data[1])
                value, clicks, solved = crud.card_click(db, user, pos)
                gameResponse = schemas.GameReponse(
                    pos=pos, value=value, clicks=clicks)
                await manager.send_personal_message(gameResponse.dict(), websocket)
                # เช็คว่าเปิดครบทุกใบแล้วถูกต้อง
                if solved:
                    # อัพเดทคะแนนสูงสุดของผู้เล่นและ Global
                    await update_best_score(websocket, user, db)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception as err:
        print(err)
        # ดัก Error ที่ตั้งขึ้นด้วยตัวเอง
        if hasattr(err, 'detail'):
            await manager.send_personal_message(f"Error: {err.detail}", websocket)
        # ดัก Error ที่เกิดขึ้นเองในโปรแกรม
        else:
            await manager.send_personal_message(f"Error: {err.args[0]}", websocket)
        manager.disconnect(websocket)
