import pygame as pg


class Witcher(pg.sprite.Sprite):
    def __init__(self, x, y, g1, g2, type):
        super().__init__(g1, g2)
        self.type = type
        self.image = self.type["right_hit"][0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.mask = pg.mask.from_surface(self.image)
        # ------------------
        self.count_walk_right = 0
        self.count_stand = 0
        self.count_walk_left = 0
        self.count_hit = 0
        self.count_hit_2 = 0
        self.count_run_right = 0
        self.count_hit_strong_1 = 0
        self.count_hit_strong_2 = 0
        self.count_run_left = 0
        self.count_cast_1 = 0
        self.count_cast_2 = 0
        self.jump_count = 20
        self.anim_jump_count = 0
        self.count_click = 7
        # ------------------
        self.last_dir = True
        self.stay = False
        self.hp = 16
        self.go_right = False
        self.go_left = False
        self.is_jump = False
        self.is_hit = False
        self.fire = False
        self.is_cast = False
        self.fx = 1000
        self.s = 10
        self.is_strong_hit = False
        self.run = False
        self.can_attack = False

        self.magic = False
        self.magic_count = 0

    def update(self, *args):
        for t in args:
            if self.is_hit and self.last_dir and t.rect.x > self.rect.x:
                if pg.sprite.collide_mask(self, t):
                    t.hp -= 0.25
            if self.is_hit and not self.last_dir and t.rect.x < self.rect.x:
                if pg.sprite.collide_mask(self, t):
                    t.hp -= 0.25
            if self.is_strong_hit and self.last_dir and t.rect.x > self.rect.x:
                if pg.sprite.collide_mask(self, t):
                    t.hp -= 0.5
            if self.is_strong_hit and not self.last_dir and t.rect.x < self.rect.x:
                if pg.sprite.collide_mask(self, t):
                    t.hp -= 0.5

    def abilities(self):
        keys = pg.key.get_pressed()
        keys_1 = pg.mouse.get_pressed()
        mods = pg.key.get_mods()

        # Счётчики ходьбы

        if self.count_walk_right >= 36:
            self.count_walk_right = 0
        if self.count_walk_left >= 36:
            self.count_walk_left = 0
        if self.count_stand >= 75:
            self.count_stand = 0
        if self.rect.y > 500:
            self.rect.y = 500
        if self.count_run_right >= 32:
            self.count_run_right = 0
            self.can_attack = False
        if self.count_run_left >= 32:
            self.count_run_left = 0
            self.can_attack = False

        # Счётчики атаки

        if self.count_hit >= 30:
            self.count_hit = 0
            self.is_hit = False
            self.can_attack = False
        if self.count_cast_1 >= 24:
            self.count_cast_1 = 0
            self.is_cast = False
        if self.count_cast_2 >= 24:
            self.count_cast_2 = 0
            self.is_cast = False
        if self.count_hit_2 >= 30:
            self.count_hit_2 = 0
            self.is_hit = False
            self.can_attack = False
        if self.count_hit_strong_1 >= 30:
            self.count_hit_strong_1 = 0
            self.is_strong_hit = False
            self.can_attack = False
        if self.count_hit_strong_2 >= 30:
            self.is_strong_hit = False
            self.count_hit_strong_2 = 0
            self.can_attack = False

        # Проверка взаимодействия с клавиатурой

        if keys[pg.K_d]:
            self.rect.x += self.s
            self.go_right = True
            self.go_left = False
            self.run = False
            self.stay = False
            self.last_dir = True
        elif keys[pg.K_a]:
            self.rect.x -= self.s
            self.go_right = False
            self.go_left = True
            self.run = False
            self.stay = False
            self.last_dir = False
        if not self.go_left and not self.go_right and not self.is_jump and not self.run:
            self.go_right = False
            self.go_left = False
            self.run = False
            self.stay = True
            self.count_walk_left = 0
            self.count_walk_right = 0

        if self.go_right:
            self.image = self.type["walk_right"][self.count_walk_right // 9]
            self.mask = pg.mask.from_surface(self.image)
            self.count_walk_right += 1
        elif self.go_left:
            self.image = pg.transform.flip(self.type["walk_right"][self.count_walk_left // 9], True, False)
            self.mask = pg.mask.from_surface(self.image)
            self.count_walk_left += 1

        if self.stay:
            if self.last_dir:
                self.image = self.type["stand_right"][self.count_stand // 15]
                self.mask = pg.mask.from_surface(self.image)

                self.count_stand += 1
            else:
                self.image = pg.transform.flip(self.type["stand_right"][self.count_stand // 15], True, False)
                self.mask = pg.mask.from_surface(self.image)
                self.count_stand += 1

        # !!!ПРЫЖОК!!! #
        if keys[pg.K_SPACE]:
            self.is_jump = True
            self.stay = False

        if self.is_jump:
            self.run = False
            if self.jump_count >= -20:
                self.rect.y -= self.jump_count
                self.jump_count -= 1
                self.anim_jump_count += 1
                if self.last_dir:
                    self.image = self.type["jump"][self.anim_jump_count // 9]
                else:
                    self.image = pg.transform.flip(self.type["jump"][self.anim_jump_count // 9], True, False)
            else:
                self.jump_count = 20
                self.anim_jump_count = 0
                self.is_jump = False
                self.stay = True

        # !!!АТАКА!!! #
        if self.count_hit >= 30:
            self.count_hit = 0
            self.is_hit = False
            self.can_attack = False
        if self.count_cast_1 >= 24:
            self.count_cast_1 = 0
            self.is_cast = False
        if self.count_cast_2 >= 24:
            self.count_cast_2 = 0
            self.is_cast = False
        if self.count_hit_2 >= 30:
            self.count_hit_2 = 0
            self.is_hit = False
            self.can_attack = False
        if self.count_hit_strong_1 >= 30:
            self.count_hit_strong_1 = 0
            self.is_strong_hit = False
            self.can_attack = False
        if self.count_hit_strong_2 >= 30:
            self.is_strong_hit = False
            self.count_hit_strong_2 = 0
            self.can_attack = False

        if keys_1[0]:
            self.is_hit = True
        if self.is_hit:
            if self.stay:
                self.can_attack = True
                if self.last_dir:
                    self.image = self.type["right_hit"][self.count_hit // 6]
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_hit += 1
                else:
                    self.image = pg.transform.flip(self.type["right_hit"][self.count_hit // 6], True, False)
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_hit += 1
            else:
                self.is_hit = False
        if keys_1[0] and mods & pg.KMOD_LSHIFT:
            self.is_strong_hit = True
        if self.is_strong_hit:
            if self.stay:
                self.can_attack = True
                if self.last_dir:
                    self.image = self.type["left_hit"][self.count_hit_strong_1 // 6]
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_hit_strong_1 += 1
                else:
                    self.image = pg.transform.flip(self.type["left_hit"][self.count_hit_strong_2 // 6], True,
                                                   False)
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_hit_strong_2 += 1
            else:
                self.is_strong_hit = False

        if keys_1[2]:
            self.is_cast = True
            self.count_click -= 0.2
            if self.count_click <= 1:
                self.count_click = 7
        if self.is_cast:
            if self.stay:
                if self.last_dir:
                    self.image = self.type["cast"][self.count_cast_1 // 6]
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_cast_1 += 1
                else:
                    self.image = pg.transform.flip(self.type["cast"][self.count_cast_2 // 6], True, False)
                    self.mask = pg.mask.from_surface(self.image)
                    self.count_cast_2 += 1
        self.go_left = False
        self.go_right = False
        # БЕГ
        if mods & pg.KMOD_LSHIFT and keys[pg.K_d]:
            self.rect.x += 3
            self.run = True
            self.go_right = False
            self.go_left = False
            self.stay = False
            self.last_dir = True
        elif mods & pg.KMOD_LSHIFT and keys[pg.K_a]:
            self.rect.x -= 3
            self.go_right = False
            self.go_left = False
            self.run = True
            self.stay = False
            self.last_dir = False

        if self.run:
            if self.last_dir:
                self.image = self.type["run"][self.count_run_right // 8]
                self.mask = pg.mask.from_surface(self.image)
                self.count_run_right += 1
            else:
                self.image = pg.transform.flip(self.type["run"][self.count_run_left // 8], True, False)
                self.mask = pg.mask.from_surface(self.image)
                self.count_run_left += 1

        self.run = False
