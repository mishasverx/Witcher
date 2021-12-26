import pygame as pg
import pygame.sprite


class Map:
    def __init__(self, bg, count):
        x, y = 0, 0
        backg = pg.image.load(bg)
        a = backg.get_size()
        for i in range(count):
            screen.blit(backg, (x, y))
            x += a[0]
            y += a[1]