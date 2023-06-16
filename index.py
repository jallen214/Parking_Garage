class Parking_Garage():
    def __init__(self, tickets, parkingSpaces, CurrentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.CurrentTicket = CurrentTicket

    def take_ticket(self):
        self.tickets.pop()
        self.parkingSpaces.pop()

    def pay_for_parking(self):
        i = input('Your total is $10.00, please insert cash or card')
        if i =="":
            print('ticket has not been paid')
        else:
            print('ticket has been paid and they have 15 minutes to leave')

    def leave_garage(self):
        
   


        




    
