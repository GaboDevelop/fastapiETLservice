from fastapi import APIRouter

from app.api.v1 import sale_order

api_router = APIRouter()
api_router.include_router(sale_order.router, prefix="/orders", tags=["orders"])
