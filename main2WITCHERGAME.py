import pygame as pg
from player import Withcer
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pg.init()
pg.display.set_caption("WITCHER")
width = 1600
height = 900
x, y = 150, 600
size = width, height
screen = pg.display.set_mode(size)

running = True
FPS = 60
clock = pg.time.Clock()
bg = pg.transform.scale2x(pg.image.load("source/background.png"))
screen.blit(bg, (0, -850))
w = Withcer()

class Map:
    pass


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        w.moving()
        clock.tick(FPS)
        pg.display.flip()
pg.quit()
