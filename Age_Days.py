# This is an Age Calculator in days

# Ask the user for their age in years
age_years = input("What is your age in years?\n")

# Set variable to convert years to days
days_in_year = 365

# Calculate the user's age in days
age_days = int(age_years) * days_in_year

# Print out the user's age in days
print(f"You're {age_days} days old!")