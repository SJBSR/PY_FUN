# Ticket generator
import random
import numbers
import datetime
import numpy as np

a = datetime.datetime.now()
#print(a + datetime.timedelta(days=5))

# Welcome message and user inputs
print("Welcome to the Ticket Generator!")
name = input("Please enter your name: ")
issue = str(input("What seems to be the problem?\n"))
priority = int(input("On a scale from 1 to 10, how urgent is this issue?\n"))

# Generate ticket ID and print ticket info ( still needs formatting )
# Format has to create a ticket number from the last ticket number created starting from 0001 to 99999
ticket_id = int(0000 + 1) <= 1 + 1





#ticket_id = 1000 + random.randint(1, 8999)
print("You're ticket info is below." f"\nDate: {a.strftime('%Y-%m-%d %H:%M:%S')}\nTicket ID: {ticket_id}\nName: {name}\nIssue: {issue}\nPriority: {priority}")