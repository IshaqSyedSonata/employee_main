
from fastapi import FastAPI
from config.db import my_sql_engine, local_session
from models.index import Base
from routers.index import emp
Base.metadata.create_all(bind=my_sql_engine)
def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()
app = FastAPI()
app.include_router(emp)

@app.get('/')
def app_main():
    return {"Message" : "Hello"}