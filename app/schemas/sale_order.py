from typing import Optional
from pydantic import BaseModel


class SaleOrderBase(BaseModel):
    _id: Optional[str]
    number_order: Optional[str]
    amount: Optional[float]


class SaleOrderCreate(SaleOrderBase):
    _id: str
    number_order: str
    amount: float


class SaleOrderUpdate(SaleOrderBase):
    _id: str
    pass


class SaleOrderResponse(SaleOrderBase):
    class Config:
        orm_mode = True
