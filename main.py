import pygame as pg
import os
import sys
from math import floor
from random import choice

pg.init()
pg.display.set_caption("WITCHER")
width, height = 1600, 900
size = width, height
screen = pg.display.set_mode(size)
# ---------------------------------
all_sprites = pg.sprite.Group()  # группа всех спрайтов
witcher_sprites = pg.sprite.Group()  # группа спрайтов ведьмака
tile_group = pg.sprite.Group()  # группа спрайтов объектов
mouse_group = pg.sprite.Group()  # группа спрайтов мыши
mage_group = pg.sprite.Group()
fire_group = pg.sprite.Group()
light_group = pg.sprite.Group()
int_group = pg.sprite.Group()
hp_group = pg.sprite.Group()
mp_gpoup = pg.sprite.Group()
drowner_gpoup = pg.sprite.Group()
skeleton_group = pg.sprite.Group()
mobs_sprites = pg.sprite.Group()
# ---------------------------------
running = True
jump = False
FPS = 60
speed = 10
x_player, y_player = 0, 500
clock = pg.time.Clock()


# -------------------------------d


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
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


mouse_s = pg.sprite.Group()
mouse = pg.sprite.Sprite()
mouse.image = load_image("source/arrow.png")
mouse.rect = mouse.image.get_rect()
mouse_s.add(mouse)
pg.mouse.set_visible(False)
# 🡫🡫🡫🡫🡫🡫🡫🡫 изображения ведьмака
witcher_images = {
    "walk_right": [load_image("source/player/right/2.png"), load_image("source/player/right/3.png"),
                   load_image("source/player/right/2.png"), load_image("source/player/right/1.png")],
    "stand_right": [load_image("source/player/stand_right/1.png"), load_image("source/player/stand_right/2.png"),
                    load_image("source/player/stand_right/3.png"), load_image("source/player/stand_right/4.png"),
                    load_image("source/player/stand_right/5.png")],
    "right_hit": [load_image("source/player/right_hit/1.png"), load_image("source/player/right_hit/2.png"),
                  load_image("source/player/right_hit/3.png"), load_image("source/player/right_hit/4.png"),
                  load_image("source/player/right_hit/5.png")],
    "left_hit": [load_image("source/player/left_hit/1.png"), load_image("source/player/left_hit/2.png"),
                 load_image("source/player/left_hit/3.png"), load_image("source/player/left_hit/4.png"),
                 load_image("source/player/left_hit/5.png")],
    "run": [load_image("source/player/run/1.png"), load_image("source/player/run/2.png"),
            load_image("source/player/run/3.png"), load_image("source/player/run/4.png")],
    "jump": [load_image("source/player/jump/1.png"), load_image("source/player/jump/2.png"),
             load_image("source/player/jump/3.png"), load_image("source/player/jump/4.png"),
             load_image("source/player/jump/5.png")],
    "cast": [load_image("source/player/cast/1.png"), load_image("source/player/cast/2.png"),
             load_image("source/player/cast/3.png"), load_image("source/player/cast/3.png")],
    "fire": [load_image("source/player/magic/fire/1.png"), load_image("source/player/magic/fire/2.png"),
             load_image("source/player/magic/fire/3.png"), load_image("source/player/magic/fire/4.png"),
             load_image("source/player/magic/fire/5.png"), load_image("source/player/magic/fire/6.png"),
             load_image("source/player/magic/fire/7.png"), load_image("source/player/magic/fire/8.png"),
             load_image("source/player/magic/fire/9.png"), load_image("source/player/magic/fire/10.png")]
}
# 🡩🡩🡩🡩🡩🡩🡩🡩 изображения ведьмака
mobs_images = {
    "mouse": [load_image("source/mobs/mouse/1.png"), load_image("source/mobs/mouse/2.png"),
              load_image("source/mobs/mouse/3.png"), load_image("source/mobs/mouse/4.png"),
              load_image("source/mobs/mouse/5.png"), load_image("source/mobs/mouse/6.png"),
              load_image("source/mobs/mouse/7.png")],
    "mage_walk": [load_image("source/mobs/mage/walk/1.png"), load_image("source/mobs/mage/walk/2.png"),
                  load_image("source/mobs/mage/walk/3.png"), load_image("source/mobs/mage/walk/2.png")],
    "mage_hit": [load_image("source/mobs/mage/hit/1.png"), load_image("source/mobs/mage/hit/2.png"),
                 load_image("source/mobs/mage/hit/3.png"), load_image("source/mobs/mage/hit/4.png"),
                 load_image("source/mobs/mage/hit/5.png"), load_image("source/mobs/mage/hit/6.png"),
                 load_image("source/mobs/mage/hit/7.png"), load_image("source/mobs/mage/hit/8.png"),
                 load_image("source/mobs/mage/hit/9.png"), load_image("source/mobs/mage/hit/10.png")],
    "mage_hit_light": [load_image("source/mobs/mage/hit_mage/1.png"), load_image("source/mobs/mage/hit_mage/2.png"),
                       load_image("source/mobs/mage/hit_mage/3.png"), load_image("source/mobs/mage/hit_mage/4.png"),
                       load_image("source/mobs/mage/hit_mage/5.png"), load_image("source/mobs/mage/hit_mage/6.png"),
                       load_image("source/mobs/mage/hit_mage/7.png"), load_image("source/mobs/mage/hit_mage/8.png"),
                       load_image("source/mobs/mage/hit_mage/9.png"), load_image("source/mobs/mage/hit_mage/10.png"),
                       load_image("source/mobs/mage/hit_mage/11.png"), load_image("source/mobs/mage/hit_mage/12.png"),
                       load_image("source/mobs/mage/hit_mage/13.png"), load_image("source/mobs/mage/hit_mage/14.png")],
    "drowner": [load_image("source/mobs/drowner/walk/1.png"), load_image("source/mobs/drowner/walk/2.png"),
                load_image("source/mobs/drowner/walk/3.png"), load_image("source/mobs/drowner/walk/4.png")],
    "drowner_hit": [load_image("source/mobs/drowner/hit/1.png"), load_image("source/mobs/drowner/hit/2.png"),
                    load_image("source/mobs/drowner/hit/3.png"), load_image("source/mobs/drowner/hit/4.png"),
                    load_image("source/mobs/drowner/hit/5.png"), load_image("source/mobs/drowner/hit/6.png"),
                    load_image("source/mobs/drowner/hit/7.png")],
    "skeleton": [load_image("source/mobs/skeleton/walk/1.png"), load_image("source/mobs/skeleton/walk/2.png"),
                 load_image("source/mobs/skeleton/walk/3.png"), load_image("source/mobs/skeleton/walk/4.png"),
                 load_image("source/mobs/skeleton/walk/5.png"), load_image("source/mobs/skeleton/walk/6.png"),
                 load_image("source/mobs/skeleton/walk/7.png")],
    "skeleton_hit": [load_image("source/mobs/skeleton/hit/1.png"), load_image("source/mobs/skeleton/hit/2.png"),
                     load_image("source/mobs/skeleton/hit/3.png"), load_image("source/mobs/skeleton/hit/4.png"),
                     load_image("source/mobs/skeleton/hit/5.png"), load_image("source/mobs/skeleton/hit/6.png"),
                     load_image("source/mobs/skeleton/hit/7.png"), load_image("source/mobs/skeleton/hit/8.png")]
}
gui_images = {
    "INT": [load_image("source/GUI/int/1.png"), load_image("source/GUI/int/2.png"),
            load_image("source/GUI/int/3.png"), load_image("source/GUI/int/4.png"),
            load_image("source/GUI/int/5.png"), load_image("source/GUI/int/6.png"),
            load_image("source/GUI/int/7.png"), load_image("source/GUI/int/8.png"),
            load_image("source/GUI/int/9.png"), load_image("source/GUI/int/10.png"),
            load_image("source/GUI/int/11.png")],
    "HP": [load_image("source/GUI/hp/0.png"), load_image("source/GUI/hp/1.png"), load_image("source/GUI/hp/2.png"),
           load_image("source/GUI/hp/3.png"), load_image("source/GUI/hp/4.png"),
           load_image("source/GUI/hp/5.png"), load_image("source/GUI/hp/6.png"),
           load_image("source/GUI/hp/7.png"), load_image("source/GUI/hp/8.png"),
           load_image("source/GUI/hp/9.png"), load_image("source/GUI/hp/10.png"),
           load_image("source/GUI/hp/11.png"), load_image("source/GUI/hp/12.png"), load_image("source/GUI/hp/13.png"),
           load_image("source/GUI/hp/14.png"), load_image("source/GUI/hp/15.png"), load_image("source/GUI/hp/16.png")],
    "MP": [load_image("source/GUI/mp/0.png"), load_image("source/GUI/mp/1.png"), load_image("source/GUI/mp/2.png"),
           load_image("source/GUI/mp/3.png"), load_image("source/GUI/mp/4.png"),
           load_image("source/GUI/mp/5.png"), load_image("source/GUI/mp/6.png"),
           load_image("source/GUI/mp/7.png")]
}
obj_images = {
    "portal_b": [load_image("source/obj/portal_b/1.png"), load_image("source/obj/portal_b/2.png"),
                 load_image("source/obj/portal_b/3.png"),
                 load_image("source/obj/portal_b/4.png"), load_image("source/obj/portal_b/5.png"),
                 load_image("source/obj/portal_b/6.png"), load_image("source/obj/portal_b/7.png"),
                 load_image("source/obj/portal_b/8.png"), load_image("source/obj/portal_b/9.png")]
}


# class Camera:
#     # зададим начальный сдвиг камеры
#     def __init__(self, camera_func, width, height):
#         self.camera_func = camera_func
#         self.state = pg.Rect(0, 0, width, height)
#
#     # сдвинуть объект obj на смещение камеры
#     def apply(self, target):
#         return target.rect.move(self.state.topleft)
#
#     # позиционировать камеру на объекте target
#     def update(self, target):
#         self.state = self.camera_func(self.state, target.rect)
#
#
# def camera_func(camera, target_rect):
#     l = -target_rect.x + 800
#     t = -target_rect.y + 450
#     w, h = camera.width, camera.height
#
#     l = min(0, l)
#     l = max(-(camera.width - 1600), l)
#     t = max(-(camera.height - 900), t)
#     t = min(0, t)


class Portal(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = obj_images['portal_b'][0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
        self.count = 0
        self.pos = pos

    def go(self, x, y):
        if self.pos:
            self.rect.x, self.rect.y = x, y
            if self.count >= 90:
                self.count = 0
            self.image = obj_images["portal_b"][self.count // 10]
            self.mask = pg.mask.from_surface(self.image)
            self.count += 1
        else:
            self.rect.x, self.rect.y = x, y
            if self.count >= 90:
                self.count = 0
            self.image = pg.transform.flip(obj_images["portal_b"][self.count // 10], True, False)
            self.mask = pg.mask.from_surface(self.image)
            self.count += 1


class Light(pg.sprite.Sprite):
    def __init__(self, x, y, f):
        super().__init__(light_group)
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


class Skeleton(pg.sprite.Sprite):
    def __init__(self, x, y, s):
        super().__init__(skeleton_group, mobs_sprites)
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
    def __init__(self, x, y, s):
        super().__init__(drowner_gpoup, mobs_sprites)
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
    def __init__(self, x, y, s):
        super().__init__(mage_group, mobs_sprites)
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


fireballs = []


class Witcher(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(witcher_sprites, mobs_sprites)
        self.image = witcher_images["right_hit"][0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.mask = pg.mask.from_surface(self.image)
        self.a = self.mask.count()
        # ------------------
        self.count_walk_right = 0  # cчетчик анимации ходьбы
        self.count_stand = 0  # cчетчик анимации стойки
        self.count_walk_left = 0
        self.count_hit = 0
        self.count_hit_2 = 0
        self.count_run_right = 0
        self.count_hit_strong_1 = 0
        self.count_hit_strong_2 = 0
        self.count_run_left = 0
        self.count_cast_1 = 0
        self.count_cast_2 = 0
        self.jump_count = 20
        self.anim_jump_count = 0
        self.count_click = 7
        # ------------------
        self.last_dir = True
        self.stay = False
        self.hp = 16
        self.is_jump = False
        self.is_hit = False
        self.fire = False
        self.is_cast = False
        self.fx = 1000
        self.is_strong_hit = False

        self.can_attack = False

        self.magic = False
        self.magic_count = 0

    def update(self, t):
        if self.is_hit and self.last_dir and t.rect.x > self.rect.x:
            if pg.sprite.collide_mask(self, t):
                t.hp -= 0.25
        if self.is_hit and not self.last_dir and t.rect.x < self.rect.x:
            if pg.sprite.collide_mask(self, t):
                t.hp -= 0.25
        if self.is_strong_hit and self.last_dir and t.rect.x > self.rect.x:
            if pg.sprite.collide_mask(self, t):
                t.hp -= 0.5
        if self.is_strong_hit and not self.last_dir and t.rect.x < self.rect.x:
            if pg.sprite.collide_mask(self, t):
                t.hp -= 0.5

    def move(self):
        keys = pg.key.get_pressed()
        if self.count_walk_right >= 36:
            self.count_walk_right = 0
        if self.count_walk_left >= 36:
            self.count_walk_left = 0
        if self.count_stand >= 75:
            self.count_stand = 0
        if self.rect.y > 500:
            self.rect.y = 500
        if keys[pg.K_d]:
            self.rect.x += speed
            right = True
            left = False
            self.stay = False
            self.last_dir = True
        elif keys[pg.K_a]:
            right = False
            left = True
            self.stay = False
            self.rect.x -= speed
            self.last_dir = False
        else:
            right = False
            left = False
            self.stay = True
            self.count_walk_left = 0
            self.count_walk_right = 0

        if right:
            self.image = witcher_images["walk_right"][self.count_walk_right // 9]
            self.mask = pg.mask.from_surface(self.image)
            self.count_walk_right += 1
        elif left:
            self.image = pg.transform.flip(witcher_images["walk_right"][self.count_walk_left // 9], True, False)
            self.mask = pg.mask.from_surface(self.image)

            self.count_walk_left += 1

        else:
            if self.last_dir:
                self.image = witcher_images["stand_right"][self.count_stand // 15]
                self.mask = pg.mask.from_surface(self.image)

                self.count_stand += 1
            else:
                self.image = pg.transform.flip(witcher_images["stand_right"][self.count_stand // 15], True, False)
                self.mask = pg.mask.from_surface(self.image)
                self.count_stand += 1

    def jump(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.is_jump = True
            self.stay = False

        if self.is_jump:
            if self.jump_count >= -20:
                self.rect.y -= self.jump_count
                self.jump_count -= 1
                self.anim_jump_count += 1
                if self.last_dir:
                    self.image = witcher_images["jump"][self.anim_jump_count // 9]
                else:
                    self.image = pg.transform.flip(witcher_images["jump"][self.anim_jump_count // 9], True, False)
            else:
                self.jump_count = 20
                self.anim_jump_count = 0
                self.is_jump = False
                self.stay = True

    def attack(self):
        keys = pg.mouse.get_pressed()
        keys_1 = pg.key.get_pressed()
        if self.count_hit >= 30:
            self.count_hit = 0
            self.is_hit = False
            self.can_attack = False
        if self.count_cast_1 >= 40:
            self.count_cast_1 = 0
            self.is_cast = False
        if self.count_cast_2 >= 40:
            self.count_cast_2 = 0
            self.is_cast = False
        if self.count_hit_2 >= 30:
            self.count_hit_2 = 0
            self.is_hit = False
            self.can_attack = False
        if self.count_hit_strong_1 >= 30:
            self.count_hit_strong_1 = 0
            self.is_strong_hit = False
            self.can_attack = False
        if self.count_hit_strong_2 >= 30:
            self.is_strong_hit = False
            self.count_hit_strong_2 = 0
            self.can_attack = False

        if keys[0]:
            self.is_hit = True
        if self.is_hit:
            if self.stay:
                self.can_attack = True
                if self.last_dir:
                    self.image = witcher_images["right_hit"][self.count_hit // 6]
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_hit += 1
                else:
                    self.image = pg.transform.flip(witcher_images["right_hit"][self.count_hit // 6], True, False)
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_hit += 1
            else:
                self.is_hit = False
        if keys[0] and keys_1[pg.K_LSHIFT]:
            self.is_strong_hit = True
        if self.is_strong_hit:
            if self.stay:
                self.can_attack = True
                if self.last_dir:
                    self.image = witcher_images["left_hit"][self.count_hit_strong_1 // 6]
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_hit_strong_1 += 1
                else:
                    self.image = pg.transform.flip(witcher_images["left_hit"][self.count_hit_strong_2 // 6], True,
                                                   False)
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_hit_strong_2 += 1
            else:
                self.is_strong_hit = False

        if keys[2]:
            self.is_cast = True
            self.count_click -= 0.2
            if self.count_click <= 1:
                self.count_click = 7
        if self.is_cast:
            if self.stay:
                if self.last_dir:
                    self.image = witcher_images["cast"][self.count_cast_1 // 10]
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_cast_1 += 1
                else:
                    self.image = pg.transform.flip(witcher_images["cast"][self.count_cast_2 // 10], True, False)
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_cast_2 += 1


class Fire(pg.sprite.Sprite):
    def __init__(self, x, y, dir):
        super().__init__(fire_group)
        self.dir = dir
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
            fire_group.remove(self)
            del self


class Mouse(pg.sprite.Sprite):
    def __init__(self, h, w, x, y, s):
        super().__init__(mouse_group)

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


class Int(pg.sprite.Sprite):
    def __init__(self):
        super().__init__(int_group)
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
    def __init__(self):
        super().__init__(hp_group)
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
    def __init__(self):
        super().__init__(mp_gpoup)
        self.image = gui_images["MP"][7]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 25, 35
        self.fl = True

    def udpate(self, tr):
        if self.fl:
            self.image = gui_images["MP"][floor(tr.count_click)]


backg = pg.image.load("source/boloto.png")
i = Int()
hp = HP()
mp = MP()
w = Witcher(500, 500)
m = Mage(-1000, 500, 5)
d = Drowner(2500, 500, 7)
s = Skeleton(1900, 500, 3)
p1, p2 = Portal(False), Portal(True)
l = Light(1000000, -20, True)
m1 = Mouse(230, 230, 0, 350, 7)
m2 = Mouse(115, 115, 1600 - 115, 500, 15)
m3 = Mouse(300, 300, 1300, 200, 10)
# camera = Camera(camera_func, 3200, 900)
while running:
    # camera.update(w)
    # for sprite in all_sprites:
    #     screen.blit(sprite.image, camera.apply(sprite))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEMOTION:
            mouse.rect.topleft = event.pos
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse.image = load_image("source/arrow2.png")
        elif event.type == pg.MOUSEBUTTONUP:
            mouse.image = load_image("source/arrow.png")
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
            if w.stay:
                f = Fire(w.rect.x, w.rect.y, w.last_dir)
                fireballs.append(f)

    for elem in fireballs:
        elem.move()
    screen.blit(backg, (0, 0))
    all_sprites.draw(screen)
    tile_group.draw(screen)
    mage_group.draw(screen)
    mouse_group.draw(screen)
    fire_group.draw(screen)
    drowner_gpoup.draw(screen)
    skeleton_group.draw(screen)
    witcher_sprites.draw(screen)
    light_group.draw(screen)
    int_group.draw(screen)
    hp_group.draw(screen)
    mp_gpoup.draw(screen)
    if pg.mouse.get_focused():
        mouse_s.draw(screen)
    clock.tick(FPS)
    pg.display.flip()
    m1.fly_right()
    m2.fly_left()
    m3.fly_left()
    d.walk(w)
    d.update(w)
    m.walk(w)
    m.update(w, l)
    s.walk(w)
    s.update(w)
    hp.udpate(w)
    mp.udpate(w)
    p1.go(-160, 450)
    p2.go(1360, 450)
    w.move()
    w.update(m)
    w.update(d)
    w.update(s)
    w.jump()
    w.attack()
    i.inter()
    # w.magic_attack()

pg.quit()
