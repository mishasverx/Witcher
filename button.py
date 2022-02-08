import pygame as pg

class Button():
    def __init__(self, image1, image2, pos):
        self.image1 = image1
        self.image2 = image2
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.image = self.image2
            return True
        return False
