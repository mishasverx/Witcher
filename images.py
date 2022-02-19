import os
import sys
import pygame as pg


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

    return image


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
witcher_images_m = {
    "walk_right": [load_image("source/player_m/right/2.png"), load_image("source/player_m/right/3.png"),
                   load_image("source/player_m/right/2.png"), load_image("source/player_m/right/1.png")],
    "stand_right": [load_image("source/player_m/stand_right/1.png"), load_image("source/player_m/stand_right/2.png"),
                    load_image("source/player_m/stand_right/3.png"), load_image("source/player_m/stand_right/4.png"),
                    load_image("source/player_m/stand_right/5.png")],
    "right_hit": [load_image("source/player_m/right_hit/1.png"), load_image("source/player_m/right_hit/2.png"),
                  load_image("source/player_m/right_hit/3.png"), load_image("source/player_m/right_hit/4.png"),
                  load_image("source/player_m/right_hit/5.png")],
    "left_hit": [load_image("source/player_m/left_hit/1.png"), load_image("source/player_m/left_hit/2.png"),
                 load_image("source/player_m/left_hit/3.png"), load_image("source/player_m/left_hit/4.png"),
                 load_image("source/player_m/left_hit/5.png")],
    "run": [load_image("source/player_m/run/1.png"), load_image("source/player_m/run/2.png"),
            load_image("source/player_m/run/3.png"), load_image("source/player_m/run/4.png")],
    "jump": [load_image("source/player_m/jump/1.png"), load_image("source/player_m/jump/2.png"),
             load_image("source/player_m/jump/3.png"), load_image("source/player_m/jump/4.png"),
             load_image("source/player_m/jump/5.png")],
    "cast": [load_image("source/player_m/cast/1.png"), load_image("source/player_m/cast/2.png"),
             load_image("source/player_m/cast/3.png"), load_image("source/player_m/cast/3.png")],
    "fire": [load_image("source/player_m/magic/fire/1.png"), load_image("source/player_m/magic/fire/2.png"),
             load_image("source/player_m/magic/fire/3.png"), load_image("source/player_m/magic/fire/4.png"),
             load_image("source/player_m/magic/fire/5.png"), load_image("source/player_m/magic/fire/6.png"),
             load_image("source/player_m/magic/fire/7.png"), load_image("source/player_m/magic/fire/8.png"),
             load_image("source/player_m/magic/fire/9.png"), load_image("source/player_m/magic/fire/10.png")]}

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
                       load_image("source/mobs/mage/hit_mage/7.png"), load_image("source/mobs/mage/hit_mage/8.png")],
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
                 load_image("source/obj/portal_b/8.png"), load_image("source/obj/portal_b/9.png")],
    "portal_o": [load_image("source/obj/portal_o/1.png"), load_image("source/obj/portal_o/2.png"),
                 load_image("source/obj/portal_o/3.png"),
                 load_image("source/obj/portal_o/4.png"), load_image("source/obj/portal_o/5.png"),
                 load_image("source/obj/portal_o/6.png"), load_image("source/obj/portal_o/7.png"),
                 load_image("source/obj/portal_o/8.png"), load_image("source/obj/portal_o/9.png")]
}

effects_images = {
    'hp': [load_image("source/effects/hp/1.png"), load_image("source/effects/hp/2.png"),
           load_image("source/effects/hp/3.png")]
}

pages = {
    0: [load_image("source/GUI/tutorial/1/1.png"), load_image("source/GUI/tutorial/1/2.png"),
        load_image("source/GUI/tutorial/1/3.png"), load_image("source/GUI/tutorial/1/4.png")],
    1: [load_image("source/GUI/tutorial/2/1.png"), load_image("source/GUI/tutorial/2/2.png"),
        load_image("source/GUI/tutorial/2/3.png"), load_image("source/GUI/tutorial/2/4.png")],
    2: [load_image("source/GUI/tutorial/3/1.png"), load_image("source/GUI/tutorial/3/2.png"),
        load_image("source/GUI/tutorial/3/3.png"), load_image("source/GUI/tutorial/3/4.png"),
        load_image("source/GUI/tutorial/3/5.png"), load_image("source/GUI/tutorial/3/6.png")],
    3: [load_image("source/GUI/tutorial/4/1.png"), load_image("source/GUI/tutorial/4/2.png"),
        load_image("source/GUI/tutorial/4/3.png"), load_image("source/GUI/tutorial/4/4.png"),
        load_image("source/GUI/tutorial/4/5.png"), load_image("source/GUI/tutorial/4/6.png"),
        load_image("source/GUI/tutorial/4/7.png"), load_image("source/GUI/tutorial/4/8.png"),
        load_image("source/GUI/tutorial/4/9.png"), load_image("source/GUI/tutorial/4/10.png"),
        load_image("source/GUI/tutorial/4/11.png"), load_image("source/GUI/tutorial/4/12.png"),
        load_image("source/GUI/tutorial/4/13.png")]
}