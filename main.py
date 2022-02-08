import pygame as pg
import os
import sys
from math import floor
from random import choice
from camera import *
from images import *
from mobs import *
from obj import *
from witcher import Witcher
from gui import *
from map import *
from button import  Button

pg.init()
pg.display.set_caption("WITCHER")
width, height = 1600, 900
size = width, height
screen = pg.display.set_mode(size)
# ---------------------------------
witcher_sprites = pg.sprite.Group()  # группа спрайтов ведьмака
fire_group = pg.sprite.Group()
int_group = pg.sprite.Group()
hp_group = pg.sprite.Group()
mp_gpoup = pg.sprite.Group()
mobs_sprites = pg.sprite.Group()
map_sprites = pg.sprite.Group()
# ---------------------------------
jump = False
FPS = 60
x_player, y_player = 0, 500
clock = pg.time.Clock()
# -------------------------------d
mouse_s = pg.sprite.Group()
mouse = pg.sprite.Sprite()
mouse.image = load_image("source/arrow.png")
mouse.rect = mouse.image.get_rect()
mouse_s.add(mouse)
# pg.mouse.set_visible(False)

buttons = {
    "start": [load_image("source/GUI/menu/s1.png"), load_image("source/GUI/menu/s2.png")],
    "options": [load_image("source/GUI/menu/o1.png"), load_image("source/GUI/menu/o2.png")],
    "quit": [load_image("source/GUI/menu/q1.png"), load_image("source/GUI/menu/q2.png")],
}
def menu():
    fon = load_image("source/GUI/menu/menu1.png")
    screen.blit(fon, (0, 0))
    while True:
        MENU_MOUSE_POS = pg.mouse.get_pos()
        start = Button(buttons["start"][0], buttons["start"][1], (120, 420))
        options = Button(buttons["options"][0], buttons["options"][1], (120, 530))
        quit_ = Button(buttons["quit"][0], buttons["quit"][1], (120, 640))
        start.update(screen)
        options.update(screen)
        quit_.update(screen)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONUP:
                if start.checkForInput(MENU_MOUSE_POS):
                    play()
                if options.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    sys.exit()
                if quit_.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    sys.exit()
        pg.display.update()
def play():
    running = True
    i = Int(int_group)
    hp = HP(hp_group)
    mp = MP(mp_gpoup)
    w = Witcher(500, 500, witcher_sprites, mobs_sprites)
    m = Mage(-1000, 500, 5, mobs_sprites)
    d = Drowner(2500, 500, 7, mobs_sprites)
    s = Skeleton(1900, 500, 3, mobs_sprites)
    l = Light(1000000, -20, True, mobs_sprites)
    m1 = Mouse(230, 230, 0, 350, 7, mobs_sprites)
    camera = Camera()
    maps = Map(0, map_sprites)
    while running:
        camera.update(w)
        for sprite in mobs_sprites:
            camera.apply(sprite)
        for sprite in map_sprites:
            camera.apply(sprite)
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
                    f = Fire(w.rect.x, w.rect.y, w.last_dir, fire_group, mobs_sprites)
                    fireballs.append(f)

        map_sprites.draw(screen)
        mobs_sprites.draw(screen)
        witcher_sprites.draw(screen)
        int_group.draw(screen)
        hp_group.draw(screen)
        fire_group.draw(screen)
        mp_gpoup.draw(screen)
        if pg.mouse.get_focused():
            mouse_s.draw(screen)
        clock.tick(FPS)
        pg.display.flip()
        m1.fly_right()
        d.walk(w)
        d.update(w)
        m.walk(w)
        m.update(w, l)
        s.walk(w)
        s.update(w)
        hp.udpate(w)
        mp.udpate(w)
        w.abilities()
        w.update(m)
        w.update(d)
        w.update(s)
        i.inter()
        for elem in fireballs:
            elem.move()

    pg.quit()

menu()