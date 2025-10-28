# Simple Python program for basic arithmetic operations

# Take input from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Perform operations
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b if b != 0 else "Undefined (cannot divide by zero)"

# Display results
print("\nResults:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")