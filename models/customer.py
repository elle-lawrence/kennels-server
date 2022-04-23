class Customer():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, address, location_id, animal_id):
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id
        self.animal_id = animal_id
        
new_customer = Customer(4, "Cindy Loo", "1010 1st Ave", 1, 4)