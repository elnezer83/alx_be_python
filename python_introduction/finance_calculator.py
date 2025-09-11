#!/usr/bin/env python3

# This script calculates monthly and projected annual savings based on user input.

# --- 1. Get User Input for Financial Details ---
# The input() function gets a line of text from the user.
# The int() function immediately converts that text into a number (integer),
# which is necessary for mathematical calculations.

# Prompt for monthly income and store it as an integer
monthly_income = int(input("Enter your monthly income: "))

# Prompt for monthly expenses and store it as an integer
monthly_expenses = int(input("Enter your total monthly expenses: "))

# --- 2. Calculate Monthly Savings ---
# Subtract expenses from income to find the monthly savings.
monthly_savings = monthly_income - monthly_expenses

# --- 3. Project Annual Savings ---
# The task assumes a 5% simple annual interest rate (0.05).
# We calculate the total savings over 12 months.
annual_savings_without_interest = monthly_savings * 12

# We calculate the interest earned over one year on the total savings.
interest_earned = annual_savings_without_interest * 0.05

# We add the interest to the annual savings to get the final projected amount.
projected_savings = annual_savings_without_interest + interest_earned

# --- 4. Output Results ---
# We use f-strings to print the results in the required format.
# The {monthly_savings} and {projected_savings} will be replaced with their calculated values.
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
