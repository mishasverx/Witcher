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
from button import Button

pg.init()
pg.display.set_caption("WITCHER")
width, height = 1600, 900
size = width, height
screen = pg.display.set_mode(size, pg.DOUBLEBUF)
FPS = 60
clock = pg.time.Clock()
# -------------------------------d
mouse_s = pg.sprite.Group()
mouse = pg.sprite.Sprite()
mouse.image = load_image("source/arrow.png")
mouse.rect = mouse.image.get_rect()
mouse_s.add(mouse)
pg.mouse.set_visible(False)
music = pg.mixer.Sound('source/GUI/music/menu_music.mp3')
music.set_volume(0.2)
buttons = {
    "start": [load_image("source/GUI/menu/s1.png"), load_image("source/GUI/menu/s2.png")],
    "options": [load_image("source/GUI/menu/o1.png"), load_image("source/GUI/menu/o2.png")],
    "quit": [load_image("source/GUI/menu/q1.png"), load_image("source/GUI/menu/q2.png")],
}

def menu_options():
    music.stop()
    page_sprites = pg.sprite.Group()
    fon = load_image("source/GUI/options/options.png")
    book = load_image("source/GUI/options/book.png")
    page = Page(page_sprites, 300, 0)
    button = Button(load_image("source/GUI/options/X.png"), load_image("source/GUI/options/X.png"), (20, 20))
    while True:
        mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEMOTION:
                mouse.rect.topleft = event.pos
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse.image = load_image("source/arrow2.png")
            elif event.type == pg.MOUSEBUTTONUP:
                mouse.image = load_image("source/arrow.png")
                if button.checkForInput(mouse_pos):
                    menu()
        clock.tick(FPS)
        pg.display.flip()
        screen.blit(fon, (0, 0))
        screen.blit(book, (300, 100))
        page_sprites.draw(screen)
        page.update()
        button.update(screen)
        if pg.mouse.get_focused():
            mouse_s.draw(screen)

def menu():
    music.play(-1)
    fon = load_image("source/GUI/menu/menu1.png")
    running = True
    while running:
        mouse_pos = pg.mouse.get_pos()
        start = Button(buttons["start"][0], buttons["start"][1], (120, 420))
        options = Button(buttons["options"][0], buttons["options"][1], (120, 530))
        quit_ = Button(buttons["quit"][0], buttons["quit"][1], (120, 640))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONUP:
                if start.checkForInput(mouse_pos):
                    pg.mixer.stop()
                    play()
                    running = False
                if options.checkForInput(mouse_pos):
                    menu_options()
                if quit_.checkForInput(mouse_pos):
                    pg.quit()
                    sys.exit()
            if event.type == pg.MOUSEMOTION:
                mouse.rect.topleft = event.pos
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse.image = load_image("source/arrow2.png")
            elif event.type == pg.MOUSEBUTTONUP:
                mouse.image = load_image("source/arrow.png")

        clock.tick(FPS)
        pg.display.flip()
        screen.blit(fon, (0, 0))
        start.update(screen)
        options.update(screen)
        quit_.update(screen)
        if pg.mouse.get_focused():
            mouse_s.draw(screen)




def play():
    witcher_sprites = pg.sprite.Group()  # группа спрайтов ведьмака
    fire_group = pg.sprite.Group()
    mobs_sprites = pg.sprite.Group()
    gui_group = pg.sprite.Group()
    map_sprites = pg.sprite.Group()
    running = True
    i = Int(gui_group)
    hp = HP(gui_group)
    mp = MP(gui_group)
    w = Witcher(3200, 500, witcher_sprites, mobs_sprites, witcher_images_m)
    m = Mage(-1000, 500, 5, mobs_sprites)
    d = Drowner(2500, 500, 7, mobs_sprites)
    s = Skeleton(1900, 500, 3, mobs_sprites)
    l = Light(1000000, -20, True, mobs_sprites)
    m1 = Mouse(230, 230, 0, 350, 7, mobs_sprites)
    camera = Camera()
    maps = Map(0, map_sprites, w)
    while running:
        camera.update(w)
        pg.event.set_allowed([pg.QUIT, pg.MOUSEBUTTONDOWN, pg.MOUSEMOTION, pg.MOUSEBUTTONUP])
        for sprite in mobs_sprites:
            camera.apply(sprite, maps, w)
        for sprite in map_sprites:
            camera.apply(sprite, maps, w)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEMOTION:
                mouse.rect.topleft = event.pos
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse.image = load_image("source/arrow2.png")
            elif event.type == pg.MOUSEBUTTONUP:
                mouse.image = load_image("source/arrow.png")
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                if w.stay:
                    f = Fire(w.rect.x, w.rect.y, w.last_dir, mobs_sprites)
                    fireballs.append(f)
        if w.hp <= 0.5:
            menu()
        screen.fill((0, 0, 0))
        map_sprites.draw(screen)
        mobs_sprites.draw(screen)
        gui_group.draw(screen)
        witcher_sprites.draw(screen)
        fire_group.draw(screen)
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
