##
## Name: Caleb Rogers
## Prog3Rogers.py
##
## Purpose:
## Calculate the purchase charge of downloaded music
##
## Inputs:
## Last name, first name, cost per song, and number of songs
##
## Output:
## Full name, number of songs purchased, price per song,
## service charge,taxes owed, and total charge
##
## Certification of Authenticity:
## I certify that this lab is entirely my own work.
##

def main():
    print("This program will calculate the purchase charge of downloaded music")

    # Inputs for last name, first name, cost per song, and number of songs
    lastName = input("What is your last name? ")
    firstName = input("What is your first name? ")

    songCost = float(input("What is the cost per song? "))
    while songCost < 0:
        songCost = float(input("Invalid input, please enter a valid cost per song: "))

    numSongs = int(input("How many songs are being downloaded? "))
    while numSongs < 0:
        numSongs = int(input("Invalid input, please enter a valid number of songs: "))

    # Calculate base charge
    baseCharge = numSongs * songCost

    # Calculate service charge
    if numSongs <= 3:
        serviceRate = .13
    elif numSongs >= 4 and numSongs < 6:
        serviceRate = .10
    else:
        serviceRate = .07

    service = serviceRate * baseCharge

    # Calculate net payment
    netPayment = baseCharge + service

    # Calculate tax amount
    if netPayment <= 5.00:
        taxRate = 0.00
    elif netPayment > 5 and netPayment <= 7.50:
        taxRate = .045
    elif netPayment > 7.50 and netPayment <= 9.99:
        taxRate = .0725
    else:
        taxRate = .09

    tax = taxRate * netPayment

    # Calculate total charge
    total = netPayment + tax

    # Output
    print()
    print()
    print("Your name is:", firstName, lastName)
    print("The number of songs you are purchasing are:", numSongs, "song(s)")
    print("The price per song is: ${0:02.2f}".format(songCost))
    print("The service charge is: ${0:02.2f}".format(service))
    print("The taxes owed are: ${0:02.2f}".format(tax))
    print()
    print("Your total charge is: ${0:02.2f}".format(total))
    print()
    print("Thank you for participating in my experimental program!")

main()
    
