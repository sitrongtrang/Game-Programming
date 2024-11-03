import pygame
import random
from classes.GameManager import GameManager
from data import constant

# Initialize Pygame
pygame.init()

# Screen settings

screen = pygame.display.set_mode((constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
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
