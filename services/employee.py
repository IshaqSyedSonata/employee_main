from models.index import Employee

def get_employees(db, limit, page, search):
    skip = (page - 1) * limit
    employees = db.query(Employee
                # ).filter(Employee.title.contains(search)
                ).limit(limit
                ).offset(skip
                ).all()
    return employees

def get_employee(db, emp_id):
    employee = db.query(Employee).filter(Employee.id == emp_id).first()
    # employee = db.query(Employee
    #             # ).filter(Employee.title.contains(search)
                # ).all()
    return employee

def add_employee(db, employee_data):
    new_employee_data = Employee(**employee_data.dict())
    db.add(new_employee_data)
    db.commit()      
    db.refresh(new_employee_data)
    emp_id = new_employee_data.id # getting the last newly inserted primary key
    return emp_id

    