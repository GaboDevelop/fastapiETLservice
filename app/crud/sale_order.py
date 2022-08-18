from mongoengine import connect

from app.database.mongo import Mongo
from app.database.session import Session
from app.models.sale_order import SaleOrder
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from app.schemas import SaleOrderCreate, SaleOrderUpdate

ModelType = TypeVar("ModelType", bound=SaleOrder)
CreateSchemaType = TypeVar("CreateSchemaType", bound=SaleOrderCreate)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SaleOrderUpdate)


class CRUDSaleOrder(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    model = None
    mongo = Mongo()

    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A Mongo Collection model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model
        self.mongo.initialize()

    def create(self, data: CreateSchemaType) -> dict:
        new_user = self.model(**data)
        new_user.save()
        return {
            '_id': new_user.pk,
            'amount': new_user.amount,
            'number_order': new_user.number_order
        }

    def get_all(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        try:
            res = self.model.objects
            return list(res)
        except:
            print("Error en consulta get_all")
            return []

    # def get(self, id: Any) -> Optional[ModelType]:
    #     return True
    #
    # def update(self, id: Any, data: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
    #     return True
    #
    # def remove(self,  id: Any) -> ModelType:
    #     return True


sale_order = CRUDSaleOrder(SaleOrder)
