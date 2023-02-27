from fastapi import APIRouter, Depends, HTTPException, status, Request
from config.session import get_db
from sqlalchemy.orm import Session
products_router = APIRouter()
from models.index import Products, Employee

# from schemas.index import ListProductResponse

@products_router.get("/{emp_id}")
async def get_employee_products(emp_id: int, db : Session = Depends(get_db)) :
    # print(f' {request.method} ------------------------------------------' )
    # print(  {dict(request.headers.items())}'  )
    # print(f' {request.body} ------------------------------------------' )
    try:
        employee_products = db.query(Products, Employee
            ).join(
                Employee, 
                Products.owner_id == Employee.id
            ).filter(
                Products.owner_id == emp_id
            ).all()
        print(type(employee_products))
        print(employee_products)
         
        # print( employee_products[1].Products.name )
        # return JSONResponse(status_code=404, content={"message": len(employee_products)})
        return {'status': 'success', 'results' : 2, 'products' :  employee_products[0].Products}
        # return {'status': 'success', 'results' : 2}
        # return {'status': 'success'}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail='Server Down')
            
