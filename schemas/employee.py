from typing import List
from pydantic import BaseModel

class EmployeeData(BaseModel):
    id: int | None = None
    name : str
    email : str
    address : str
    is_active : bool

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class ListEmployeeResponse(BaseModel):
    status: str
    results: int
    employees: List[EmployeeData]
    
    class Config:
        orm_mode = True
