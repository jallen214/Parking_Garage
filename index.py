class ParkingGarage:
    def __init__(self, tickets, parking_spaces, current_ticket):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = current_ticket

    def take_ticket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            self.parking_spaces.pop(0)
            self.current_ticket[ticket] = {"paid": False}
            print(f"Ticket {ticket} issued. Please proceed to a parking space.")
        else:
            print("Apologies, the parking garage is full. Please try again later.")


    def pay_for_parking(self):
        ticket = input("Enter your ticket number: ")
        if ticket in self.current_ticket:
            if not self.current_ticket[ticket]["paid"]:
                amount = input("Enter the amount for parking: ")
                if amount:
                    self.current_ticket[ticket]["paid"] = True
                    print("Payment successful. You have 15 minutes to leave.")
                else:
                    print("Payment unsuccessful. Please try again.")
            else:
                print("Your ticket has already been paid.")
        else:
            print("Invalid ticket number, Please try again.")
    
    def leave_garage(self):
        ticket = input("Enter your ticket number: ")
        if ticket in self.current_ticket:
            if self.current_ticket[ticket]["paid"]:
                print("Thank you. Have a nice day!")
                self.parking_spaces.append(ticket)
                self.tickets.append(ticket)
                self.current_ticket.pop(ticket)
            else:
                print("Payment pending. Please make the payment.")
        else:
            print("Invalid ticket number. Please try agian.")

tickets = ['A1', 'A2', 'A3', 'A4', 'A5']
parking_spaces = ['P1', 'P2', 'P3', 'P4', 'P5']
current_ticket = {}

garage = ParkingGarage(tickets, parking_spaces, current_ticket)

garage.take_ticket()
garage.pay_for_parking()
garage.leave_garage()



        



