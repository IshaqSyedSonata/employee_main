from fastapi import APIRouter
emp = APIRouter()

@emp.get('/home')
def employee_home():
    return {"MEssage" : "Welcome Employee Router"}