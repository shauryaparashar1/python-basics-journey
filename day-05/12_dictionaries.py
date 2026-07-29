# Dictionaries in Python
prices = {"Apple": 100, "Banana": 50, "Orange": 75}

# Accessing values using keys
print(prices["Apple"])  # Output: 100 
print(prices.get("Banana"))  # Output: 50
print(prices.get("Grapes", "Not Found"))  # Output: Not Found

# Changing values
prices["Apple"] = 200
print(prices["Apple"])  # Output: 200