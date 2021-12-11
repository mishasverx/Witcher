import pygame as pg
import main

walk_right = [pg.image.load("source/player/right/1.png"), pg.image.load("source/player/right/2.png"),
              pg.image.load("source/player/right/3.png")]
walk_left = [pg.image.load("source/player/left/1.png"), pg.image.load("source/player/left/2.png"),
             pg.image.load("source/player/left/3.png")]
stay = pg.image.load("source/player/stand/3.png")
SPEED = 15
width = 300
height = 300
x, y = 0, 0
