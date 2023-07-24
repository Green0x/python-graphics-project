# 2026836
# Jamie Wheeler
# Programming Project
from graphics import *

# Function for drawing a grid around the patterns
def drawGrid(gridAmount):
    topX = 0
    botX = 100
    topY = 0
    botY = 100

    for i in range(gridAmount):
        rect = Rectangle(Point(topX, topY), Point(botX, botY))
        rect.draw(win)

        for i in range(gridAmount):
            rect = Rectangle(Point(topX, topY), Point(botX, botY))
            rect.draw(win)
            topX = topX + 100
            botX = botX + 100

        topX = 0
        botX = 100
        botY = botY + 100


# Function for creating final digit pattern
def drawPattern(start, end, colour1):
    topX = start      # Left and right position
    botX = topX + 10
    topY = end        # Up and down position
    botY = topY + 10

    for i in range(10):

        rect = Rectangle(Point(topX, topY), Point(botX, botY))
        rect.draw(win)
        rect.setFill(colour1)
        topX = topX + 10
        botX = botX + 10
        botY = botY - 10
        topY = topY - 10


# Function for creating diamond polygon
def createDiamond(top, left, bot, right, colour3):



    triTopX = top
    triLeftX = left
    triBotX = bot
    triRightX = right

    # This sets how many diamonds are drawn if the grid size is 7 instead of 5
    downAmount = 8
    if gridSize == 7:
        downAmount = 13

    # These are always the same
    triTopY = 100
    triLeftY = 110
    triBotY = 120
    triRightY = 110

    triLeftY2 = triLeftY
    triRightY2 = triRightY
    triBotY2 = triBotY
    triTopY2 = triTopY


    for i in range(2):


        tri = Polygon(Point(triLeftX, triLeftY), Point(triBotX, triBotY), Point(triRightX, triRightY), Point(triTopX, triTopY))
        tri.draw(win)
        tri.setFill(colour3)

        for i in range(downAmount):

            tri = Polygon(Point(triLeftX, triLeftY2), Point(triBotX, triBotY2), Point(triRightX, triRightY2), Point(triTopX, triTopY2))
            tri.draw(win)
            triLeftY2 = triLeftY2 + 40
            triRightY2 = triRightY2 + 40
            triBotY2 = triBotY2 + 40
            triTopY2 = triTopY2 + 40

        triLeftY2 = triLeftY
        triRightY2 = triRightY
        triBotY2 = triBotY
        triTopY2 = triTopY

        triLeftX = triLeftX + 40
        triRightX = triRightX + 40
        triBotX = triBotX + 40
        triTopX = triTopX + 40


# Function for creating the penultimate pattern
def drawPattern2(start, end, colour2):
    topX = start          # Left and right position
    botX = topX + 20
    topY = end            # Up and down position
    botY = topY + 20

    botY2 = botY
    topY2 = topY

    circX = start + 10
    circY = end + 10
    circY2 = circY
    circX2 = circX



    for i in range(5):
        rect = Rectangle(Point(topX, topY), Point(botX, botY))
        rect.draw(win)
        rect.setFill(colour2)
        for i in range(5):
            rect2 = Rectangle(Point(topX, topY2), Point(botX, botY2))
            rect2.draw(win)
            rect2.setFill(colour2)
            topY2 = topY2 + 20
            botY2 = botY2 + 20

        topX = topX + 20
        botX = botX + 20
        topY2 = topY
        botY2 = botY
    for i in range(5):

        circ = Circle(Point(circX, circY), 5)
        circ.draw(win)
        circ.setFill("white")
        for i in range(5):
            circ2 = Circle(Point(circX2, circY2), 5)
            circ2.draw(win)
            circ2.setFill("white")
            circY2 = circY2 + 20


        circX = circX + 20
        circY2 = circY
        circX2 = circX

# Main function
def main():

    colour2 = ""
    colour3 = ""

    colours = ["red", "green", "blue", "magenta", "orange", "cyan"] # Set valid colours
    a = True
    while a == True:
        colour1 = input("Enter colour 1: ")
        for colour in colours:
            if colour == colour1:
                a = False

    # b = True
    # while b == True:
    #     colour2 = input("Enter colour 2: ")
    #     for colour in colours:
    #         if colour == colour2:
    #             b = False

    # c = True
    # while c == True:
    #     colour3 = input("Enter colour 3: ")
    #     for colour in colours:
    #         if colour == colour3:
    #             c = False

# Create top and bottom row patterns
    posX = 0
    posY = 90
    for i in range(gridSize):
        rowSize = gridSize * 100 - 10
        drawPattern(posX, posY, colour1)
        posY = rowSize
        drawPattern(posX, posY, colour1)
        posX = posX + 100
        posY = 90

# Create downward pattern
    posX2 = 0
    posY2 = 90
    for i in range(gridSize):

        rowSize2 = gridSize * 100 - 100
        drawPattern(posX2, posY2, colour1)
        posX2 = rowSize2
        drawPattern(posX2, posY2, colour1)
        posY2 = posY2 + 100
        posX2 = 0


# Create second row pattern
    posX4 = 100
    posY4 = 100
    for i in range(gridSize - 2):
        rowSize4 = gridSize * 100 - 200
        posX4 = rowSize4
        drawPattern2(posX4, posY4, colour2)
        posX4 = posX4 - 100
        drawPattern2(posX4, posY4, colour2)
        if gridSize == 7:
            posX4 = posX4 - 100
            drawPattern2(posX4, posY4, colour2)
            posX4 = posX4 - 100
            drawPattern2(posX4, posY4, colour2)
        posX4 = posX4 - 100
        drawPattern2(posX4, posY4, colour2)
        posY4 = posY4 + 100

# Create diamond patterns
    left = 120
    bot = 130
    right = 140
    top = 130
    for i in range(gridSize - 2):
        createDiamond(top, left, bot, right, colour3)
        left = left + 100
        bot = bot + 100
        right = right + 100
        top = top + 100


# Program starts here
print("Welcome to the patch designer")
while True:
    size = int(input("Which size window would you like? "))
    if size == 5 or size == 7:
        break
    print("Please enter either 5 or 7")
win = GraphWin("Patch Design", size * 100, size * 100)
drawGrid(size)
gridSize = size
main()