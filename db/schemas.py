from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class CustomerSchema(BaseModel):
    customer_id: int
    name: str
    national_id: str
    birthdate: Optional[date]
    created_at: datetime

    class Config:
        orm_mode = True


class AccountSchema(BaseModel):
    account_id: int
    customer_id: int
    account_number: str
    balance: int
    status: str
    opened_at: datetime
    closed_at: Optional[datetime]

    class Config:
        orm_mode = True


class TransactionSchema(BaseModel):
    transaction_id: int
    account_id: int
    type: str
    amount_cents: int
    timestamp: datetime
    description: Optional[str]
    batch_id: Optional[int]

    class Config:
        orm_mode = True


class BatchSchema(BaseModel):
    batch_id: int
    type: str
    status: str
    started_at: Optional[datetime]
    finished_at: Optional[datetime]
    message: Optional[str]

    class Config:
        orm_mode = True
