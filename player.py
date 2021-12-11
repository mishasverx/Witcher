import pygame as pg

if __name__ == "__main__":
    pg.init()
    pg.display.set_caption("WITCHER")
    size = width, height = 1600, 800
    screen = pg.display.set_mode(size)

    running = True
    FPS = 60
    x, y = width // 2, height // 2
    clock = pg.time.Clock()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        clock.tick(FPS)
        pg.display.flip()
    pg.quit()
