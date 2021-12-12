import pygame as pg
import player

if __name__ == "__main__":
    pg.init()
    pg.display.set_caption("WITCHER")
    width = 1600
    height = 900
    x, y = 150, 670
    size = width, height
    screen = pg.display.set_mode(size)

    running = True
    FPS = 60
    clock = pg.time.Clock()
    anim_count = 0
    bg = pg.image.load("source/background.png")


    def drawPlayer():
        global anim_count
        global x, y
        screen.blit(bg, (0, 0))
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            x += player.SPEED
            right = True
            player.last_dir = True
            left = False
        elif keys[pg.K_a]:
            x -= player.SPEED
            left = True
            player.last_dir = False
            right = False
        else:
            right = False
            left = False
            anim_count = 0
        if anim_count >= 9:
            anim_count = 0
        if right:
            screen.blit(player.walk_right[anim_count // 3], (x, y))
            anim_count += 1
            pg.draw.rect(screen, (255, 255, 255), (x, y, 300, 300), 1)
        elif left:
            screen.blit(player.walk_left[anim_count // 3], (x, y))
            anim_count += 1
            pg.draw.rect(screen, (255, 255, 255), (x, y, 300, 300), 1)
        else:
            if player.last_dir:
                screen.blit(player.stay_right, (x, y))
                pg.draw.rect(screen, (255, 255, 255), (x, y, 300, 300), 1)
            else:
                screen.blit(player.stay_left, (x, y))
                pg.draw.rect(screen, (255, 255, 255), (x, y, 300, 300), 1)

        pg.display.update()


    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        drawPlayer()
        clock.tick(FPS)
        pg.display.flip()
    pg.quit()
