import pygame as pg
import player

if __name__ == "__main__":
    pg.init()
    pg.display.set_caption("WITCHER")
    width = 1600
    height = 900
    x, y = 150, 600
    size = width, height
    infoObject = pg.display.Info()
    screen = pg.display.set_mode((infoObject.current_w, infoObject.current_h))

    running = True
    right, left, left_hit, right_hit = False, False, False, False
    FPS = 60
    clock = pg.time.Clock()
    clock1 = pg.time.Clock()
    anim_count = 0
    anim_count2 = 0
    bg = pg.image.load("source/background.png")
    bg = pg.transform.scale2x(bg)



    def drawPlayer():
        global anim_count, anim_count2
        global x, y
        global right, left, right_hit, left_hit
        screen.blit(bg, (0, -850))
        keys = pg.key.get_pressed()
        if keys[pg.K_d] and x < 1400 and y > 50:
            x += player.SPEED
            right = True
            player.last_dir = True
            left = False
        elif keys[pg.K_a] and x > 0 and y > 50:
            x -= player.SPEED
            left = True
            player.last_dir = False
            right = False
        else:
            right = False
            left = False
            anim_count = 0

        if anim_count >= 24:
            anim_count = 0

        if right:
            screen.blit(player.walk_right[anim_count // 6], (x, y))
            picx, picy = player.walk_right[anim_count // 6].get_size()
            anim_count += 1
            pg.draw.rect(screen, (255, 255, 255), (x, y, picx, picy), 1)
        elif left:
            screen.blit(player.walk_left[anim_count // 6], (x, y))
            picx, picy = player.walk_left[anim_count // 6].get_size()
            anim_count += 1
            pg.draw.rect(screen, (255, 255, 255), (x, y, picx, picy), 1)
        else:
            if player.last_dir:
                screen.blit(player.stay_right, (x, y))
                picx, picy = player.walk_right[anim_count // 6 - 1].get_size()
                pg.draw.rect(screen, (255, 255, 255), (x, y, picx, picy), 1)
            else:
                screen.blit(player.stay_left, (x, y))
                picx, picy = player.walk_left[anim_count // 6 - 1].get_size()
                pg.draw.rect(screen, (255, 255, 255), (x, y, picx, picy), 1)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        drawPlayer()
        clock.tick(FPS)
        pg.display.flip()
    pg.quit()
