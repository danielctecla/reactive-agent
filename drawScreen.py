from agent import *

import pygame as pg
import random

n = 26 #rows
m = 42 #columns

BGPOSITION = (25,25)
BGSIZE = (25*m,25*n)

OBSTACLES = 100

WHITE = (255, 255, 255)


table = [['' for _ in range(m)] for _ in range(n)] # 26 rows x 42 columns


def mainObject() -> None:
    row = random.randint(0, n-1)
    col = random.randint(0, m-1)
    table[row][col] = 'M'
    return (row, col)
    
def obstacle(num: int) -> None:
    for i in range(num):
        row = random.randint(0, n-1)
        col = random.randint(0, m-1)
        if table[row][col] == '':
            table[row][col] = 'O'
        else:
            i -= 1

def items(num: int) -> None:
    for i in range(num):
        row = random.randint(0, n-1)
        col = random.randint(0, m-1)
        if table[row][col] == '':
            table[row][col] = 'I'
        else:
            i -= 1

def drawObjects(screen: pg.Surface) -> None:
    for i in range(n):
        for j in range(m):
            if table[i][j] == 'M':
                pg.draw.rect(screen, (255, 0, 0), (j*25 + 25, i*25 + 25, 25, 25))
            if table[i][j] == 'O':
                pg.draw.rect(screen, (0, 0, 0), (j*25 + 25, i*25 + 25, 25, 25))
            if table[i][j] == 'I':
                pg.draw.rect(screen, (0, 255, 0), (j*25 + 25, i*25 + 25, 25, 25))

def moveAgents(ragents: list, screen: pg.Surface) -> None:
    for ragent in ragents:
        ragent.move()
        pg.draw.rect(screen, (25,25,112), (ragent.col*25 + 25, ragent.row*25 + 25, 25, 25))

def updateScreen(screen: pg.Surface, ragents: list) -> None:
    screen.fill((0,0,0))
    pg.draw.rect(screen, (220,220,220), (BGPOSITION, BGSIZE))

    drawObjects(screen)
    moveAgents(ragents, screen)