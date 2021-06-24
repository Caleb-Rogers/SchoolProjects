##
## Name: Caleb Rogers
## Prog8Rogers.py
##
## Purpose:
## This program will present options to modify rectangles using classes and methods
## 
## Inputs:
## Menu choice ("W", "H", "F", "A", "P", "T", "D", "O", or "Q"),
## width for "W", height for "H", and fill style for "F"
##
## Output:
## Area for "A", perimeter for "P", text description for "T",
## drawing of rectangle for "D", and outline for "O"
## 
## Certification of Authenticity:
## I certify that this lab is entirely my own work.
##

from rectangleRogers import Rectangle

def main():

    print("This program will present options to modify rectangles")

    # Initialization
    width = 10
    height = 5
    fill = "*"
    rectangle = Rectangle(width, height, fill)
    choice = "Z"
        
    while choice.upper() != "Q":

        # Menu and Choice
        print("Choose an option")
        print("Enter 'W' to assign the width")
        print("Enter 'H' to assign the height")
        print("Enter 'F' to assign the fill style")
        print("Enter 'A' to calculate the area")
        print("Enter 'P' to calculate the perimeter")
        print("Enter 'T' to present a text description of the rectangle")
        print("Enter 'D' to draw the rectangle")
        print("Enter 'O' to draw the outline of the rectangle")
        print("Enter 'Q' to quit")

        choice = input("Enter your choice: ")
        print()

        if choice.upper() == "W":

            # Input and set width
            width = int(input("Enter the width you want to assign: "))
            while width <= 0:
                width = int(input("Invalid amount, enter a positive, whole number for a width: "))
            rectangle.setWidth(width)
            print("You're width of", width, "has been assigned to the rectangle")
            print()
            
        elif choice.upper() == "H":

            # Input and set height
            height = int(input("Enter the height you want to assign: "))
            while height <= 0:
                height = int(input("Invalid amount, enter a positive, whole number for a height: "))
            rectangle.setHeight(height)
            print("You're height of", height, "has been assigned to the rectangle")
            print()

        elif choice.upper() == "F":

            # Input and set fill style
            fill = input("Enter the fill style you want to assign: ")
            rectangle.setFillStyle(fill)
            print("You're fill style of (" + fill + ") has been assigned to the rectangle")
            print()

        elif choice.upper() == "A":

            # Calculate and output area
            area = rectangle.calcArea()
            print("The area of the rectangle is:", area)
            print()

        elif choice.upper() == "P":

            # Calculate and output perimeter
            perimeter = rectangle.calcPerimeter()
            print("The perimeter of the rectangle is:", perimeter)
            print()

        elif choice.upper() == "T":

            # Get and output the text description
            print("The rectangle has the following characteristics")
            print("Width:", rectangle.getWidth())
            print("Height:", rectangle.getHeight())
            print("Fill Style:", rectangle.getFillStyle())
            print("Area:", rectangle.calcArea())
            print("Perimeter:", rectangle.calcPerimeter())
            print()

        elif choice.upper() == "D":

            # Output drawing of the rectangle
            rectangle.drawRectangle()
            print()

        elif choice.upper() == "O":

            # Output outline of the rectangle
            rectangle.drawOutline()
            print()

        elif choice.upper() != "Q":

            # Validate menu choice
            print("The choice you entered was invalid, please enter a choice from the options below")
            print()

    print("Thank you for participating in Caleb's experimental program")

main()
