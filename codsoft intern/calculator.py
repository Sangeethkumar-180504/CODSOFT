# Simple Calculator in Python

# Function to perform calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # Check for division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Invalid operation!"

# === Main Program ===
try:
    # Take input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nChoose operation:")
    print(" +  for Addition")
    print(" -  for Subtraction")
    print(" *  for Multiplication")
    print(" /  for Division")

    operation = input("Enter your choice (+, -, *, /): ")

    # Perform calculation
    result = calculate(num1, num2, operation)

    # Display result
    print(f"\nResult: {result}")

except ValueError:
    print("Please enter valid numbers.")
