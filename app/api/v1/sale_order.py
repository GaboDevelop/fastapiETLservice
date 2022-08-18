from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from app import schemas, crud

router = APIRouter()


@router.get("", response_model=List[schemas.SaleOrderResponse])
def read_orders(skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve all products.
    """
    orders = crud.sale_order.get_all(skip=skip, limit=limit)
    return orders


@router.post("", response_model=schemas.SaleOrderCreate)
def create_product(*, product_in: schemas.SaleOrderBase) -> Any:
    """
    Create new products.
    """
    data = dict(product_in)
    product = crud.sale_order.create(data=data)
    return product

# @router.put("", response_model=schemas.ProductResponse)
# def update_product(*, db: Session = Depends(get_db), product_in: schemas.ProductUpdate) -> Any:
#     """
#     Update existing products.
#     """
#     product = crud.product.get(db, model_id=product_in.id)
#     if not product:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="The product with this ID does not exist in the system.",
#         )
#     product = crud.product.update(db, db_obj=product, obj_in=product_in)
#     return product
#
#
# @router.delete("", response_model=schemas.Message)
# def delete_product(*, db: Session = Depends(get_db), id: int) -> Any:
#     """
#     Delete existing product.
#     """
#     product = crud.product.get(db, model_id=id)
#     if not product:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="The product with this ID does not exist in the system.",
#         )
#     crud.product.remove(db, model_id=product.id)
#     return {"message": f"Product with ID = {id} deleted."}
