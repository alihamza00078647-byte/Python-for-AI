from random import randint
class Train:
    def __init__(self, ticketno, fro, to):
        self.ticketno = ticketno
        self.fro = fro 
        self.to = to
    def book(self):
        print(f"The Number of the Ticket is {self.ticketno}")
    def status(self):
        print(f"The Ticket Fare in train No: {self.ticketno} from {self.fro} to {self.to} is {randint(200, 233)}")

train_info = Train(randint(1, 12), "Delhi", "Lahore")
train_info.book()
train_info.status()


