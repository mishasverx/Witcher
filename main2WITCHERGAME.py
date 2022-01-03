import pygame as pg
import os
import sys

import player

pg.init()
pg.display.set_caption("WITCHER")
width, height = 1600, 900
size = width, height
screen = pg.display.set_mode(size)
# ---------------------------------
all_sprites = pg.sprite.Group()  # группа всех спрайтов
witcher_sprites = pg.sprite.Group()  # группа спрайтов ведьмака
tile_group = pg.sprite.Group()  # группа спрайтов объектов
# ---------------------------------
running = True
FPS = 60
speed = 10
x_player, y_player = 100, 100
clock = pg.time.Clock()
# -------------------------------
floor_width, floor_height = 80, 50  # размеры пола
plat_width, plat_height = 80, 50  # размеры платформ


# -------------------------------


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


# 🡫🡫🡫🡫🡫🡫🡫🡫 изображения объектов
tile_images = {
    'floor': load_image('source\\tile\\floour1.jpg'),
    'plat': load_image('source\\tile\\plat.jpg')
}
# 🡩🡩🡩🡩🡩🡩🡩🡩 изображения объектов

# 🡫🡫🡫🡫🡫🡫🡫🡫 изображения ведьмака
witcher_images = {
    "walk_right": [load_image("source/player/right/2.png"), load_image("source/player/right/3.png"),
                   load_image("source/player/right/2.png"), load_image("source/player/right/1.png")],
    "walk_left": [load_image("source/player/left/2.png"), load_image("source/player/left/3.png"),
                  load_image("source/player/left/2.png"), load_image("source/player/left/1.png")],
    "stand_right": [load_image("source/player/stand_right/1.png"), load_image("source/player/stand_right/2.png"),
                    load_image("source/player/stand_right/3.png"), load_image("source/player/stand_right/4.png"),
                    load_image("source/player/stand_right/5.png")],
    "stand_left": [load_image("source/player/stand_left/1.png"), load_image("source/player/stand_left/2.png"),
                   load_image("source/player/stand_left/3.png"), load_image("source/player/stand_left/4.png"),
                   load_image("source/player/stand_left/5.png")]
}

# 🡩🡩🡩🡩🡩🡩🡩🡩 изображения ведьмака


def move(hero):
    keys = pg.key.get_pressed()
    if keys[pg.K_d]:
        hero.rect.x += speed
    if keys[pg.K_a]:
        hero.rect.x -= speed


class Witcher(pg.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__(witcher_sprites, all_sprites)
        self.image = pg.image.load("source/player/stand_right/1.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.pos = x, y
        # ------------------
        self.count_walk = 0  # cчетчик анимации ходьбы
        self.count_stand = 0  # cчетчик анимации стойки
        # ------------------



class Tile(pg.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__(tile_group, all_sprites)
        self.image = tile_images[type]
        if type == "floor":
            self.rect = self.image.get_rect().move(
                floor_width * x, floor_height * y)
        elif type == "plat":
            self.rect = self.image.get_rect().move(
                plat_width * x, plat_height * y)


def generate_level(level):
    x, y, count = None, None, 0
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '@':
                Tile('floor', x, y)
            elif level[y][x] == "#":
                Tile('plat', x, y)
    return x, y


def load_level(filename):
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: list(x.ljust(max_width, '.')), level_map))


level = load_level('map_1.txt')
level_x, level_y = generate_level(level)


class Map:
    def __init__(self, bg, count):
        x, y = 0, 0
        backg = pg.image.load(bg)
        a = backg.get_size()
        for i in range(count):
            screen.blit(backg, (x, y))
            x += a[0]

backg = backg = pg.image.load("source/background.png")
map_ = Map("source/background.png", 2)
w = Witcher("stand_left", x_player, y_player)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        keys = pg.key.get_pressed()
        move(w)
        screen.blit(backg, (0, 0))
        # all_sprites.draw(screen)
        tile_group.draw(screen)
        witcher_sprites.draw(screen)
        clock.tick(FPS)
        pg.display.flip()
pg.quit()
