class Camera:
    def __init__(self):
        self.dx = 0

    def apply(self, obj, map, w):
        obj.rect.x += self.dx
        if map.rect.x >= 0:
            map.rect.x = -4800
        if map.rect.x == -4800:
            obj.rect.x += self.dx
        if map.rect.x <= -4800:
            map.rect.x = 0
        if map.rect.x == 0:
            obj.rect.x -= self.dx

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - 1600 // 2)
