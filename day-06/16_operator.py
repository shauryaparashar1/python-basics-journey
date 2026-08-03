# ----------------------------------------
# Python Class Example
# ----------------------------------------
# This program demonstrates:
# 1. Creating a class
# 2. Using a constructor (__init__)
# 3. Creating objects
# 4. Returning a new object from a method
# ----------------------------------------


class Point:
    """Represents a point in a 2D coordinate system."""

    # Initialize the point with x and y coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Add the coordinates of two Point objects
    # and return a new Point object
    def sum(self, p):
        return Point(self.x + p.x, self.y + p.y)

    # Display the coordinates of the point
    def print_point(self):
        print(f"X is {self.x} and Y is {self.y}")


# ----------------------------------------
# Create two Point objects
# ----------------------------------------
p1 = Point(3, 2)
p2 = Point(6, 3)

# Add the two points
p3 = p1.sum(p2)

# Print the resulting point
p3.print_point()