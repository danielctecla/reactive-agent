from drawScreen import *
import pygame as pg
import random

class Agent():
    # Constructor
    def __init__(self):
        self.col = random.randint(0, m - 1)
        self.row = random.randint(0, n - 1)

        self.hasItem = False

    # Getters and setters
    def getPosition(self) -> tuple:
        return (self.col, self.row)
    
    def getHasItem(self) -> bool:
        return self.hasItem
    
    def setPosition(self, col: int, row: int) -> None:
        self.col = col
        self.row = row

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

    def move(self) -> None:
        if self.hasItem:
            pass
        else:
            step = self.randomStep()
            self.setPosition(self.col + step[1], self.row + step[0])
    