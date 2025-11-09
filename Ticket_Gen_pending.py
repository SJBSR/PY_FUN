# Ticket generator
import random
import numbers
import datetime
import numpy as np

a = datetime.datetime.now()
#print(a + datetime.timedelta(days=5))

print("Welcome to the Ticket Generator!")
name = input("Please enter your name: ")
issue = str(input("What seems to be the problem?\n"))
priority = int(input("On a scale from 1 to 10, how urgent is this issue?\n"))

ticket_id = 1000 + random.randint(1, 8999)
print("You're ticket info:" f"\nDate: {a.strftime('%Y-%m-%d %H:%M:%S')}\nTicket ID: {ticket_id}\nName: {name}\nIssue: {issue}\nPriority: {priority}")