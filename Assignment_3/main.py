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

# Initialize Game Manager
game_manager = GameManager(screen)
game_manager.new_game()

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game_manager.update()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
