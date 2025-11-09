# Tax Calculator
import decimal

# Welcome message
print ("Hello! Welcome to the Tax Calculator!")

# Define tax rate
tax = 0.0625

# Request user input for amount
amount = float(input("Please enter the amount: "))

# Calculate total with tax only displaying two decimal places
total = amount + (amount * tax)
print("The total amount with tax is: {:.2f}".format(total))