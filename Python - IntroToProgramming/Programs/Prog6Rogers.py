##
## Name: Caleb Rogers
## Prog6Rogers.py
##
## Purpose:
## This program will track pay-per-view movies purchased by users.
## 
## Inputs:
## Customer ID, customer name, number of movies ordered, length of each movie,
## and rating of each movie.
##
## Output:
## Customer name, customer ID, number of movies purchased, total cost of the movies,
## service charge, total amount due, number of customers processed,
## highest amount charged to a customer, customer ID of the highest amount,
## lowest amount charged to a customer, customer ID of the lowest amount,
## total amount of downloads purchased, and average purchase amount.
## 
## Certification of Authenticity:
## I certify that this lab is entirely my own work.
##

def chooseMovies(movies):

    totalCost = 0

    for i in range(movies):

        # Input Ordered Movies
        movieLength = int(input("Enter the length of the movie (in minutes): "))
        while movieLength < 1 or movieLength > 240:
            movieLength = int(input("Invalid input, enter a number between 1 and 240, inclusively: "))
        rating = input("Enter the letter of the movie rating: ")
        while (rating == "G") and (rating == "P") and (rating == "R") and (rating == "X") and (rating == "O"):
            rating = input("Invalid Input, Enter a valid letter: ")

        # Calculate Cents Per Minute
        if rating == "G":
            centsPerMin = .039
        elif rating == "P":
            centsPerMin = .054
        elif rating == "R":
            centsPerMin = .068
        elif rating == "X":
            centsPerMin = .273
        elif rating == "O":
            centsPerMin = .040

        # Calculate Cost Per Movie
        costOfMovie = movieLength * centsPerMin

        # Calculate And Return Cost Of All Movies Per User
        totalCost = totalCost + costOfMovie
    return totalCost
            
def calcServiceCharge(moviesAmount, costOfMovies):

    # Calculate And Return Service Charge 
    if moviesAmount <= 3:
        serviceRate = .18
    elif moviesAmount <= 7:
        serviceRate = .15
    elif moviesAmount <= 11:
        serviceRate = .11
    else:
        serviceRate = .05

    serviceCharge = costOfMovies * serviceRate

    return serviceCharge

def calcTotalDue(costForMovies, service):

    # Calculate and Return Total Amount Due 
    total = costForMovies + service
    tax = total * .07
    total = total + tax
    return total
    

def outputResults(name, ID, numberOfMovies, cost, chargeOfService, amountDue):

    # Output Per User
    print()
    print("Customer Name:", name)
    print("Customer ID:", ID)
    print("Number of Movies Purchased:", numberOfMovies)
    print("Total Cost of Movies: ${0:02.2f}".format(cost))
    print("Service Charge: ${0:02.2f}".format(chargeOfService))
    print("Total Amount Due: ${0:02.2f}".format(amountDue))
    print()

def summaryOutput(customers, maxOfTotal, maxOfID, minOfTotal, minOfID, totalOverall, totalAverage):

    # Summary Output
    print()
    print("SUMMARY")
    print("Number of Customers Processed:", customers)
    print("Highest Amount Charged to a Customer: ${0:02.2f}".format(maxOfTotal))
    print("Customer's ID of the Highest Amount:", maxOfID)
    print("Lowest Amount Charged to a Customer: ${0:02.2f}".format(minOfTotal))
    print("Customer's ID of the Lowest Amount:", minOfID)
    print("Total Amount of Downloads Purchased: ${0:02.2f}".format(totalOverall))
    print("Average Purchase Amount: ${0:02.2f}".format(totalAverage))
    
def main():

    # Initialization
    numCustomers = 0
    maxTotal = 0
    maxID = 0
    minTotal = 9999999
    minID = 0
    overallTotal = 0
    avgTotal = 0
    customerID = -999999

    while customerID != 0:

        # Input Customer's Order
        customerID = int(input("Enter your ID (between 25,000 and 99,999): "))
        if customerID != 0:
            while customerID < 25000 or customerID > 99999:
                customerID = int(input("Invalid input, enter a number between 25,000 and 99,999, inclusively: "))
            customerName = input("Enter your name: ")
            numMovies = int(input("Enter the number of movies you are ordering: "))
            while numMovies <= 0:
                numMovies = int(input("Invalid input, enter a positive number: "))

            # Calculate Total Cost of All Movies
            moviesCost = chooseMovies(numMovies)

            # Calculate Service Charge
            serviceCharge = calcServiceCharge(numMovies, moviesCost)

            # Calculate Total Due
            totalDue = calcTotalDue(moviesCost, serviceCharge)

            # Output Results
            outputResults(customerName, customerID, numMovies, moviesCost, serviceCharge, totalDue)

            # Calculate Summary Output
            numCustomers = numCustomers + 1
            if totalDue > maxTotal:
                maxTotal = totalDue
                maxID = customerID
            if totalDue < minTotal:
                minTotal = totalDue
                minID = customerID
            overallTotal = overallTotal + totalDue
            
        else:

            # Summary Output 
            if numCustomers != 0:
                avgTotal = overallTotal / numCustomers
                summaryOutput(numCustomers, maxTotal, maxID, minTotal, minID, overallTotal, avgTotal)
            
            # Summary Output When 0 Customers
            else:
                minTotal = 0
                summaryOutput(numCustomers, maxTotal, maxID, minTotal, minID, overallTotal, avgTotal)
                   
main()
