import pygame as pg
import pygame.sprite
import os
import sys

last_dir = True
SPEED = 15
right_walk_sprites = pygame.sprite.Group()
left_walk_sprites = pygame.sprite.Group()
sprite_walk_right = pygame.sprite.Sprite()
sprite_walk_left = pygame.sprite.Sprite()

walk_right = [pg.image.load("source/player/right/2.png"), pg.image.load("source/player/right/3.png"),
                   pg.image.load("source/player/right/2.png"), pg.image.load("source/player/right/1.png")]
walk_left = [pg.image.load("source/player/left/2.png"), pg.image.load("source/player/left/3.png"),
                  pg.image.load("source/player/left/2.png"), pg.image.load("source/player/left/1.png")]
stay_right = pg.image.load("source/player/stand_right/1.png")
stay_left = pg.image.load("source/player/stand_left/1.png")
right_hit = [pg.image.load("source/player/right_hit/1.png"),
                  pg.image.load("source/player/right_hit/2.png"),
                  pg.image.load("source/player/right_hit/3.png"),
                  pg.image.load("source/player/right_hit/4.png"),
                  pg.image.load("source/player/right_hit/5.png")]


class Withcer(pg.sprite.Sprite):

    def __init__(self):
        super().__init__(right_walk_sprites, left_walk_sprites)
        self.walk_right = [pg.image.load("source/player/right/2.png"), pg.image.load("source/player/right/3.png"),
                           pg.image.load("source/player/right/2.png"), pg.image.load("source/player/right/1.png")]
        self.walk_left = [pg.image.load("source/player/left/2.png"), pg.image.load("source/player/left/3.png"),
                          pg.image.load("source/player/left/2.png"), pg.image.load("source/player/left/1.png")]
        self.stay_right = pg.image.load("source/player/stand/right.png")
        self.stay_left = pg.image.load("source/player/stand/left.png")
        self.right_hit = [pg.image.load("source/player/right_hit/1.png"),
                          pg.image.load("source/player/right_hit/2.png"),
                          pg.image.load("source/player/right_hit/3.png"),
                          pg.image.load("source/player/right_hit/4.png"),
                          pg.image.load("source/player/right_hit/5.png")]
        self.left_hit = [pg.image.load("source/player/left_hit/1.png"), pg.image.load("source/player/left_hit/2.png"),
                         pg.image.load("source/player/left_hit/3.png"), pg.image.load("source/player/left_hit/4.png"),
                         pg.image.load("source/player/left_hit/5.png")]
        self.stand_left = [pg.image.load("source/player/stand_left/1.png"),
                           pg.image.load("source/player/stand_left/2.png"),
                           pg.image.load("source/player/stand_left/3.png"),
                           pg.image.load("source/player/stand_left/4.png"),
                           pg.image.load("source/player/stand_left/5.png")]
        self.count_walk = 0
        self.anim_count2 = 0
        self.anim_count3 = 0
        self.right, self.left = False, False
        self.rect = self.image.get_rect()
        self.last_dir = True
        self.x, self.y = self.rect.x, self.rect.y
        self.keys = pg.key.get_pressed()
        if last_dir:
            self.image = self.stay_right
        else:
            self.image = self.stay_left

    def animate(self, pos, direct):
        if self.count_walk >= 24:
            self.count_walk = 0
        if pos == self.right and direct == "walk_right":
            self.image = self.walk_right[self.count_walk // 6]
            self.count_walk += 1
            sprite_walk_right.image = self.image
            right_walk_sprites.add(sprite_walk_right)
            right_walk_sprites.draw(screen)
        elif pos == self.left and direct == "walk_left":
            self.image = self.walk_left[self.count_walk // 6]
            self.count_walk += 1
            sprite_walk_right.image = self.image
            left_walk_sprites.add(sprite_walk_left)
            left_walk_sprites.draw(screen)

    def moving(self):
        if self.keys[pg.K_d]:
            self.x += SPEED
            self.right = True
            self.last_dir = True
            self.left = False
        elif self.keys[pg.K_a]:
            self.x -= SPEED
            self.right = False
            self.last_dir = False
            self.left = True
        else:
            self.right = False
            self.left = False
        if self.right:
            Withcer.animate(self.right, "walk_right")
        if self.left:
            Withcer.animate(self.right, "walk_right")
