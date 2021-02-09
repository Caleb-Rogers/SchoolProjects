##
## Name: Caleb Rogers
## Prog7Rogers.py
##
## Purpose:
## This program will present options on ways to manipulate numbers using arrays and helper functions
## 
## Inputs:
## Menu choice ("H", "M", "T', "G", "Q"), 10 grades for "H", up to 10 numbers and <enter> for "M",
## up to 10 negative numbers and a positive number and a target value for "T"
## 8 letters ("A", "B", "C", "D") for answers and again for key
##
## Output:
## Max, min, and avg of grades for "H", list of positives or list of negatives or list of positives and negatives for "M",
## array, target value, and number of times target value appears for "T", and grades for "G"
## 
## 
## Certification of Authenticity:
## I certify that this lab is my own work, but I discussed it with: Ryan Bahnsen
##

# function: maximum()
#
# This function calculates the maximum of the array
#
# Parameters: (listMax) = holds an array of 10 grades
#
# Returns: the maximum of the array
def maximum(listMax):

    # Initialization
    maxSoFar = -999999

    # Calculate and return maximum
    for value in listMax:
        if value > maxSoFar:
            maxSoFar = value
    return maxSoFar

# function: minimum()
#
# This function calculates the minimum of the array
#
# Parameters: (listMin) = holds an array of 10 grades
#
# Returns: the minimum of the array
def minimum(listMin):

    # Initialization
    minSoFar = 999999

    # Calculate and return minimum
    for value in listMin:
        if value < minSoFar:
            minSoFar = value
    return minSoFar

# function: average()
#
# This function calculates the average of the array
#
# Parameters: (listAvg) = holds an array of 10 grades
#
# Returns: the average of the array
def average(listAvg):

    # Initalization
    sumSoFar = 0
    count = 0

    # Calculate and return average
    for value in listAvg:
        sumSoFar += value
        count += 1
    average = sumSoFar / count
    return average
     
# function: posOrNeg()
#
# This function calculates if there are more positive numbers or negatives in the array
#
# Parameters: (listPosOrNeg) = holds an array up to 10 numbers
#
# Returns: none
def posOrNeg(listPosOrNeg):

    # Initalization
    posList = []
    negList = []
    positives = 0
    negatives = 0

    for value in listPosOrNeg:

        # Calculate list of positives
        if value > 0:
            posList.append(value)
            positives += 1

        # Calculate list of negatives
        elif value < 0:
            negList.append(value)
            negatives += 1
            
    # Output list of positives
    if positives > negatives:
        print()
        print("There are more positive numbers than negatives") 
        print("The list of positive numbers are:", posList)
        print()

    # Output list of negatives
    elif positives < negatives:
        print()
        print("There are more negative numbers than positives") 
        print("The list of negative numbers are:", negList)
        print()

    # Output list of positives and negatives
    else:
        print()
        print("There are the same number of positive numbers as negatives")
        print("The list of numbers are:", listPosOrNeg)
        print()
            
                
# function: numTimes()
#
# This function calculates number of times a target value appears in the array
#
# Parameters: (listTimes) = holds an array up to 10 negative numbers
#             (target) = holds a target value
#
# Returns: none
def numTimes(listTimes, target):

    # Calculate number of times target value appears
    numTarget = 0
    for value in listTimes:
        if value == target:
            numTarget += 1

    # Output the array, target value, and number of times target value appears
    print()
    print("The list of numbers entered are:", listTimes)
    print("The target value entered was:", target)
    print("The target value appeared:", numTarget, "time(s)")
    print()
    
# function: gradeQuiz()
#
# This function grades a Multiple Choice quiz with a key
#
# Parameters: (listAns) = holds an array of 8 answers
#             (listKey) = holds an array of 8 correct answers from the key
#
# Returns: Number of correct answers
def gradeQuiz(listAns, listKey):

    # Initalization
    correct = 0

    # Calculate number of correct answers
    for value in range(8):
        if listAns[value].upper() == listKey[value].upper():
            correct += 1
    return correct

def main():

    # Greeting
    print("This program will present options on ways to manipulate numbers")

    choice = "Z"
    while choice.upper() != "Q":

        # Menu and input choice
        print("Choose an option")
        print("Enter 'H' to handle grades")
        print("Enter 'M' to determine if there are more positive numbers or more negatives")
        print("Enter 'T' to determine how many times")
        print("Enter 'G' to grade a quiz")
        print("Enter 'Q' to quit the program")

        choice = input("Enter your choice: ")

        if choice.upper() == "H":

            # Initialization
            theList = []
            count = 0
            high = 0
            low = 0
            avg = 0

            # Input grades into a array
            print()
            print("Enter ten grades to calculate the maximum, minimum, and average of your grades")
            for nums in range(10):
                grades = int(input("Enter a answer ({}): ".format(nums + 1)))
                theList.append(grades)

            # Calculate max, min, and avg of grades
            high = maximum(theList)
            low = minimum(theList)
            avg = average(theList)

            # Output max, min, and avg of grades
            print("The maximum of your list of grades is:", high)
            print("The minimum of your list of grades is:", low)
            print("The average of your list of grades is:", avg)
            print()
            
        elif choice.upper() == "M":

            # Initialization
            theList = []
            count = 1
            nums = 0

            # Input numbers into a array
            print()
            print("Enter a list up to 10 numbers and click <enter> to continue")
            print("This will determine if there are more positive numbers than negatives")
            while nums != "" and count != 10:
                nums = input("Enter a Number ({}): ".format(count))
                if nums != "":  
                    nums = int(nums)
                    theList.append(nums)
                    count += 1

            # Calculate if more positives or negatives
            posOrNeg(theList)
                
        elif choice.upper() == "T":

            # Initialization
            theList = []
            nums = -999999
            count = 1

            # Input numbers into a array
            print()
            print("Enter a list up to 10 negative numbers and enter a positive number to continue")
            print("Then enter a target value")
            print("This will determine how many times the target value appears in the list")
            while count != 10 and nums < 0:
                nums = int(input("Enter a Number ({}): ".format(count)))
                if nums < 0:
                    theList.append(nums)
                count += 1

            # Input target value and calculate number of times target value is in array
            targetValue = int(input("Enter a Target Value: "))
            numTimes(theList, targetValue)
            
        elif choice.upper() == "G":

            # Initialization
            ansList = []
            keyList = []

            # Input numbers into array of answers and array of the key
            print()
            print("Enter the 8 answers (A, B, C, or D) from a Multiple Choice quiz")
            print("Then enter the 8 correct answers from the key")
            for nums in range(8):
                ans = input("Enter an answer ({}): ".format(nums + 1))
                while ans.upper() != "A" and ans.upper() != "B" and ans.upper() != "C" and ans.upper() != "D":
                    ans = input("Invalid input, enter the letter A, B, C, or D: ")
                ansList.append(ans)
            for nums in range(8):
                key = input("Enter a key ({}): ".format(nums + 1))
                while key.upper() != "A" and key.upper() != "B" and key.upper() != "C" and key.upper() != "D":
                    key = input("Invalid input, enter the letter A, B, C, or D: ")
                keyList.append(key)

            # Calculate grades                
            correct = gradeQuiz(ansList, keyList)
            percent = correct / 8

            if percent >= .90:
                grade = "A"
            elif percent >= .88:
                grade = "A-"
            elif percent >= .85:
                grade = "B+"
            elif percent >= .80:
                grade = "B"
            elif percent >= .78:
                grade = "B-"
            elif percent >= .75:
                grade = "C+"
            elif percent >= .70:
                grade = "C"
            elif percent >= .68:
                grade = "C-"
            elif percent >= .65:
                grade = "D+"
            elif percent >= .60:
                grade = "D"
            else:
                grade = "F"

            # Output grades
            print()
            print("This quiz received a", correct, "out of 8 which results a {:.0%}".format(percent))
            print("The grade on this quiz is:", grade)
            print()

        elif choice.upper() != "Q":

            # Validate menu choice
            print()
            print("Invalid choice, please enter a valid choice from the options below")
            print()

    # Closing
    print()
    print("Thank you in participating in Caleb's experimental program")

main()
