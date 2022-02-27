import random

from button import Button
from camera import Camera
from gui import *
from images import *
from map import *
from mobs import *
from obj import *
from witcher import Witcher

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
music2 = pg.mixer.Sound('source/GUI/music/game_music.mp3')
music2.set_volume(0.2)
buttons = {
    "start": [load_image("source/GUI/menu/s1.png"), load_image("source/GUI/menu/s2.png")],
    "options": [load_image("source/GUI/menu/o1.png"), load_image("source/GUI/menu/o2.png")],
    "quit": [load_image("source/GUI/menu/q1.png"), load_image("source/GUI/menu/q2.png")],
}
names_mobs = ['mage', 'drowner', 'skeleton']
mobs = []
mobs_dir = [-1, 1]
can_spawn_mob = True
last_score = 0
with open("score.txt", "r") as f:
    for i in f:
        record = i
with open("last_result.txt", "r") as f:
    for j in f:
        last_score = j

def spawn_mobs(sprite_group, hero):
    global can_spawn_mob
    if can_spawn_mob:
        can_spawn_mob = False
        mob = random.choice(names_mobs)
        mob_dir = random.choice(mobs_dir)
        if mob == 'mage':
            m = Mage(hero.rect.x + mob_dir * 1000, 500, 5, sprite_group)
            mobs.append(m)
        elif mob == 'drowner':
            d = Drowner(hero.rect.x + mob_dir * 1000, 500, 7, sprite_group)
            mobs.append(d)
        elif mob == 'skeleton':
            s = Skeleton(hero.rect.x + mob_dir * 1000, 500, 3, sprite_group)
            mobs.append(s)


def menu_options():
    music.stop()
    page_sprites = pg.sprite.Group()
    fon = load_image("source/GUI/options/options.png")
    book = load_image("source/GUI/options/book.png")
    page1 = Page(page_sprites, 300, 0)
    page2 = Page(page_sprites, 800, 1)
    button = Button(load_image("source/GUI/options/X.png"), load_image("source/GUI/options/X.png"), (30, 20))
    button1 = Button(load_image("source/GUI/options/button1.png"), load_image("source/GUI/options/button1.png"),
                     (360, 690))
    button2 = Button(load_image("source/GUI/options/button2.png"), load_image("source/GUI/options/button2.png"),
                     (1140, 690))
    running = True
    s1, s2 = 0, 1
    while running:
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
                    running = False
                if button2.checkForInput(mouse_pos):
                    page1.kill(), page2.kill()
                    s1 += 2
                    s2 += 2
                    if s1 > 4:
                        s1 = 4
                    if s2 > 5:
                        s2 = 5
                    page1, page2 = Page(page_sprites, 300, s1), Page(page_sprites, 800, s2)
                if button1.checkForInput(mouse_pos):
                    page1.kill(), page2.kill()
                    s1 -= 2
                    s2 -= 2
                    if s1 < 0:
                        s1 = 0
                    if s2 < 1:
                        s2 = 1
                    page1, page2 = Page(page_sprites, 300, s1), Page(page_sprites, 800, s2)
        clock.tick(FPS)
        pg.display.flip()
        screen.blit(fon, (0, 0))
        screen.blit(book, (300, 100))
        page_sprites.draw(screen)
        page1.update()
        page2.update()
        button.update(screen)
        button1.update(screen)
        button2.update(screen)
        if pg.mouse.get_focused():
            mouse_s.draw(screen)


def menu():
    global last_score
    music2.stop()
    music.play(-1)
    fon = load_image("source/GUI/menu/menu1.png")
    running = True
    font = pg.font.Font('super_font.ttf', 70)
    text1 = font.render(f'Ваш рекорд: {record}', True, (255, 255, 255))
    text2 = font.render(f'Последний результат: {last_score}', True, (255, 255, 255))
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
        screen.blit(text1, (725, 400))
        screen.blit(text2, (725, 470))
        start.update(screen)
        options.update(screen)
        quit_.update(screen)
        if pg.mouse.get_focused():
            mouse_s.draw(screen)


def play():
    global can_spawn_mob
    global record
    global last_score
    score = 0
    font = pg.font.Font('super_font.ttf', 60)
    music2.play()
    witcher_sprites = pg.sprite.Group()  # группа спрайтов ведьмака
    fire_group = pg.sprite.Group()
    active_sprites = pg.sprite.Group()
    gui_group = pg.sprite.Group()
    map_sprites = pg.sprite.Group()
    potion_group = pg.sprite.Group()
    score_l = [0, 0]
    running = True
    i = Int(gui_group)
    hp = HP(gui_group)
    mp = MP(gui_group)
    w = Witcher(1600, 500, witcher_sprites, active_sprites, witcher_images_sword)
    # m1 = Mouse(230, 230, 0, 350, 7, active_sprites)
    php = Potion(potion_group, "potion_hp")
    pmp = Potion(potion_group, "potion_mp")
    camera = Camera()
    maps = Map(0, map_sprites, w)
    while running:
        print(w.mp)
        if mobs == []:
            can_spawn_mob = True
        spawn_mobs(active_sprites, w)
        camera.update(w)
        pg.event.set_allowed([pg.QUIT, pg.MOUSEBUTTONDOWN, pg.MOUSEMOTION, pg.MOUSEBUTTONUP])
        for sprite in active_sprites:
            camera.apply(sprite, maps, w)
        for sprite in map_sprites:
            camera.apply(sprite, maps, w)
        for sprite in potion_group:
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
                if w.stay and not w.is_cast:
                    f = Fire(w.rect.x, w.rect.y, w.last_dir, active_sprites)
                    fireballs.append(f)

        if w.hp <= 0.5:
            running = False
            can_spawn_mob = True
            mobs.clear()
            if score > int(record):
                with open("score.txt", "w") as f:
                    record = score
                    score_l[0] = record
                    f.write(str(score_l[0]))
            with open("last_result.txt", "w") as f:
                last_score = score
                score_l[1] = last_score
                f.write(str(score_l[1]))
            score = 0
            menu()

        screen.fill((0, 0, 0))
        map_sprites.draw(screen)
        gui_group.draw(screen)
        witcher_sprites.draw(screen)
        active_sprites.draw(screen)
        potion_group.draw(screen)
        fire_group.draw(screen)
        if pg.mouse.get_focused():
            mouse_s.draw(screen)
        clock.tick(FPS)
        text1 = font.render(f'Текущий счет: {score}', True, (255, 255, 255))
        screen.blit(text1, (900, 70))
        pg.display.flip()
        # m1.fly()
        for elem in mobs:
            elem.walk(w)
            elem.update(w)
            w.update(elem)
            for el in fireballs:
                el.move(elem)
            if elem.hp <= 0:
                if elem.is_mage:
                    for el in lightnings:
                        lightnings.remove(el)
                        el.g.remove(el)
                        del el
                mobs.remove(elem)
                active_sprites.remove(elem)
                del elem
                score += 1
        php.update(w)
        pmp.update(w)
        hp.udpate(w)
        mp.udpate(w)
        w.abilities()
        i.inter()
    pg.quit()


menu()
