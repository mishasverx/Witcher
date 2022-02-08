import pygame as pg


class Map(pg.sprite.Sprite):
    def __init__(self, type, g1):
        super().__init__(g1)
        if type == 0:
            self.image = pg.image.load("source/boloto.png")
        else:
            self.image = pg.image.load("source/background_3.png")
        self.rect = self.image.get_rect()
        self.rect.x = -100