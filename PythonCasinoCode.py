import random
import csv
from datetime import datetime
FILENAME = "casinos.csv"

class Person:
    def __init__ (self, name, money, chips):
        self.name = name
        self.money = money
        self.chips = chips

    def conMon(self):
        while True:
            try:
                gMoney = int(input("How much money does " + self.name + " want to convert to chips?: $"))
                print()
                break
            except ValueError:
                print()
                print("You entered an invalid entry. Please try again.")
                print()
        X = datetime.now()
        X = str(X)
        outfile = open("casinos.csv", "w")
        outfile.write(X)
        outfile.close()
        self.money -= gMoney
        self.chips += gMoney/2
        print("Your Chips:",self.chips)

    def conChip(self):
        gMoney = self.chips*2
        self.money += gMoney
        print("Your Total Money:",self.money)
        print()

    def slots(self):
        x = "y"
        while x == "y":
            if self.chips < 10:
                print("You do not have enough chips to play.")
                break
            else:
                c1 = random.randint(1,3)
                c2 = random.randint(1,3)
                c3 = random.randint(1,3)
                print(str(c1) + " " + str(c2) + " " + str(c3))
                if c1 == c2 & c2 == c3:
                    print()
                    print("You win the...")
                    if c1 == 1:
                        print("Small Prize!")
                        print()
                        self.chips += 15 ####
                        #X=self.chips
                        #X=str(X)
                        #outfile = open("casino.csv", "w")
                        #outfile.write(X)
                        #outfile.close()
                        print("15 chips!")
                        print("Chips Left:",self.chips)
                        print("=" * 11)
                    if c2 == 2:
                        print("Medium Prize!")
                        print()
                        self.chips += 25 #####
                        #X=self.chips
                        #X=str(X)
                        #outfile = open("casino.csv", "w")
                        #outfile.write(X)
                        #outfile.close()         
                        print("25 chips!")
                        print(self.chips)
                        print("=" * 11)
                        print()
                    if c3 == 3:
                        print("Large Prize!")
                        print()
                        self.chips += 40 ######
                        #X=self.chips
                        #X=str(X)
                        #outfile = open("casino.csv", "w")
                        #outfile.write(X)
                        #outfile.close()
                        print("40 chips!")
                        print("Chips Left:",self.chips)
                        print("=" * 11)
                        print()
                else:
                    print()
                    print("No Luck!")
                    print()
                    self.chips -= 10 #####
                    #X=self.chips
                    #X=str(X)
                    #outfile = open("casino.csv", "w")
                    #outfile.write(X)
                    #outfile.close()
                    print("Chips Left:",self.chips)
                    print("=" * 11)
                x = input("Play again? (y/n): ")
                x = x.lower()
                print()
                if x == "n":
                    print("Thanks for playing! Bye!")
       
