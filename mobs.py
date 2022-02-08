import pygame as pg
from images import mobs_images
from random import choice


class Skeleton(pg.sprite.Sprite):
    def __init__(self, x, y, s, g1):
        super().__init__(g1)
        self.image = mobs_images['skeleton'][0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y, self.s = x, y, s
        self.mask = pg.mask.from_surface(self.image)
        self.count_walk_right = 0
        self.count_walk_left = 0
        self.hp = 10
        self.count_hit_left = 0
        self.count_hit_right = 0

        self.last_dir = True
        self.is_moving = True
        self.can_attack = True

    def walk(self, hero):
        if self.count_walk_right >= 70:
            self.count_walk_right = 0
        if self.count_walk_left >= 70:
            self.count_walk_left = 0
        if self.count_hit_right >= 48:
            self.count_hit_right = 0
        if self.count_hit_left >= 48:
            self.count_hit_left = 0
        if self.rect.x < hero.rect.x:
            self.last_dir = True
        else:
            self.last_dir = False

        if self.rect.x > hero.rect.x:
            if self.rect.x - (hero.rect.x + hero.rect.width) > -400:
                if self.last_dir:
                    self.rect.x += self.s
                    self.image = mobs_images["skeleton"][self.count_walk_left // 10]
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_walk_right += 1

                else:
                    self.rect.x -= self.s
                    self.image = pg.transform.flip(mobs_images["skeleton"][self.count_walk_left // 10], True, False)
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_walk_left += 1
            else:
                if self.last_dir:
                    self.image = mobs_images["skeleton_hit"][self.count_hit_right // 6]
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_hit_right += 1
                else:
                    self.mask = pg.mask.from_surface(self.image)
                    self.image = pg.transform.flip(mobs_images["skeleton_hit"][self.count_hit_left // 6], True, False)
                    self.count_hit_left += 1
        else:
            if hero.rect.x - (self.rect.x + self.rect.width) > -400:
                if self.last_dir:
                    self.rect.x += self.s
                    self.image = mobs_images["skeleton"][self.count_walk_right // 10]
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_walk_right += 1

                else:
                    self.rect.x -= self.s
                    self.image = pg.transform.flip(mobs_images["skeleton"][self.count_walk_left // 10], True, False)
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_walk_left += 1
            else:
                if self.last_dir:
                    self.image = mobs_images["skeleton_hit"][self.count_hit_right // 6]
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_hit_right += 1
                else:
                    self.mask = pg.mask.from_surface(self.image)
                    self.image = pg.transform.flip(mobs_images["skeleton_hit"][self.count_hit_left // 6], True, False)
                    self.count_hit_left += 1

    def update(self, t):
        a = choice([0, 1])
        if self.hp <= 0:
            self.hp = 10
            if a == 0:
                self.rect.x = 2100
            else:
                self.rect.x = -600
        if self.can_attack:
            if pg.sprite.collide_mask(self, t):
                t.hp -= 0.01


class Drowner(pg.sprite.Sprite):
    def __init__(self, x, y, s, g1):
        super().__init__(g1)
        self.image = mobs_images['drowner'][0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y, self.s = x, y, s
        self.mask = pg.mask.from_surface(self.image)
        self.count_walk_right = 0
        self.count_walk_left = 0
        self.hp = 10
        self.count_hit_left = 0
        self.count_hit_right = 0

        self.last_dir = True
        self.is_moving = True
        self.can_attack = True

    def walk(self, hero):
        if self.count_walk_right >= 40:
            self.count_walk_right = 0
        if self.count_walk_left >= 40:
            self.count_walk_left = 0
        if self.count_hit_right >= 70:
            self.count_hit_right = 0
        if self.count_hit_left >= 70:
            self.count_hit_left = 0
        if self.rect.x < hero.rect.x:
            self.last_dir = True
        else:
            self.last_dir = False

        if self.rect.x > hero.rect.x:
            if self.rect.x - (hero.rect.x + hero.rect.width) > -400:
                if self.last_dir:
                    self.rect.x += self.s
                    self.image = pg.transform.flip(mobs_images["drowner"][self.count_walk_right // 10],
                                                   True, False)
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_walk_right += 1

                else:
                    self.rect.x -= self.s
                    self.image = mobs_images["drowner"][self.count_walk_left // 10]
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_walk_left += 1
            else:
                if self.last_dir:
                    self.image = pg.transform.flip(mobs_images["drowner_hit"][self.count_hit_right // 10],
                                                   True, False)
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_hit_right += 1
                else:
                    self.mask = pg.mask.from_surface(self.image)
                    self.image = mobs_images["drowner_hit"][self.count_hit_left // 10]
                    self.count_hit_left += 1
        else:
            if hero.rect.x - (self.rect.x + self.rect.width) > -400:
                if self.last_dir:
                    self.rect.x += self.s
                    self.image = pg.transform.flip(mobs_images["drowner"][self.count_walk_right // 10],
                                                   True, False)
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_walk_right += 1

                else:
                    self.rect.x -= self.s
                    self.image = mobs_images["drowner"][self.count_walk_left // 10]
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_walk_left += 1
            else:
                if self.last_dir:
                    self.image = pg.transform.flip(mobs_images["drowner_hit"][self.count_hit_right // 10],
                                                   True, False)
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_hit_right += 1
                else:
                    self.mask = pg.mask.from_surface(self.image)
                    self.image = mobs_images["drowner_hit"][self.count_hit_left // 10]
                    self.count_hit_left += 1

    def update(self, t):
        a = choice([0, 1])
        if self.hp <= 0:
            if a == 0:
                self.rect.x = 3100
            else:
                self.rect.x = -1000
            self.hp = 10
        if self.can_attack:
            if pg.sprite.collide_mask(self, t):
                t.hp -= 0.01


class Mage(pg.sprite.Sprite):
    def __init__(self, x, y, s, g1):
        super().__init__(g1)
        self.image = mobs_images['mage_walk'][0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y, self.s = x, y, s
        self.mask = pg.mask.from_surface(self.image)
        self.count_walk_right = 0
        self.count_walk_left = 0
        self.hp = 20
        self.count_hit_left = 0
        self.count_hit_right = 0
        self.can_attack = True
        self.last_dir = True
        self.is_moving = True

    def walk(self, hero):
        if self.count_walk_right >= 36:
            self.count_walk_right = 0
        if self.count_walk_left >= 35:
            self.count_walk_left = 0
        if self.count_hit_right >= 100:
            self.count_hit_right = 0
        if self.count_hit_left >= 100:
            self.count_hit_left = 0
        if self.rect.x < hero.rect.x:
            self.last_dir = True
        else:
            self.last_dir = False
        if self.rect.x > hero.rect.x:
            if self.rect.x - (hero.rect.x + hero.rect.width) > 200:
                if self.last_dir:
                    self.rect.x += self.s
                    self.image = pg.transform.flip(mobs_images["mage_walk"][self.count_walk_right // 9],
                                                   True, False)
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_walk_right += 1
                    self.can_attack = False

                else:
                    self.rect.x -= self.s
                    self.image = mobs_images["mage_walk"][self.count_walk_left // 9]
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_walk_left += 1
                    self.can_attack = False
            else:
                if self.last_dir:
                    self.image = pg.transform.flip(mobs_images["mage_hit"][self.count_hit_right // 10],
                                                   True, False)
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_hit_right += 1
                    self.can_attack = True
                else:
                    self.mask = pg.mask.from_surface(self.image)
                    self.image = mobs_images["mage_hit"][self.count_hit_left // 10]
                    self.count_hit_left += 1
                    self.can_attack = True
        else:
            if hero.rect.x - (self.rect.x + self.rect.width) > 200:
                if self.last_dir:
                    self.rect.x += self.s
                    self.image = pg.transform.flip(mobs_images["mage_walk"][self.count_walk_right // 9],
                                                   True, False)
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_walk_right += 1
                    self.can_attack = False
                else:
                    self.rect.x -= self.s
                    self.image = mobs_images["mage_walk"][self.count_walk_left // 9]
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_walk_left += 1
                    self.can_attack = False
            else:
                if self.last_dir:
                    self.image = pg.transform.flip(mobs_images["mage_hit"][self.count_hit_right // 10],
                                                   True, False)
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_hit_right += 1
                    self.can_attack = True
                else:
                    self.mask = pg.mask.from_surface(self.image)
                    self.image = mobs_images["mage_hit"][self.count_hit_left // 10]
                    self.count_hit_left += 1
                    self.can_attack = True

    def update(self, t, l):
        a = choice([0, 1])
        if self.hp <= 0:
            if a == 0:
                self.rect.x = 3600
            else:
                self.rect.x = -2000
            self.hp = 20
        if -200 <= self.rect.x < 1600:
            if pg.sprite.collide_mask(self, t):
                t.hp -= 0.01
            if l.count_hit - 1 == 0:
                l.rect.x = t.rect.x + 50
            l.hit(t)
        else:
            l.rect.x = -1000


class Mouse(pg.sprite.Sprite):
    def __init__(self, h, w, x, y, s, g1):
        super().__init__(g1)

        self.fly_count1 = 0
        self.fly_count2 = 0
        self.h, self.w, self.s = h, w, s
        self.image = pg.transform.scale(mobs_images["mouse"][2], [self.h, self.w])
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.mask = pg.mask.from_surface(self.image)

    def fly_right(self):
        if self.fly_count2 >= 28:
            self.fly_count2 = 0
        self.image = pg.transform.flip(pg.transform.scale(mobs_images["mouse"][self.fly_count2 // 4], [self.h, self.w]),
                                       True, False)
        self.rect.x += self.s
        self.fly_count2 += 1
        if self.rect.x > 1600:
            self.rect.x = -300

    def fly_left(self):
        if self.fly_count1 >= 28:
            self.fly_count1 = 0
        self.image = pg.transform.scale(mobs_images["mouse"][self.fly_count1 // 4], [self.h, self.w])
        self.rect.x -= self.s
        self.fly_count1 += 1
        if self.rect.x < -300:
            self.rect.x = 1600 + 300