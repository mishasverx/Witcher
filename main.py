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
    left = False
    right = False
    anim_count = 0
    bg = pg.image.load("source/background.png")


    def drawPlayer():
        global anim_count
        screen.blit(bg, (0, 0))
        if anim_count + 1 >= 10:
            anim_count = 0
        if right:
            screen.blit(player.walk[anim_count // 3], (x, y))
            anim_count += 1
        if left:
            pass
        pg.display.update()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            keys = pg.key.get_pressed()
            if keys[pg.K_d] and x > 5:
                x += player.SPEED / FPS
                right = True
                left = False
            elif keys[pg.K_a] and player.x < 500:
                player.x -= player.SPEED / FPS
                left = True
                right = False
            else:
                right = False
                left = False
                anim_count = 0
        drawPlayer()
        clock.tick(FPS)
        pg.display.flip()
    pg.quit()
