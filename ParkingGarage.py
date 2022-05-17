class Garage():
    """A simple parking garage with only 5 spaces and 15 minute parking downtown."""
    def __init__(self):
        self.tickets = 5
        self.parkingSpaces = ["a1", "b2", "c3", "d4", "e5"]
        self.unavailableParkingSpace = []
        self.currentTicket = {"Paid": False}

    def DisplayAavailableSpaces(self):
        """Display svailable parking spaces"""
        print("The following parking spaces in our garage availabe are: ")
        for spaces in self.parkingSpaces:
            print(spaces)

    def takeTicket(self):
        """When driver takes a ticket the space will be moved to unavailable list."""
        self.DisplayAavailableSpaces()
        if self.tickets > 0:
            response = input("Please enter the space your would like to reserve: [a1], [b2], [c3], [d4], [e5] ").lower()
            if response == "a1" or "b2" or "c3" or "d4" or "e5":
                self.parkingSpaces.remove(response)
                self.unavailableParkingSpace.append(response)
                print(f"You have reserved {response}, Please take your ticket.")
            self.tickets -= 1
        elif self.tickets <= 0:
            print(f"We have {self.tickets} available in our garage, please try again later. We apologize for th inconvience")
            

    def payForParking(self):
        "Paying for 5 dollars for parking ticket"
        if self.tickets > 0:
            userpay = input("Please enter your 5 dollar payment now(Cash Only): [5] ")
            if userpay == "5":
                print("Your ticket has been paid you have 15 minutes to leave.")
                self.currentTicket["Paid"] = True
            else:
                print("Invalid input, Please try again")
        if self.tickets <= 0:
            print("Goodbye")

    def leaveGarage(self,):
        """When driver returns a ticket the space will be moved to parking spaces list as available."""
        if self.currentTicket["Paid"] == False:
            self.payForParking()
        elif self.currentTicket["Paid"] == True:
            response = input("Please enter the space your would like to return: [a1], [b2], [c3], [d4], [e5] ")
            if response.lower() == "a1" or "b2" or "c3" or "d4" or "e5":
                self.unavailableParkingSpace.remove(response)
                self.parkingSpaces.append(response)
            print("Your ticket has been paid you have 15 minutes to leave.")
            print("Thank you, have a nice day!")
            self.tickets += 1

OutlawGarage = Garage()

while True:
    start = input ("Would you like to park in our garage? Enter [y] for yes, [n] for no, [s] for show available spaces, [q] for quit at anytime: ")
    if start.lower() == "y":
        OutlawGarage.takeTicket()
        OutlawGarage.payForParking()
        OutlawGarage.leaveGarage()
    elif start.lower() == "s":
        OutlawGarage.DisplayAavailableSpaces()
    elif start.lower() == "n":
        print("Have a nice day, Goodbye!")
    elif start.lower() == "q":
        print("Have a nice day, Goodbye!")
        break
    else:
        print("Invalid Input, please try again.")
