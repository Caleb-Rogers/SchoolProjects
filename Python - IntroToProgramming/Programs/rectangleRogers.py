"""
File: rectangleRogers.py
<Resources to modify a rectangle>
"""

class Rectangle:

    def __init__(self, initalWidth, initalHeight, initalFill):
        """Initializes instance variables"""
        self.myWidth = initalWidth
        self.myHeight = initalHeight
        self.myFillStyle = initalFill

    def getWidth(self):
        """Returns the rectangle's width"""
        return self.myWidth

    def getHeight(self):
        """Returns the rectangle's height"""
        return self.myHeight

    def getFillStyle(self):
        """Returns the rectangle's fill style"""
        return self.myFillStyle

    def setWidth(self, newWidth):
        """Sets the rectangle's width"""
        self.myWidth = newWidth
        
    def setHeight(self, newHeight):
        """Sets the rectangle's height"""
        self.myHeight = newHeight

    def setFillStyle(self, newFillStyle):
        """Sets the rectangle's fill style"""
        self.myFillStyle = newFillStyle

    def calcArea(self):
        """Computes and returns area of the rectangle"""
        area = self.myWidth * self.myHeight
        return area
        
    def calcPerimeter(self):
        """Computes and returns perimeter of the rectangle"""
        perimeter = (self.myWidth * 2) + (self.myHeight * 2)
        return perimeter
        
    def drawRectangle(self):
        """Uses rectangle's dimensions to draw the rectangle"""
        for i in range(self.myHeight):
                for j in range(self.myWidth):
                    print(self.myFillStyle, end="")
                print()

    def drawOutline(self):
        """Uses rectangle's dimensions to draw an outline of the rectangle"""
        for i in range(1, self.myHeight + 1):
            for j in range(1, self.myWidth + 1):
                if i == 1 or i == self.myHeight or j == 1 or j == self.myWidth:
                    print(self.myFillStyle, end="")
                else:
                    print(" ", end="")
            print()


