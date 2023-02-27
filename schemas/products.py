from typing import List

# import typing as t

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
    # products: t.List[t.Tuple[ProductData, EmployeeData]]

    class Config:
        orm_mode = True
