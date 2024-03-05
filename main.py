from agent import Agent
from drawScreen import *

import pygame as pg
import random

pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((1100, 700)) # 44 colums x 28 rows (each cell is 25x25 pixels)

obstacle(170)
items(60)

def main(ragents: list) -> None:
    running = True

    while running:
        clock.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        updateScreen(screen, ragents)
        pg.display.flip()


if __name__ == "__main__":
    ragent = Agent(mainObject())
    main([ragent])

pg.quit()
        
