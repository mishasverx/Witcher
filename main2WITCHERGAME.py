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
width, height = 1600, 900
size = width, height
screen = pg.display.set_mode(size)
all_sprites = pg.sprite.Group()
witcher_sprites = pg.sprite.Group()
tile_group = pg.sprite.Group()
tile_images = {
    'floor': load_image('source\\tile\\floour1.jpg'),
    'plat': load_image('source\\tile\\plat.jpg')
}
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
floor_width, floor_height = 80, 50
plat_width, plat_height = 80, 50
running = True
FPS = 60
x, y = 100, 100
clock = pg.time.Clock()


class Witcher(pg.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__(witcher_sprites, all_sprites)
        self.image = witcher_images[type]
        self.x, self.y = x, y
        self.count = 1

    def move(self, pos):
        if self.count >= 24:
            self.count = 0
        if pos == "right" and self.count > 0:
            self.image = witcher_images["walk_right"][self.count // 6]
            self.count += 1
        elif pos == "left" and self.count > 0:
            self.image = witcher_images["walk_left"][self.count // 6]
            self.count += 1

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


map_ = Map("source/background.png", 2)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # all_sprites.draw(screen)
        tile_group.draw(screen)
        witcher_sprites.draw(screen)
        clock.tick(FPS)
        pg.display.flip()
pg.quit()
