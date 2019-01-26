class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []
        
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        items = {'name' : name, 'price' : price}
        self.items.append(items)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        sum = 0    
        for item in self.items: 
            sum += item['price']
        return sum

# class method example for a person
class Person:
    def __init__(self, firstName, lastName, address, gender, height, weight):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.gender = gender
        self.height = height
        self.weight = weight

    def personInfo(self):
        return {"first name": self.firstName, "last name": self.lastName, "address": self.address}

    def personBMI(self):
        print({"weight":self.weight, "height^2": self.height**2})
        return float(self.weight / (self.height**2))

# make person and print information
personsAddress = {"street": "123 SW 17th Ave", "state": "FL", "city": "Jacksonville", "zip": "123456798" }
bill = Person("Bill", "Williams", personsAddress, "male", 2,85 )
print(bill.personBMI())
print(bill.personInfo())