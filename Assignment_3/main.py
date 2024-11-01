import pygame
import random
from classes.Items.DmgItem import DmgItem
from classes.Characters.Player import Player
from classes.Characters.Enemy import Enemy
from classes.CollisionManager import CollisionManager

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Platformer")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Initialize player and add to all_sprites
player = Player(all_sprites, 100, 550, 50, 50)
enemy = Enemy(all_sprites, 500, 550, 50, 50)
enemies.add(enemy)

# Platform settings
platform_width, platform_height = 100, 20
platforms = [
    pygame.Rect(200, SCREEN_HEIGHT - 150, platform_width, platform_height),
    pygame.Rect(350, SCREEN_HEIGHT - 300, platform_width, platform_height)
]

item = DmgItem(400, 550, 50, 50)
items = [item]

# Initialize Collision Manager
collision_manager = CollisionManager(player, enemies, platforms, items)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    collision_manager.update()

    all_sprites.update()
    all_sprites.draw(screen)


    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)
        if platform.right < 0:
            platform.x = SCREEN_WIDTH
            platform.y = random.randint(200, SCREEN_HEIGHT - 50)

    for item in items:
        item.update(screen, items)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
