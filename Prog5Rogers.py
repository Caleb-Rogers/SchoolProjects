##
## Name: Caleb Rogers
## Prog5Rogers.py
##
## Purpose:
## This program will compute taxes using file input.
##
## Inputs:
## Input file.
##
## Output:
## Taxpayer ID, filing status, taxable income, tax rate, tax amount owed,
## number of taxpayers processed, highest tax amount, tax payer's ID with
## highest tax amount, total taxes paid, and average of taxes paid.
##
## Certification of Authenticity:
## I certify that this lab is entirely my own work.
##

def main():

    # Greet user
    print("This program will compute your taxes")

    # Get input file and open file
    fileName = input("Enter the file name, including the suffix: ")
    theFile = open(fileName, "r")
    print()

    # Get number of taxpayers from file
    numTaxPayers = int(theFile.readline())

    # Intialization
    standardDeduction = 4250
    overallTotalTax = 0
    count = 0
    maxTax = 0
    overallTotalTax = 0
    
    for i in range(numTaxPayers):

        # Get data from input file
        taxPayerID = int(theFile.readline())
        status = theFile.readline().strip().upper()
        grossIncome = float(theFile.readline())
        numExemptions = int(theFile.readline())

        # Calculate tax income
        exemptions = numExemptions * 1600
        taxIncome = grossIncome - standardDeduction - exemptions

        # Calculate tax rate       
        if status == "S":
            if taxIncome < 15000:
                taxRate = .14
            elif taxIncome <= 50000:
                taxRate = .22
            else:
                taxRate = .31
        elif status == "M":
            if taxIncome < 25000:
                taxRate = .12
            elif taxIncome <= 135000:
                taxRate = .20
            else:
                taxRate = .29
        elif status == "H":
            if taxIncome < 30000:
                taxRate = .13
            elif taxIncome <= 70000:
                taxRate = .21
            else:
                taxRate = .30

        # Calculate total tax
        totalTax = taxIncome * taxRate

        # Calculate max tax amount
        if totalTax > maxTax:
            maxTax = totalTax
            maxTaxPayer = taxPayerID

        # Calculate overall total tax
        overallTotalTax = overallTotalTax + totalTax

        # Validate negative tax income
        if taxIncome < 0:
            taxRate = 0
            totalTax = 0
        
        # Output each taxpayer's data
        print("Taxpayer ID:", taxPayerID)

        if status == "S":
            print("Filing Status: Single")
        elif status == "M":
            print("Filing Status: Married, filing jointly")
        elif status == "H":
            print("Filing Status: Head of Household")

        print("Taxable Income: ${0:02.2f}".format(taxIncome))
        print("Tax Rate: {:.0%}".format(taxRate))
        print("Tax Amount Owed: ${0:02.2f}".format(totalTax))
        print()

    # Calculate average of taxes
    avgTax = overallTotalTax / numTaxPayers
    
    # Output Summary
    print()
    print("Number of taxpayers processed:", numTaxPayers)
    print("Highest tax amount of ${0:02.2f}".format(maxTax)) 
    print("Tax payer's ID with the highest tax amount:", maxTaxPayer)
    print("Total taxes paid: ${0:02.2f}".format(overallTotalTax))
    print("Average of taxes paid: ${0:02.2f}".format(avgTax))
    print()
    print("Thank you for participating in my experimental program!")

    theFile.close()
main()

        
