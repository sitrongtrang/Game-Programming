import pygame
import random
from classes.MapSpawner import MapSpawner
import os
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
mapSpawner = MapSpawner(screen, 1)
mapSpawner.spawnMap(0)

while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                character_speed_y = jump_speed
                is_jumping = True

    mapSpawner.renderMap()



    pygame.display.flip()
    clock.tick(60)

pygame.quit()
