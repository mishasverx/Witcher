import pygame as pg
import main

walk_right = [pg.image.load("source/player/right/1.png"), pg.image.load("source/player/right/2.png"),
              pg.image.load("source/player/right/3.png")]
walk_left = [pg.image.load("source/player/left/1.png"), pg.image.load("source/player/left/2.png"),
             pg.image.load("source/player/left/3.png")]
stay_right = pg.image.load("source/player/stand/right.png")
stay_left = pg.image.load("source/player/stand/left.png")
last_dir = True
SPEED = 10
width = 300
height = 300
