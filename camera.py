class Camera:
    def __init__(self):
        self.dx = 0

    def apply(self, obj, map, w):
        obj.rect.x += self.dx
        if map.rect.x >= 0:
            map.rect.x = -1
        if map.rect.x == -1:
            obj.rect.x += obj.rect.x
        if map.rect.x <= -4800:
            map.rect.x = -4799
        if map.rect.x == -4799:
            obj.rect.x -= obj.rect.x

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - 1600 // 2)