# =========================================
# Topic: Input and Type Casting
# Description: Typecasting and User Input in Python
# Author: Shaurya Parashar
# =========================================

# ---- Type Casting ----
# Convert string to integer
string = "10"
integer = int(string)
print("String to Integer:", integer)

# convert integer to string
num_int = 20
num_str = str(num_int)   
print("integer to string:", num_str)

# Convert float to integer
x_flo = 2.4
x_int = int(x_flo)
print("float to integer:", x_int)


# ---- Taking User Input in Python ----
order = input("Enter your order:")
quantity = int(input("Quantity you want:"))
print(f"You ordered - {order}, Number of items - {quantity}, Thanks for purchasing.")

# ---- Notes ----
# Practiced Typecasting and User Input in Python