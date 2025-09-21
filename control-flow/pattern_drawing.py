# This script draws a square pattern of asterisks based on user input.

# 1. Prompt User for Pattern Size
# We use a try-except block to handle cases where the user might enter non-numeric input.
try:
    pattern_size = int(input("Enter the size of the pattern: "))

    # 2. Draw the Pattern
    # This is the outer loop that handles the rows.
    # We initialize a counter variable 'row' to 0.
    row = 0
    while row < pattern_size:
        
        # This is the inner loop that handles the columns (the asterisks in each row).
        # We use a for loop to iterate from 0 up to (but not including) pattern_size.
        for column in range(pattern_size):
            # The print() function with end="" keeps the asterisks on the same line.
            print("*", end="")
        
        # After the inner loop finishes, we print a newline character to move to the next row.
        print()
        
        # This is the crucial part to prevent an infinite loop.
        # We increment the row counter.
        row += 1

except ValueError:
    print("Invalid input. Please enter a positive integer.")
