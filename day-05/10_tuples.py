# Tuple in Python
coordinates = (99, 20)
print(coordinates[0])  # Prints the first element of the tuple

# unpacking a tuple
coordinates = (99, 20, 33, 44)
x, y, z, w = coordinates  # Unpacks the tuple into variables x, y, z, and w
print(x, w)  # Prints the values of the variables

# Tuple methods
# Tuples are immutable, so they do not have methods like append or insert
coordinates = (99, 20, 33, 44)

print(coordinates.count(20))  # Counts the occurrences of 20 in the tuple
print(coordinates.index(33))  # Returns the index of the first occurrence of 33

