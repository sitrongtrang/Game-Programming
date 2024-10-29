# Game loop example
from classes.Player import Player
import pygame

pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")
player = Player(100, 300, 50, 50)

all_sprites = pygame.sprite.Group(player, player.bullets)

# Game loop example
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:  # Press 'F' to shoot
                player.shoot()

    # Update sprites
    all_sprites.update()

    # Draw everything
    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()



# Quit Pygame
pygame.quit()