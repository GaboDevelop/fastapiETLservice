from typing import Optional
from pydantic import BaseModel


class SaleOrderBase(BaseModel):
    number_order: Optional[str]
    amount: Optional[float]


class SaleOrderCreate(SaleOrderBase):
    number_order: str
    amount: float


class SaleOrderUpdate(SaleOrderBase):
    _id: int
    pass


class SaleOrderResponse(SaleOrderBase):
    class Config:
        orm_mode = True
