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