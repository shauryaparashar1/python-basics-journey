# =========================================
# Topic: Functions and Modules
# Description: Practice file for functions, return values, lambda, recursion,
#              modules, scope, docstrings, and small problem-solving examples.
# Author: Shaurya Parashar
# =========================================


# -----------------------------------------
# Defining Functions in Python
# -----------------------------------------

def greet():
    """Print a greeting message."""
    print("Hello, welcome to Python functions!")


greet()


# -----------------------------------------
# Function Arguments & Return Values
# -----------------------------------------

def greet_user(name):
    """Return a greeting message for a user."""
    return f"Hello, {name}!"


message = greet_user("Max")
print(message)


def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


result = add_numbers(10, 20)
print("Sum:", result)


def calculate_area_of_circle(radius):
    """Return the area of a circle."""
    pi = 3.14159
    return pi * radius * radius


area = calculate_area_of_circle(5)
print("Area of circle:", area)


def introduce(name, age=18):
    """Return a short introduction message."""
    return f"My name is {name} and I am {age} years old."


print(introduce("Alex"))
print(introduce("Max", 20))


# -----------------------------------------
# Lambda Functions in Python
# -----------------------------------------

square = lambda x: x * x
print("Square of 6:", square(6))

add = lambda x, y: x + y
print("Lambda add:", add(4, 7))

is_even = lambda num: "Even" if num % 2 == 0 else "Odd"
print("10 is:", is_even(10))


# -----------------------------------------
# Recursion in Python
# -----------------------------------------

def factorial(n):
    """Return factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print("Factorial of 5:", factorial(5))


def fibonacci(n):
    """Return nth Fibonacci number using recursion."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci of 6:", fibonacci(6))


# -----------------------------------------
# Modules and Pip - Using External Libraries
# -----------------------------------------

import math
import random

print("Square root of 81:", math.sqrt(81))
print("Ceiling of 4.2:", math.ceil(4.2))
print("Random number between 1 and 10:", random.randint(1, 10))

# Note:
# External libraries are installed using pip, for example:
# pip install requests
# Then you can import and use them in your Python program.


# -----------------------------------------
# Variable Scope and Docstrings
# -----------------------------------------

global_message = "I am a global variable"


def show_scope():
    """Demonstrate local and global variable scope."""
    local_message = "I am a local variable"
    print(global_message)
    print(local_message)


show_scope()


def multiply(a, b):
    """
    Multiply two numbers and return the result.

    Parameters:
    a (int or float): First number
    b (int or float): Second number

    Returns:
    int or float: Product of a and b
    """
    return a * b


print("Multiply:", multiply(3, 4))


# -----------------------------------------
# Functions & Modules - Practice Set
# -----------------------------------------

def is_prime(num):
    """Check whether a number is prime or not."""
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print("7 is prime:", is_prime(7))
print("10 is prime:", is_prime(10))


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


print("25°C in Fahrenheit:", celsius_to_fahrenheit(25))


def count_vowels(text):
    """Count vowels in a given string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


print("Vowels in 'Python is fun':", count_vowels("Python is fun"))


def max_of_three(a, b, c):
    """Return the largest among three numbers."""
    return max(a, b, c)


print("Largest number:", max_of_three(12, 45, 23))


def reverse_text(text):
    """Return the reverse of a string."""
    return text[::-1]


print("Reverse of 'python':", reverse_text("python"))


# -----------------------------------------
# Notes:
# - Practiced defining and calling functions
# - Used arguments, return values, and default parameters
# - Learned lambda functions and recursion
# - Practiced modules, scope, and docstrings
# - Solved small problems using functions
# -----------------------------------------