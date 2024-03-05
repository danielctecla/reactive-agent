from drawScreen import *
import pygame as pg
import random

class Agent():
    # Constructor
    def __init__(self, mainObjects_: list):
        self.col = random.randint(0, m - 1)
        self.row = random.randint(0, n - 1)
        self.mainObjects = mainObjects_

        self.hasItem = False

    # Getters and setters
    def getPosition(self) -> tuple:
        return (self.col, self.row)
    
    def setPosition(self, col: int, row: int) -> None:
        self.col = col
        self.row = row

    def getHasItem(self) -> bool:
        return self.hasItem
    
    def invertHasItem(self) -> None:
        self.hasItem = not self.hasItem

    # Sensors for the agent
    def northSensor(self) -> bool:
        return self.row > 0 and table[self.row - 1][self.col] != 'O'
    
    def southSensor(self) -> bool:
        return self.row < n - 1 and table[self.row + 1][self.col] != 'O'
    
    def eastSensor(self) -> bool:
        return self.col < m - 1 and table[self.row][self.col + 1] != 'O'
    
    def westSensor(self) -> bool:
        return self.col > 0 and table[self.row][self.col - 1] != 'O'

    # Agent's behavior
    def randomStep(self) -> tuple:
        possibleSteps = []

        if self.northSensor():
            possibleSteps.append((-1, 0))
        if self.southSensor():
            possibleSteps.append((1, 0))
        if self.eastSensor():
            possibleSteps.append((0, 1))
        if self.westSensor():
            possibleSteps.append((0, -1))
        return random.choice(possibleSteps)

    def movetoMainObj(self) -> None:
        posibleSteps = []
        bestStep = (0, 0)
        bestDistance = 1000000

        if self.northSensor():
            posibleSteps.append((-1, 0))
        if self.southSensor():
            posibleSteps.append((1, 0))
        if self.eastSensor():
            posibleSteps.append((0, 1))
        if self.westSensor():
            posibleSteps.append((0, -1))

        for mainObject in self.mainObjects:
            for row,column in posibleSteps:
                distance = (abs(mainObject[0] - (self.row + row))**2 + abs(mainObject[1] - (self.col + column))**2) ** 0.5
                if distance < bestDistance:
                    bestDistance = distance
                    bestStep = (row, column)
        
        self.setPosition(self.col + bestStep[1], self.row + bestStep[0])
        
        if table[self.row][self.col] == 'M':
            self.invertHasItem()


    def move(self) -> None:
        if self.hasItem:
            self.movetoMainObj()
        else:
            row,column = self.randomStep()
            if table[self.row + row][self.col + column] == 'I':
                self.invertHasItem()
                table[self.row + row][self.col + column] = ''   
            self.setPosition(self.col + column, self.row + row)
    