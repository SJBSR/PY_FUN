# This is an Age Calculator in days

# Ask the user for their age in years (\n creates a new line for the user's input)
age_years = input("What is your age in years?\n")

# Set variable to convert years to days
days_in_year = 365

# Calculate the user's age in days
age_days = int(age_years) * days_in_year

# Print out the user's age in days (using an f-string)
print(f"You're {age_days} days old!")