# =========================================
# Topic: Strings in Python
# Description: Practice of string basics, methods, and problem-solving
# Author: Shaurya Parashar
# =========================================


# -------------------------------
# 1. String Declaration
# -------------------------------

# Single quoted string
name1 = 'Alex'

# Double quoted string
name2 = "Alex"

# Triple quoted string (multi-line)
name3 = '''My name is Alex.
I am 20 years old.'''

print(name1)
print(name2)
print(name3)


# -------------------------------
# 2. String Indexing
# -------------------------------

fruit = "apple"

print("First character:", fruit[0])
print("Fourth character:", fruit[3])
print("Last character:", fruit[-1])


# -------------------------------
# 3. String Slicing
# -------------------------------

text = "I am Alex"

print("Full string:", text[:])
print("Slice (1:4):", text[1:4])
print("Reverse string:", text[::-1])


# -------------------------------
# 4. String Methods (Basic)
# -------------------------------

name = "alex"

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())

text_with_space = "   Hello World   "

print("Left strip:", text_with_space.lstrip())
print("Right strip:", text_with_space.rstrip())
print("Full strip:", text_with_space.strip())


# -------------------------------
# 5. String Methods (Useful)
# -------------------------------

sentence = "python is fun"

print("Replace word:", sentence.replace("fun", "great"))
print("Split words:", sentence.split())
print("Find index of 'is':", sentence.find("is"))


# -------------------------------
# 6. Reverse a String
# -------------------------------

text = "python"
print("Reversed:", text[::-1])


# -------------------------------
# 7. Palindrome Check
# -------------------------------

word = "civic"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# -------------------------------
# 8. Count Vowels
# -------------------------------

text = "hello world"
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Vowel count:", count)


# -------------------------------
# 9. Clean User Input
# -------------------------------

raw_name = "   shaurya   "
clean_name = raw_name.strip().title()

print("Cleaned Name:", clean_name)


# -------------------------------
# 10. String Formatting
# -------------------------------

name = "Alex"
age = 27

print(f"My name is {name} and I am {age} years old")


# -------------------------------
# Notes:
# - Learned string basics, indexing, slicing
# - Practiced string methods and formatting
# - Applied concepts using small problems
# -------------------------------