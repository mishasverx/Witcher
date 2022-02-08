import pygame as pg
from images import gui_images
import sys
from math import floor


class Int(pg.sprite.Sprite):
    def __init__(self, g1):
        super().__init__(g1)
        self.image = gui_images["INT"][0]
        self.count = 0
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 25, 35

    def inter(self):
        fl = True
        if self.count >= 110:
            self.count = 0
        if fl:
            self.image = gui_images["INT"][self.count // 10]
            self.count += 1


class HP(pg.sprite.Sprite):
    def __init__(self, g1):
        super().__init__(g1)
        self.image = gui_images["HP"][16]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 25, 35
        self.fl = True

    def udpate(self, tr):
        if self.fl:
            self.image = gui_images["HP"][floor(tr.hp)]
            if floor(tr.hp) <= 0.5:
                pg.quit()
                sys.exit()


class MP(pg.sprite.Sprite):
    def __init__(self, g1):
        super().__init__(g1)
        self.image = gui_images["MP"][7]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 25, 35
        self.fl = True

    def udpate(self, tr):
        if self.fl:
            self.image = gui_images["MP"][floor(tr.count_click)]
