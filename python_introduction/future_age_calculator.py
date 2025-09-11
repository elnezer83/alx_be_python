#!/usr/bin/env python3

# This script asks for the user's age and calculates their age in 2050.

# 1. Get user input
# The input() function asks the user a question and gets their answer.
# The answer is always read as a string (text).
user_age_string = input("How old are you? ")

# 2. Convert the input to a number (integer)
# We use the int() function to convert the string (text) into an integer (number).
# This is necessary to perform mathematical calculations.
user_age_int = int(user_age_string)

# 3. Calculate the age in 2050
# We assume the current year is 2023, so we add 27 years to the age.
age_in_2050 = user_age_int + 27

# 4. Print the final result
# We use an f-string to insert the calculated age into the final sentence.
print(f"In 2050, you will be {age_in_2050} years old.")