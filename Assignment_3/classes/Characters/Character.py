import pygame
from data import constant

class Character(pygame.sprite.Sprite):
    def __init__(self,all_sprites, x, y, width, height, hp, dmg, speed, gravity=1):
        super().__init__()

        all_sprites.add(self)
        self.all_sprites = all_sprites

        self.hp = hp
        self.base_hp = hp
        self.dmg = dmg
        self.base_dmg = dmg
        self.bullet = constant.BULLET_LIMIT
        # Placeholder sprite
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 255))  # Blue color for placeholder

        # Rect attributes
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Movement attributes
        self.speed = speed
        self.base_speed = speed
        self.jump_power = constant.JUMP_POWER
        self.gravity = gravity
        self.vel_y = 0
        self.is_jumping = False

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

    def jump(self):
        if not self.is_jumping:
            self.vel_y = -self.jump_power
            self.is_jumping = True

    def apply_gravity(self):
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # Ground collision
        if self.rect.y >= constant.GROUND_LEVEL:
            self.rect.y = constant.GROUND_LEVEL
            self.is_jumping = False
            self.vel_y = 0

    def update(self):
        self.apply_gravity()

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.kill()

    def setDmg(self, dmg):
        # limit maximum damage to base damage * increase coefficient from item
        self.dmg = min(dmg, self.base_dmg * constant.DMG_INCREASE_COEFF) 

    def setHP(self, hp):
        self.hp = min(hp, self.base_hp)

    def setSpeed(self, speed):
        self.speed = min(speed, self.base_speed * constant.SPEED_INCREASE_COEFF)

    def setBullet(self, bullet):
        self.bullet = min(bullet, constant.BULLET_LIMIT)