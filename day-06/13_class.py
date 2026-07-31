class Car: # Define a class named Car
    company = "BMW"

    def __init__(self, model, year): # Initialize the instance attributes
        self.model = model
        self.year = year     

C1 = Car("X5", 2020) # Create an instance of the Car class
print(C1.company)
print(C1.model)
print(C1.year)

C2 = Car("X3", 2021) # Create another instance of the Car class
print(C2.company)
print(C2.model)
print(C2.year)
