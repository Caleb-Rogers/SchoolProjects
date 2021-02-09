##
## Name: Caleb Rogers
## Prog1Rogers.py
##
## Purpose: Program to convert degrees Celsius to degrees Fahrenheit
##
## Input: degrees Celsius 
##
## Output: degrees Fahrenheit
##
## Certification of Authenticity:
## I certify that this lab is entirely my own work, but i discussed it
## with: Matt and Madeline
##

def main():
    print("This program is designed to convert degrees Celsius to degrees Fahrenheit")
#input for range number
    num = int(input("How many temperatures would you like to be calculated? "))
    for i in range(num):
#input for celsius
        celsius = float(input("What is the Celsius temperature? "))
#calculation of celsius to fahrenheit
        fahrenheit = (9/5) * celsius + 32
#output for fahrenheit
        print("The temerature is", fahrenheit, "degrees fahrenheit")
    print("Thanks for participating in this experimental program")
main()

