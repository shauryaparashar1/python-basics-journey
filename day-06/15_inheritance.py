# ----------------------------------------
# Python Inheritance Example
# ----------------------------------------
# Inheritance allows one class (child class)
# to inherit attributes and methods from another
# class (parent class).
# ----------------------------------------


# Parent (Base) Class
class Animal:
    # Constructor to initialize the object's attributes
    def __init__(self, name):
        self.name = name

    # Method that can be inherited or overridden
    def speak(self):
        print("Animal sound")


# Child (Derived) Class
class Cat(Animal):
    # Override the speak() method of the Animal class
    def speak(self):
        print("Meoow!")


# ----------------------------------------
# Create an object of the Cat class
# ----------------------------------------
cat = Cat("Kitty")

# Call the overridden method
cat.speak()