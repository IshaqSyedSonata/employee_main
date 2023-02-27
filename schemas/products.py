from typing import List

from pydantic import BaseModel
from .employee import EmployeeData

class ProductData(BaseModel):
    id: int | None = None
    name : str
    description : str
    owner_id : int
    is_active : bool

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class ListProductResponse(BaseModel):
    status: str
    results: int
    products : List[ProductData] 

    class Config:
        orm_mode = True
