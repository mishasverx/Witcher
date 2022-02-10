import pygame as pg
from images import obj_images, witcher_images, mobs_images


class Portal(pg.sprite.Sprite):
    def __init__(self, pos, g1):
        super().__init__(g1)
        self.image = obj_images['portal_o'][0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
        self.count = 0
        self.pos = pos

    def go(self):
        if self.pos:
            self.rect.x, self.rect.y = 2000, 450
            if self.count >= 90:
                self.count = 0
            self.image = obj_images["portal_o"][self.count // 10]
            self.mask = pg.mask.from_surface(self.image)
            self.count += 1
        else:
            self.rect.x, self.rect.y = -160, 450
            if self.count >= 90:
                self.count = 0
            self.image = pg.transform.flip(obj_images["portal_o"][self.count // 10], True, False)
            self.mask = pg.mask.from_surface(self.image)
            self.count += 1


class Light(pg.sprite.Sprite):
    def __init__(self, x, y, f, g1):
        super().__init__(g1)
        self.image = mobs_images['mage_hit_light'][0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.f = f
        self.mask = pg.mask.from_surface(self.image)
        self.count_hit = 0
        self.count = 0
    def hit(self, t):
        if self.count_hit >= 70:
            self.count_hit = 0
        self.image = mobs_images["mage_hit_light"][self.count_hit // 5]
        self.mask = pg.mask.from_surface(self.image)
        self.count_hit += 1
        if pg.sprite.collide_mask(self, t):
            t.hp -= 0.02


fireballs = []


class Fire(pg.sprite.Sprite):
    def __init__(self, x, y, dir, g1, g2):
        super().__init__(g1, g2)
        self.dir = dir
        self.g = g1
        if not self.dir:
            self.image = pg.transform.flip(witcher_images["fire"][0], True, False)
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = x + 160, y + 150
        else:
            self.image = witcher_images["fire"][0]
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = x + 210, y + 150
        self.mask = pg.mask.from_surface(self.image)
        self.count = 0
        self.doing = True

    def move(self):
        if self.count >= 70:
            self.count = 0
        if self.doing:
            if not self.dir:
                self.rect.x -= 10
                self.image = witcher_images["fire"][self.count // 7]
                self.mask = pg.mask.from_surface(self.image)
                self.count += 1
                if self.rect.x < -100:
                    self.doing = False
            else:
                self.rect.x += 10
                self.image = pg.transform.flip(witcher_images["fire"][self.count // 7], True, False)
                self.mask = pg.mask.from_surface(self.image)
                self.count += 1
                if self.rect.x > 1600:
                    self.doing = False
        else:
            self.g.remove(self)
            del self
