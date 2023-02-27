
from fastapi import FastAPI
from config.db import my_sql_engine
from models.index import Base
print("------------------")
from routers.index import emp
from routers.index import products_router
print("--------*********************---")
Base.metadata.create_all(bind=my_sql_engine)

        
app = FastAPI()
app.include_router(emp, tags=['Employee'], prefix='/v1/employee')
app.include_router(products_router, tags=['Prodcuts'], prefix='/v1/products')
@app.get('/')
def app_main():
    return {"Message" : "Hello"}