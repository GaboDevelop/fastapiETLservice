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
    mongo = None

    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A Mongo Collection model class
        * `schema`: A Pydantic model (schema) class
        """
        print("AQUI 2")
        self.model = model
        print(model)
        self.mongo = Mongo()
        print(self.mongo)

    def create(self, data: CreateSchemaType) -> ModelType:
        new_user = self.model(data)
        new_user.save()
        return new_user.to_json()

    def get_all(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        print("AQUI 3")
        print(self.model)
        connect(host="DB_URI")
        return self.model.objects.to_json()

    # def get(self, id: Any) -> Optional[ModelType]:
    #     return True
    #
    # def update(self, id: Any, data: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
    #     return True
    #
    # def remove(self,  id: Any) -> ModelType:
    #     return True


sale_order = CRUDSaleOrder(SaleOrder)
