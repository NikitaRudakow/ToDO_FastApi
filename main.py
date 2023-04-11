from enum import Enum
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Trading APP"
)

fake_trades = [
    {"id": 1, "user_id": 1,  "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12}
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=10)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post("/trades")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}


fake_users_for_validate = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "tradep", "name": "Matt", "transactions": [
        {"id": 1, "date": "2020-03-16", "price": 12.0, "type": "sell"}
        ]
    }
]


class TypeTransactions(Enum):
    sell = "sell"
    buy = "buy"


class Transactions(BaseModel):
    id: int = Field(ge=0)
    date: str
    price: float = Field(ge=0.0)
    type: TypeTransactions


class User(BaseModel):
    id: int = Field(ge=0)
    role: str = Field(max_length=10)
    name: str = Field(max_length=15)
    transactions: Optional[List[Transactions]] = []


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users_for_validate if user_id == user.get("id")]
