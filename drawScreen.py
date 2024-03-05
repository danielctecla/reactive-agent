from agent import *

import pygame as pg
import random

n = 26 #rows
m = 42 #columns

BGPOSITION = (25,25)
BGSIZE = (25*m,25*n)

WHITE = (255, 255, 255)


table = [['' for _ in range(m)] for _ in range(n)] # 26 rows x 42 columns

def moveAgents(ragents: list, screen: pg.Surface) -> None:
    for ragent in ragents:
        ragent.move()
        pg.draw.rect(screen, (0, 0, 0), (ragent.col*25 + 25, ragent.row*25 + 25, 25, 25))

def updateScreen(screen: pg.Surface, ragents: list) -> None:
    screen.fill((105,105,105))
    pg.draw.rect(screen, (255, 255, 255), (BGPOSITION, BGSIZE))

    moveAgents(ragents, screen)

