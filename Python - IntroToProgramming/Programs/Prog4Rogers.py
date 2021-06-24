##
## Name: Caleb Rogers
## Prog4Rogers.py
##
## Purpose:
## This program uses Python's random number generator
## to create a gambling simulator
##
## Inputs:
## Amount of money player wants to bet
##
## Output:
## Each play, roll of each die, amount in pot,
## total number of rolls, max amount that was in pot and the play it was on
##
## Certification of Authenticity:
## I certify that this lab is entirely my own work.
##

def main():
    from random import randrange
    play = 0
    maxRoll = 0
    maxMoney = 0
    
    # Greet user
    print("Welcome to the Lucky Seven Eleven game!")
    print("Bet a dollar for every roll!")
    print("If you roll a 7, you win $3! If you roll an 11, you win $2!")
    print()

    # Input pot
    pot = int(input("From $1 to $100, how much are you willing to bet? "))

    while pot <= 0 or pot > 100:
        print("The given bet is an invalid amount")
        pot = int(input("Please enter a number between $1 to $100: "))

    print("your current pot is ${0:02.2f}".format(pot))
    print("Here we go!")

    while pot > 0:

        # Calculate play
        play = play + 1
        
        # Calculate roll of dice and pot
        die1 = randrange (1,7)
        die2 = randrange (1,7)

        roll = die1 + die2

        if roll == 7:
            pot = pot + 3
        elif roll == 11:
            pot = pot + 2
        else:
            pot = pot - 1

        # Calculate max money and roll of max
        if pot > maxMoney:
            maxMoney = pot
            maxRoll = play

        # Output play, roll of each die, and pot
        print("Play:", play, end="      ")
        print("Die 1:", die1, end="      ")
        print("Die 2:", die2, end="      ")
        print("Pot:", pot)

    # Ouput total rolls, max money and the roll of max
    print("You're broke!")
    print("You ran out of money with a total of", play, "roll(s)")
    print("You should have quit after", maxRoll, "rolls when you had ${0:02.2f}".format(maxMoney))

main()
