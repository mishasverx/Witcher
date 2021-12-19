import pygame as pg
import pygame.sprite

import main

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
stand_left = [pg.image.load("source/player/stand_left/1.png"]
last_dir = True
SPEED = 15

class Withcer(pg.sprite.Sprite):
