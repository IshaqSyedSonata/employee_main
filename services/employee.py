from models.index import Employee

def get_employees(db, limit, page, search):
    skip = (page - 1) * limit
    employees = db.query(Employee
                ).filter(Employee.name.contains(search)
                ).limit(limit
                ).offset(skip
                ).all()
    return employees

def get_employee(db, emp_id):
    employee = db.query(Employee).filter(Employee.id == emp_id).first()
    return employee

def add_employee(db, employee_data):
    new_employee_data = Employee(**employee_data.dict())
    db.add(new_employee_data)
    db.commit()      
    db.refresh(new_employee_data)
    emp_id = new_employee_data.id 
    return emp_id

def delete_employee(db, emp_id):
    emp_query = db.query(Employee).filter(Employee.id == emp_id)
    emp_id = emp_query.delete()
    db.commit()
    return {"emp_id": emp_id}

    