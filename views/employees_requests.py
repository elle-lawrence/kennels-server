import sqlite3
import json
from models import Employee

EMPLOYEES = [
    {
      "id": 1,
      "name": "Elle Lawrence",
      "address": "8422 Johnson Pike E"
    },
    {
      "id": 2,
      "name": "Jayce Lynman",
      "address": "209 Emory Drive"
    },
    {
      "id": 3,
      "name": "Grace McDaniels",
      "address": "100 Copper Drive"
    }
]

# def get_all_employees():
#     return EMPLOYEES

# def get_single_employee(id):
#     request_employee = None
    
#     for employee in EMPLOYEES:
#         if employee["id"] == id:
#             request_employee = employee
        
#     return request_employee

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    
    return employee
  
def delete_employee(id):
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)        

def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break
        
def get_all_employees():
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
          e.id,
          e.name,
          e.address,
          e.location_id
        FROM employee e
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            employees.append(employee.__dict__)

    return json.dumps(employees)

def get_single_employee(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
          e.id,
          e.name,
          e.address,
          e.location_id
        FROM employee e
        WHERE e.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        employee = Employee(data['id'], data['name'], data['address'], data['location_id'])

        return json.dumps(employee.__dict__)

def get_employees_by_location(location_id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        select
            e.id,
            e.name,
            e.address,
            e.location_id
        from Employee e
        WHERE e.location_id = ?
        """, ( location_id, ))
        
        employees = []
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'] )
            employees.append(employee.__dict__)
            
    return json.dumps(employees)