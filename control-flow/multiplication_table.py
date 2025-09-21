# This script generates a multiplication table for a number provided by the user.

# 1. Prompt User for a Number
# We use a try-except block to handle cases where the user might enter non-numeric input.
try:
    number = int(input("Enter a number to see its multiplication table: "))

    # 2. Generate and Print the Multiplication Table
    # A for loop is used to iterate through the numbers from 1 to 10 (inclusive).
    # The range(1, 11) function generates a sequence from 1 up to (but not including) 11.
    for i in range(1, 11):
        # Calculate the product of the user's number and the current number in the loop.
        product = number * i
        
        # Print the result in the specified format: "X * Y = Z".
        print(f"{number} * {i} = {product}")

except ValueError:
    # This block is executed if the user's input cannot be converted to an integer.
    print("Invalid input. Please enter a valid number.")
