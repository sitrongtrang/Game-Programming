import pygame
import random
from classes.Items.DmgItem import DmgItem
from classes.Characters.Player import Player
from classes.Characters.Enemy import Enemy
from classes.CollisionManager import CollisionManager
from classes.GameManager import GameManager
from classes.Coin import Coin

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Platformer")

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

coin = Coin(370, 270, 20, 20)
coins = [coin]

# Initialize Collision Manager
game_manager = GameManager(screen, player, enemies, platforms, items, coins)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game_manager.update()

    all_sprites.update()
    all_sprites.draw(screen)


    for platform in platforms:
        pygame.draw.rect(screen, (150, 75, 0), platform)
        if platform.right < 0:
            platform.x = SCREEN_WIDTH
            platform.y = random.randint(200, SCREEN_HEIGHT - 50)

    # for item in items:
    #     item.update(screen, items)

    # coin.update(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
