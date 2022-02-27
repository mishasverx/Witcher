import pygame as pg
from images import gui_images, pages
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

    def udpate(self, tr):
        self.image = gui_images["HP"][floor(tr.hp)]


class MP(pg.sprite.Sprite):
    def __init__(self, g1):
        super().__init__(g1)
        self.image = gui_images["MP"][7]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 25, 35

    def udpate(self, tr):
        self.image = gui_images["MP"][floor(tr.count_click)]


class Page(pg.sprite.Sprite):
    def __init__(self, g1, x, type):
        super().__init__(g1)
        self.type = type
        if self.type == 0 or self.type == 1:
            self.f = 40
            self.a = 10
        if self.type == 2:
            self.f = 48
            self.a = 8
        if self.type == 3:
            self.f = 84
            self.a = 7
        if self.type == 4 or self.type == 5:
            self.f = 45
            self.a = 9
        self.image = pages[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 100
        self.count = 0

    def update(self):
        if self.count >= self.f:
            self.count = 0
        self.image = pages[self.type][self.count // self.a]
        self.count += 1