# employee_main
A web application using FastApi, SQLAlchemy, MySQL

This project is using MySQL database, and its connection parameters can be checked in config/db.py file.

Basic Requirements:
Python 3.10.10 (installed with updated pip)

fastapi --> pip install fastapi 
uvicorn --> pip install uvicorn[standard]
sqlalchemy --> pip install sqlalchemy
pymysql --> pip install pymysql

After all the pre-requisites are installed, use this command (with administrator rights) to run the application:

uvicorn main:app --reload

Then, in browser, write: http://127.0.0.1:8000

To see swagger docs, write: http://127.0.0.1:8000/docs


Unit Test Requirements:

httpx --> pip install httpx
pytest --> pip install pytest

