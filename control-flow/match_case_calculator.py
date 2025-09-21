# This script is a simple calculator that uses a match-case statement
# to perform basic arithmetic operations based on user input.

# 1. Prompt for user input
# Get the first number and convert it to an integer
num1 = int(input("Enter the first number:"))
# Get the second number and convert it to an integer
num2 = int(input("Enter the second number:"))
# Get the operation choice as a string
operation = input("Choose the operation (+, -, *, /): ")

# 2. Perform the calculation using a match-case statement
match operation:
    # Case for addition
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    # Case for subtraction
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    # Case for multiplication
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    # Case for division, with a check for division by zero
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    # Default case for any other input
    case _:
        print("Invalid operation. Please choose from +, -, *, /.")
