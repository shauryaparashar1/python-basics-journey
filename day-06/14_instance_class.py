class Car:
    company = "BMW" # This is a class attribute.

    def __init__(self, model, year): # This is the constructor method that initializes instance attributes.
        self.model = model # This is an instance attribute.
        self.year = year   # This is another instance attribute.

    def get_info(self): # This is a method that returns the car's information.
        return self.model, self.year, self.company

    def display_info(self): # This is a method that displays the car's information.
        print(f"car model: {self.model} year: {self.year} company: {self.company}")

Car1 = Car("Audi", 2020) # Create an instance of the Car class
print(Car1.model) # Access the instance attribute
print(Car1.year)  # Access the instance attribute

print(Car.company) # Access the class attribute



