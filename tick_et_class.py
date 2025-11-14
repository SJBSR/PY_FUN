import random 
class TicketGenerator:
    def __init__(self):
        self.last_ticket_number = 0

    def generate_ticket_id(self):
        self.last_ticket_number += 1
        return f"{self.last_ticket_number:04d}"

    def create_ticket(self, name, issue, priority):
        ticket_id = self.generate_ticket_id()
        ticket_info = {
            "Ticket ID": ticket_id,
            "Name": name,
            "Issue": issue,
            "Priority": priority
        }
        return ticket_info