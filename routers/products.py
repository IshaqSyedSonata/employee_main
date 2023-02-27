from fastapi import APIRouter, Depends, HTTPException, status, Request
from config.session import get_db
from sqlalchemy.orm import Session
products_router = APIRouter()
from models.index import Products, Employee

@products_router.get("/{emp_id}")
async def get_employee_products(emp_id: int, db : Session = Depends(get_db)) :
    try:
        employee_products = db.query(Products, Employee
            ).join(
                Employee, 
                Products.owner_id == Employee.id
            ).filter(
                Products.owner_id == emp_id
            ).all()
        return {'status': 'success', 'results' : 2, 'products' :  employee_products[0].Products}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail='Server Down')
            
