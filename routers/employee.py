from fastapi import APIRouter, Depends,  HTTPException, status
from config.session import get_db
from sqlalchemy.orm import Session
emp = APIRouter()
from services.index import employee
from schemas.index import EmployeeData, ListEmployeeResponse

from models.index import Employee

@emp.get('/')
async def get_employees(db : Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = '') -> ListEmployeeResponse:
    try:
        employees = employee.get_employees(db, limit, page, search)
        print(type(employees))
        print(employees)
        return {'status': 'success', 'results': len(employees), 'employees': employees}
    except Exception as e:
        # error = e.__class__.__name__
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail='Server Down')
        
@emp.get('/{id}')
async def get_employee(db : Session = Depends(get_db), emp_id: int = 10):
    emp = employee.get_employee(db, emp_id)
    return {'status': 'success', 'emp': emp}

@emp.post('/')
def create_employee(employee_data: EmployeeData, db: Session = Depends(get_db)):
    emp_id = employee.add_employee(db, employee_data)
    result = employee.get_employee(db, emp_id)
    return {'user': result, 'emp_id': emp_id}