from fastapi import APIRouter, Depends,  HTTPException, status, Response
from config.session import get_db
from sqlalchemy.orm import Session
emp = APIRouter()
from services.index import employee
from schemas.index import EmployeeData, ListEmployeeResponse
from models.index import Employee

@emp.get('/', response_model = ListEmployeeResponse)
async def get_employees(db : Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    try:
        employees = employee.get_employees(db, limit, page, search)
        return {'status': 'success', 'results': len(employees), 'employees': employees}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail='Server Down')

@emp.patch('/{id}')
def update_employee(id: str, payload: EmployeeData, db: Session = Depends(get_db)):
    emp_query = db.query(Employee).filter(Employee.id == id)
    db_emp = emp_query.first()
    if not db_emp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No employee with this id: {id} found')
    update_data = payload.dict(exclude_unset=True)
    emp_query.filter(Employee.id == id).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(db_emp)
    return {"status": "success", "employee": db_emp}

@emp.delete('/{emp_id}')
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = employee.get_employee(db, emp_id)
    if not emp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No employee with this id: {emp_id} found')
    emp = employee.delete_employee(db, emp_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@emp.post('/')
def create_employee(employee_data: EmployeeData, db: Session = Depends(get_db)):
    emp_id = employee.add_employee(db, employee_data)
    result = employee.get_employee(db, emp_id)
    return {'user': result, 'emp_id': emp_id}

@emp.get('/{emp_id}')
async def get_employee(emp_id: int, db : Session = Depends(get_db)):
    emp = employee.get_employee(db, emp_id)
    return {'status': 'success', 'emp': emp}
    

