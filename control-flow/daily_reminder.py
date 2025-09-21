# This script creates a personalized daily reminder based on user input.

# 1. Prompt for User Input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Initialize an empty reminder message variable
reminder_message = ""

# 2. Process the Task Based on Priority
# A match-case statement is used to set the base reminder message
match priority.lower():
    case "high":
        reminder_message = f"'{task}' is a high priority task"
        # Check if the high priority task is time-bound
        if time_bound.lower() == "yes":
            # Append the time-sensitive phrase to the existing message
            reminder_message += " that requires immediate attention today!"
        print(f"Reminder: {reminder_message}")
    case "medium":
        reminder_message = f"'{task}' is a medium priority task."
        # Check if the medium priority task is time-bound
        if time_bound.lower() == "yes":
            # Append the time-sensitive phrase to the existing message
            reminder_message += " that requires immediate attention today!"
        print(f"Reminder: {reminder_message}")
    case "low":
        reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        print(reminder_message)
    case _:
        # For any other input, provide a generic reminder
        print(f"Reminder: '{task}' has an unknown priority level.")
