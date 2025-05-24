import pygame as pg
mw = pg.display.set_mode((500, 500))
clock = pg.time.Clock()
game = True
while game == True:
    pg.display.update()
    clock.tick(60)