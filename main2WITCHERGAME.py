import pygame as pg
import os
import sys

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
                       load_image("source/mobs/mage/hit_mage/13.png"), load_image("source/mobs/mage/hit_mage/14.png")]
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


class Wall(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = tile_images["floor"]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.mask = pg.mask.from_surface(self.image)


class Fire(pg.sprite.Sprite):
    def __init__(self):
        super().__init__(fire_group)
        self.image = witcher_images['fire'][0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.mask = pg.mask.from_surface(self.image)
        self.count = 0

    def hit(self, x, y):
        if self.count >= 100:
            self.count = 0
        self.rect.x, self.rect.y = x, y
        self.image = witcher_images["fire"][self.count // 10]
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

    def hit(self):
        if self.count_hit >= 70:
            self.count_hit = 0
        self.image = mobs_images["mage_hit_light"][self.count_hit // 5]
        self.mask = pg.mask.from_surface(self.image)
        self.count_hit += 1


class Mage(pg.sprite.Sprite):
    def __init__(self, x, y, s):
        super().__init__(mage_group)
        self.image = mobs_images['mage_walk'][0]
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

    def walk(self, hero):
        # right = False
        # left = False
        # right_hit = False
        # last = False
        # left_hit = False
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

        # if self.rect.x < hero.rect.x - 100:
        #     right = True
        #     left = False
        #     last = True
        #     self.rect.x += self.s
        # elif self.rect.x > hero.rect.x + 300:
        #     left = True
        #     right = False
        #     last = False
        #     self.rect.x -= self.s
        # if self.rect.x == hero.rect.x + 300 and not (last):
        #     right_hit = False
        #     left_hit = True
        # if self.rect.x == hero.rect.x - 100:
        #     right_hit = True
        #     left_hit = False
        #
        # if right:
        #     self.image = pg.transform.scale(pg.transform.flip(mobs_images["mage_walk"][self.count_walk_right // 9],
        #                                                       True, False), [315, 355])
        #     self.mask = pg.mask.from_surface(self.image)
        #     self.count_walk_right += 1
        #     self.count_hit_right = 0
        # elif left:
        #     self.image = pg.transform.scale(mobs_images["mage_walk"][self.count_walk_left // 9], [315, 355])
        #     self.mask = pg.mask.from_surface(self.image)
        #     self.count_walk_left += 1
        #     self.count_hit_left = 0
        #
        # if right_hit:
        #     self.image = pg.transform.scale(pg.transform.flip(mobs_images["mage_hit"][self.count_hit_right // 10],
        #                                                       True, False), [315, 355])
        #     self.mask = pg.mask.from_surface(self.image)
        #     self.count_hit_right += 1
        # if left_hit:
        #     self.image = pg.transform.scale(mobs_images["mage_hit"][self.count_hit_left // 10], [315, 355])
        #     self.mask = pg.mask.from_surface(self.image)
        #     self.count_hit_left += 1

        if abs(self.rect.x - hero.rect.x) > 600:
            if self.last_dir:
                self.rect.x += self.s
                self.image = pg.transform.scale(pg.transform.flip(mobs_images["mage_walk"][self.count_walk_right // 9],
                                                                  True, False), [315, 355])
                self.mask = pg.mask.from_surface(self.image)
                self.count_walk_right += 1

            else:
                self.rect.x -= self.s
                self.image = pg.transform.scale(mobs_images["mage_walk"][self.count_walk_left // 9], [315, 355])
                self.mask = pg.mask.from_surface(self.image)
                self.count_walk_left += 1
        else:
            if self.last_dir:
                self.image = pg.transform.scale(pg.transform.flip(mobs_images["mage_hit"][self.count_hit_right // 10],
                                                                  True, False), [315, 355])
                self.mask = pg.mask.from_surface(self.image)
                self.count_hit_right += 1
            else:
                self.mask = pg.mask.from_surface(self.image)
                self.image = pg.transform.scale(mobs_images["mage_hit"][self.count_hit_left // 10], [315, 355])
                self.count_hit_left += 1

    def hp1(self):
        if self.hp <= 0:
            self.rect.x = -1000
            self.hp = 10


class Witcher(pg.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__(witcher_sprites)
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
        self.jump_count = 20
        self.anim_jump_count = 0
        self.can_attack = False

    def update(self, t):
        if self.can_attack:
            if pg.sprite.collide_mask(self, t):
                t.hp -= 0.1

    def move(self):
        keys = pg.key.get_pressed()
        last_dir = True
        right = False
        left = False
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
        # keys = pg.mouse.get_pressed()
        # keys_1 = pg.key.get_pressed()
        # if self.count_hit >= 30:
        #     self.count_hit = 0
        # if self.count_hit_2 >= 30:
        #     self.count_hit_2 = 0
        # if self.count_hit_strong_1 >= 30:
        #     self.count_hit_strong_1 = 0
        # if self.count_hit_strong_2 >= 30:
        #     self.count_hit_strong_2 = 0
        #
        # if keys[0]:
        #     if self.stay:
        #         if self.last_dir:
        #             self.image = witcher_images["right_hit"][self.count_hit // 6]
        #             self.mask = pg.mask.from_surface(self.image)
        #             self.count_hit += 1
        #         else:
        #             self.image = pg.transform.flip(witcher_images["right_hit"][self.count_hit // 6], True, False)
        #             self.mask = pg.mask.from_surface(self.image)
        #             self.count_hit += 1
        # if keys[0] and keys_1[pg.K_LSHIFT]:
        #     if self.stay:
        #         if self.last_dir:
        #             self.image = witcher_images["left_hit"][self.count_hit_strong_1 // 6]
        #             self.mask = pg.mask.from_surface(self.image)
        #             self.count_hit_strong_1 += 1
        #         else:
        #             self.image = pg.transform.flip(witcher_images["left_hit"][self.count_hit_strong_2 // 6], True,
        #                                            False)
        #             self.mask = pg.mask.from_surface(self.image)
        #             self.count_hit_strong_2 += 1
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

        if keys[2]:
            self.is_cast = True
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
            if self.image == witcher_images["cast"][2] or \
                self.image == witcher_images["cast"][3]:
                self.fire = True
            if self.fire:
                f = Fire()
                f.hit(self.fx, 660)
                self.fx -= 10

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
        self.image = gui_images["HP"][9]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 25, 35


class MP(pg.sprite.Sprite):
    def __init__(self):
        super().__init__(mp_gpoup)
        self.image = gui_images["MP"][7]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 25, 35


backg = pg.image.load("source/background_2.png")
# l = Light(100, -20, True)
i = Int()
hp = HP()
mp = MP()
w = Witcher("stand_left", x_player, y_player)
m = Mage(700, 440, 5)
m1 = Mouse(230, 230, 0, 350, 7)
m2 = Mouse(115, 115, 1600 - 115, 500, 15)
m3 = Mouse(300, 300, 1300, 200, 10)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.blit(backg, (0, 0))
    all_sprites.draw(screen)
    tile_group.draw(screen)
    mage_group.draw(screen)
    mouse_group.draw(screen)
    int_group.draw(screen)
    hp_group.draw(screen)
    mp_gpoup.draw(screen)
    fire_group.draw(screen)
    witcher_sprites.draw(screen)
    light_group.draw(screen)
    clock.tick(FPS)
    pg.display.flip()
    # l.hit()
    m1.fly_right()
    m2.fly_left()
    m3.fly_left()
    m.walk(w)
    m.hp1()
    w.move()
    i.inter()
    w.update(m)
    print(m.hp)
    w.jump()
    w.attack()
pg.quit()
