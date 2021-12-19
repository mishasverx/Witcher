import pygame as pg
import pygame.sprite
import os
import sys
import main

last_dir = True
SPEED = 15
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

class Withcer(pg.sprite.Sprite):
    walk_right = [pg.image.load("source/player/right/2.png"), pg.image.load("source/player/right/3.png"),
                  pg.image.load("source/player/right/2.png"), pg.image.load("source/player/right/1.png")]
    walk_left = [pg.image.load("source/player/left/2.png"), pg.image.load("source/player/left/3.png"),
                 pg.image.load("source/player/left/2.png"), pg.image.load("source/player/left/1.png")]
    stay_right = pg.image.load("source/player/stand/right.png")
    stay_left = pg.image.load("source/player/stand/left.png")
    right_hit = [pg.image.load("source/player/right_hit/1.png"), pg.image.load("source/player/right_hit/2.png"),
                 pg.image.load("source/player/right_hit/3.png"), pg.image.load("source/player/right_hit/4.png"),
                 pg.image.load("source/player/right_hit/5.png")]
    left_hit = [pg.image.load("source/player/left_hit/1.png"), pg.image.load("source/player/left_hit/2.png"),
                pg.image.load("source/player/left_hit/3.png"), pg.image.load("source/player/left_hit/4.png"),
                pg.image.load("source/player/left_hit/5.png")]
    stand_left = [pg.image.load("source/player/stand_left/1.png"), pg.image.load("source/player/stand_left/2.png"),
                  pg.image.load("source/player/stand_left/3.png"), pg.image.load("source/player/stand_left/4.png"),
                  pg.image.load("source/player/stand_left/5.png")]

    def __init__(self):
        super().__init__(all_sprites)
        self.anim_count = 0
        self.anim_count2 = 0
        self.anim_count3 = 0
        self.right, self.left = False, False
        self.last_dir = True
        self.x, self.y = 0, 0
        self.keys = pg.key.get_pressed()
        self.image = ""

    def moving(self):
        if self.keys[pg.K_d]:
            self.x += SPEED
            self.right = True
            self.last_dir = True
            self.left = False
        elif self.keys[pg.K_a]:
            self.x -= SPEED
            self.right = True
            self.last_dir = True
            self.left = False
        else:
            self.right = False
            self.left = False
            if last_dir:
                self.image =