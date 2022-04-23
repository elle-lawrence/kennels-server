class Employee():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, address, location_id, position, hrly_pay_rate):
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id
        self.position = position 
        self.hrly_pay_rate = hrly_pay_rate
        
new_employee = Employee(4, "Mrs Beaver", "1010 10st St", 1, "Dog Walker", "$14")