import pygame as pg
import os
import sys

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
x_player, y_player = 100, 500
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
    "stand_right": [load_image("source/player/stand_right/1.png"), load_image("source/player/stand_right/2.png"),
                    load_image("source/player/stand_right/3.png"), load_image("source/player/stand_right/4.png"),
                    load_image("source/player/stand_right/5.png")],
    "right_hit": [load_image("source/player/right_hit/1.png"), load_image("source/player/right_hit/2.png"),
                  load_image("source/player/right_hit/3.png"), load_image("source/player/right_hit/4.png"),
                  load_image("source/player/right_hit/5.png")],
    "left_hit": [load_image("source/player/left_hit/1.png"), load_image("source/player/left_hit/2.png"),
                 load_image("source/player/left_hit/3.png"), load_image("source/player/left_hit/4.png"),
                 load_image("source/player/left_hit/5.png")]
}


# 🡩🡩🡩🡩🡩🡩🡩🡩 изображения ведьмака
class Wall(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = tile_images["plat"]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.mask = pg.mask.from_surface(self.image)


t = Wall(1000, 700)
t1 = Wall(500, 700)


class Witcher(pg.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__(witcher_sprites)
        self.image = witcher_images["right_hit"][0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.mask = pg.mask.from_surface(self.image)
        self.a = self.mask.count()
        # ------------------
        self.count_walk_right = 0  # cчетчик анимации ходьбы
        self.count_stand = 0  # cчетчик анимации стойки
        self.count_walk_left = 0
        self.count_hit = 0
        self.count_hit_2 = 0
        # ------------------
        self.last_dir = True

    def update(self):
        if pg.sprite.collide_mask(self, t):
            self.rect.x -= 10

    def update2(self):
        if pg.sprite.collide_mask(self, t1):
            self.rect.x += 10

def move(hero):
    keys = pg.key.get_pressed()
    last_dir = True
    right = False
    left = False
    if hero.count_walk_right >= 36:
        hero.count_walk_right = 0
    if hero.count_walk_left >= 36:
        hero.count_walk_left = 0
    if hero.count_stand >= 45:
        hero.count_stand = 0
    if keys[pg.K_d]:
        hero.rect.x += speed
        right = True
        left = False
        hero.stay = False
        hero.last_dir = True
    elif keys[pg.K_a]:
        right = False
        left = True
        hero.stay = False
        hero.rect.x -= speed
        hero.last_dir = False
    else:
        right = False
        left = False
        hero.stay = True
        hero.count_walk_left = 0
        hero.count_walk_right = 0
    if right:
        witcher_sprites.draw(screen)
        hero.image = witcher_images["walk_right"][hero.count_walk_right // 9]
        hero.mask = pg.mask.from_surface(hero.image)

        hero.count_walk_right += 1
    elif left:
        witcher_sprites.draw(screen)
        hero.image = pg.transform.flip(witcher_images["walk_right"][hero.count_walk_left // 9], True, False)
        hero.mask = pg.mask.from_surface(hero.image)

        hero.count_walk_left += 1
    else:
        if hero.last_dir:
            witcher_sprites.draw(screen)
            hero.image = witcher_images["stand_right"][hero.count_stand // 9]
            hero.mask = pg.mask.from_surface(hero.image)

            hero.count_stand += 1
        else:
            witcher_sprites.draw(screen)
            hero.image = pg.transform.flip(witcher_images["stand_right"][hero.count_stand // 9], True, False)
            hero.mask = pg.mask.from_surface(hero.image)
            hero.count_stand += 1


def attack(hero):
    # for event in pg.event.get():
    #     if event.type == pg.QUIT:
    #         pg.quit()
    #     if event.type == pg.MOUSEBUTTONDOWN:
    #         if event.button == 1:
    #             if hero.stay:
    #                 if hero.last_dir:
    #                     for i in range(45):
    #                         witcher_sprites.draw(screen)
    #                         hero.image = pg.transform.scale(witcher_images["right_hit"][i // 9], [400, 300])
    #                 else:
    #                     for i in range(45):
    #                         witcher_sprites.draw(screen)
    #                         hero.image = pg.transform.flip(pg.transform.scale(witcher_images["right_hit"][i // 9],
    #                                                               [400, 300]), True, False)

    keys = pg.mouse.get_pressed()
    keys_1 = pg.key.get_pressed()
    if hero.count_hit >= 30:
        hero.count_hit = 0
    if hero.count_hit_2 >= 30:
        hero.count_hit_2 = 0
    if keys[0]:
        if hero.stay:
            if hero.last_dir:
                witcher_sprites.draw(screen)
                hero.image = witcher_images["right_hit"][hero.count_hit // 6]
                hero.mask = pg.mask.from_surface(hero.image)
                hero.count_hit += 1
            else:
                witcher_sprites.draw(screen)
                hero.image = pg.transform.flip(witcher_images["right_hit"][hero.count_hit // 6], True, False)
                hero.mask = pg.mask.from_surface(hero.image)
                hero.count_hit += 1
    if keys[0] and keys_1[pg.K_LSHIFT]:
        if hero.stay:
            if hero.last_dir:
                witcher_sprites.draw(screen)
                hero.image = witcher_images["left_hit"][hero.count_hit_2 // 6]
                hero.mask = pg.mask.from_surface(hero.image)
                hero.count_hit_2 += 1
            else:
                witcher_sprites.draw(screen)
                hero.image = pg.transform.flip(witcher_images["left_hit"][hero.count_hit_2 // 6], True, False)
                hero.mask = pg.mask.from_surface(hero.image)
                hero.count_hit_2 += 1


class Tile(pg.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__(tile_group, all_sprites)
        self.image = tile_images[type]
        self.mask = pg.mask.from_surface(self.image)
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


backg = pg.image.load("source/background_2.png")
map_ = Map("source/background_2.png", 2)
w = Witcher("stand_left", x_player, y_player)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.blit(backg, (0, 0))
    all_sprites.draw(screen)
    tile_group.draw(screen)
    witcher_sprites.draw(screen)
    clock.tick(FPS)
    pg.display.flip()
    move(w)
    w.update()
    w.update2()
    attack(w)
pg.quit()
