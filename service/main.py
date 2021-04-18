from typing import List,Optional
from fastapi import Depends, FastAPI,  WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from . import crud, models, schemas, auth
from .database import SessionLocal, engine, get_db
from datetime import timedelta,datetime
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


"""================== Web socket Zone ================== """

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
        player_best_score = crud.get_player_best_score(db,user)
        global_best_score =  crud.get_global_best_score(db)
        await manager.broadcast(f"Global:{best_score}")
        await manager.send_personal_message(f"Score:{player_best_score}", websocket)
    except:
        pass


@app.websocket("/playgame")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)):
    await manager.connect(websocket)
    try:
        token = await websocket.receive_text()
        user = await auth.get_current_user(token, db)
        await update_best_score(websocket,user,db)
        while True:

            data = await websocket.receive_text()
            if data[:5] == "click":
                pos = int(data[6:])

    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception as err:
        print(err)
        if hasattr(err, 'detail'):
            await manager.send_personal_message(f"Error: {err.detail}", websocket)
        else:
            await manager.send_personal_message(f"Error: {err.args[0]}", websocket)
        manager.disconnect(websocket)