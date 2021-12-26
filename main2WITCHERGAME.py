import pygame as pg
import os
import sys


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


pg.init()
pg.display.set_caption("WITCHER")
width = 1600
height = 900
size = width, height
screen = pg.display.set_mode(size)
tile_group = pg.sprite.Group()
tile_images = {
    'floor': load_image('source\\tile\\floour1.jpg')
    # 'empty': load_image('grass.png')
}
floor_width, floor_height = 80, 50
running = True
FPS = 60
clock = pg.time.Clock()


class Tile:
    def __init__(self, type, x, y):
        self.image = tile_images[type]
        self.rect = self.image.get_rect().move(
            floor_width + x, floor_height + y)


def load_level(filename):
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: list(x.ljust(max_width, '.')), level_map))


def generate_level(level):
    x, y = 80, 50
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '@':
                Tile('floor', x, y)
    return x, y


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


map_ = Map("source/background.png", 2)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        clock.tick(FPS)
        pg.display.flip()
pg.quit()
