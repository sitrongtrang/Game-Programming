from classes.Player import Player
import pygame

pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Create a main sprite group to include all sprites
all_sprites = pygame.sprite.Group()
player = Player(all_sprites,100, 300, 50, 50)


# Game loop example
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprites
    all_sprites.update()

    # Draw everything
    screen.fill((30, 30, 30))

    # Draw all sprites (including player and bullets)
    all_sprites.draw(screen)

    # Draw bullets explicitly if needed (not necessary if bullets are in all_sprites)
    # player.bullets.draw(screen)  # You can keep this line if you want to draw separately

    pygame.display.flip()

# Quit Pygame
pygame.quit()
