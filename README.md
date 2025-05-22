# Task 1: Basic Mathematical Operations

# Input from the end users
n1 = float(input("Enter First Number: "))
n2 = float(input("Enter Second Number: "))

# Performing operations
addition = n1 + n2
subtraction = n1 - n2
multiplication = n1 * n2

# Handling division by zero
if n2 != 0:
    division = n1 / n2
else:
    division = "Undefined (division by zero is not allowed)"

# Displaying the results
print("Addition =", addition)
print("Subtraction =", subtraction)
print("Multiplication =", multiplication)
print("Division =", division)
input("Press enter to exit:")

# Assignment 2: Create a Personalized Greeting

# Taking input from the user
first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")

# Concatenating full name
full_name = first_name + " " + last_name

# Printing personalized greeting
print("Hello, " + full_name + "! Welcome to Python program.")
input("Press enter for exit")
