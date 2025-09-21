# This script creates a simple calculator using a match-case statement.

# 1. Prompt for User Input
# Ask the user to enter the first and second numbers.
# We convert the input strings to integers using int() to perform mathematical operations.
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # Ask for the operation choice.
    operation = input("Choose the operation (+, -, *, /): ")

    # 2. Perform the Calculation Using Match Case
    # The match case statement checks the value of the 'operation' variable.
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}.")
        case '-':
            result = num1 - num2
            print(f"The result is {result}.")
        case '*':
            result = num1 * num2
            print(f"The result is {result}.")
        case '/':
            # Check for division by zero before performing the operation.
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                # Use floating-point division to get a more precise result.
                result = num1 / num2
                print(f"The result is {result}.")
        case _:
            # This case handles any input that is not one of the four valid operations.
            print("Invalid operation. Please choose from +, -, *, /.")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
