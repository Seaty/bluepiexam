from typing import List, Optional

from pydantic import BaseModel

""" Base Schemas for database """

class UserBase(BaseModel):
    username: str

    class Meta:
        orm_mode = True


class Card(BaseModel):
    value: int
    shown: bool
    correct: bool

    class Meta:
        orm_mode = True

class Game(BaseModel):
    cards: List[Card]
    clicks: int
    active: bool

    class Meta:
        orm_mode = True

""" Base Schemas for JWT Token"""

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
        
