# employee_main
A web application using FastApi, SQLAlchemy, MySQL

Developed by: Syed Mohmad Ishaq
ishaq.syed@sonata-software.com

This application is an enhanced form of the following tutorial, and hence requires all packages/softwares needed for this tutorial: https://fastapi.tiangolo.com/tutorial/sql-databases/

However, this tutorial is using MySQL database, and its connection parameters can be checked in database.py file.

Basic Requirements:
Python 3.10.10 (installed with updated pip)

fastapi --> pip install fastapi 
uvicorn --> pip install uvicorn[standard]
sqlalchemy --> pip install sqlalchemy
pymysql --> pip install pymysql

After all the pre-requisites are installed, use this command (with administrator rights) to run the application:

uvicorn sql_app.main:app --reload

Then, in browser, write: http://127.0.0.1:8000/home

To see swagger docs, write: http://127.0.0.1:8000/docs