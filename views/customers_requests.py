import sqlite3
import json
from models import Customer


CUSTOMERS = [
    {
      "id": 1,
      "name": "Olly Oxen-frez",
      "address": "8422 Johnson Pike E",
      "location_id": "2",
      "animal_id": "3"
    },
    {
      "id": 2,
      "name": "Bonnie Clyde",
      "address": "209 Emory Drive",
      "location_id": "2",
      "animal_id": "2"
    },
    {
      "id": 3,
      "name": "Justin Gilly",
      "address": "100 Copper Drive",
      "location_id": "2",
      "animal_id": "1"
    }
    # {
    #   "name": "Momo Fuko",
    #   "address": "10 Dearly Ln"
    # }
]

# def get_all_customers():
#   return CUSTOMERS

def get_single_customer(id):
    requested_customer = None
  
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
 
    return requested_customer

def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    
    return customer
  
def delete_customer(id):
    customer_index = -1

    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)
        
def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break
      
def get_all_customers():
    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
          c.id,
          c.name,
          c.address,
          c.location_id,
          c.animal_id
        FROM customer c
        """)

        customers = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['location_id'], row['animal_id'])
            customers.append(customer.__dict__)

    return json.dumps(customers)
