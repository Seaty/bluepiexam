from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "user_master"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
 
    games =  relationship("Game", back_populates="owner")

class Game(Base):
    __tablename__ = "game_master"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user_master.id"), index=True)
    clicks = Column(Integer, index=True, default=0)
    active = Column(Boolean, default=True)
    solved = Column(Boolean, default=False)

    cards = relationship("Card")
    owner = relationship("User", back_populates="games")

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Integer, index=True)
    shown = Column(Boolean, default=False)
    correct = Column(Boolean, default=False)
    game_id = Column(Integer, ForeignKey("game_master.id"))