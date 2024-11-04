import pygame
from data import constant
from classes.Spritesheet import Spritesheet


class Character(pygame.sprite.Sprite):
    def __init__(self, all_sprites, x, y, width, height, hp, dmg, speed, gravity=1):
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
        self.vel_x = 0  # Horizontal velocity
        self.vel_y = 0  # Vertical velocity
        self.is_jumping = False
        self.hp_bar = Spritesheet("images/hp_bar.png")

    def move_left(self):
        self.vel_x = -self.speed

    def move_right(self):
        self.vel_x = self.speed

    def stop(self):
        self.vel_x = 0  # Stop horizontal movement

    def jump(self):
        if not self.is_jumping:
            self.vel_y = -self.jump_power
            self.is_jumping = True

    def apply_gravity(self):
        self.vel_y += self.gravity

    def update(self, camera_x=0):
        # Apply horizontal and vertical velocities to the character's position
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Apply gravity effect
        self.apply_gravity()

        # Ground collision
        if self.rect.y >= constant.GROUND_LEVEL:
            self.rect.y = constant.GROUND_LEVEL
            self.is_jumping = False
            self.vel_y = 0

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

    def draw(self, screen, camera_x=0):
        screen.blit(
            self.image,
            (self.rect.x - camera_x, self.rect.y, self.rect.width, self.rect.height),
        )

    def drawHpBar(self, screen, x, y):
        if self.hp / self.base_hp >= 1:
            hp_bar_image = self.hp_bar.image_at(1, 0, 3.5)
            # resize image to 1/2
            hp_bar_image = pygame.transform.scale(
                hp_bar_image,
                (int(hp_bar_image.get_width() / 2), int(hp_bar_image.get_height() / 2)),
            )
            screen.blit(hp_bar_image, (x, y))
        elif self.hp / self.base_hp >= 0.8:
            hp_bar_image = self.hp_bar.image_at(2, 0, 3.5)
            hp_bar_image = pygame.transform.scale(
                hp_bar_image,
                (int(hp_bar_image.get_width() / 2), int(hp_bar_image.get_height() / 2)),
            )
            screen.blit(hp_bar_image, (x, y))
        elif self.hp / self.base_hp >= 0.6:
            hp_bar_image = self.hp_bar.image_at(3, 0, 3.5)
            hp_bar_image = pygame.transform.scale(
                hp_bar_image,
                (int(hp_bar_image.get_width() / 2), int(hp_bar_image.get_height() / 2)),
            )
            screen.blit(hp_bar_image, (x, y))
        elif self.hp / self.base_hp >= 0.4:
            hp_bar_image = self.hp_bar.image_at(4, 0, 3.5)
            hp_bar_image = pygame.transform.scale(
                hp_bar_image,
                (int(hp_bar_image.get_width() / 2), int(hp_bar_image.get_height() / 2)),
            )
            screen.blit(hp_bar_image, (x, y))
        elif self.hp / self.base_hp >= 0.2:
            hp_bar_image = self.hp_bar.image_at(5, 0, 3.5)
            hp_bar_image = pygame.transform.scale(
                hp_bar_image,
                (int(hp_bar_image.get_width() / 2), int(hp_bar_image.get_height() / 2)),
            )
            screen.blit(hp_bar_image, (x, y))
        elif self.hp / self.base_hp > 0:
            hp_bar_image = self.hp_bar.image_at(6, 0, 3.5)
            hp_bar_image = pygame.transform.scale(
                hp_bar_image,
                (int(hp_bar_image.get_width() / 2), int(hp_bar_image.get_height() / 2)),
            )
            screen.blit(hp_bar_image, (x, y))
        else:
            pass
