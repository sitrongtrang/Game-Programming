from classes.Player import Player
from classes.Character import Character
import pygame


def main():
    pygame.init()

    # Set up display
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("My Game")

    all_sprites = pygame.sprite.Group()
    player = Player(all_sprites, 100, 300, 50, 50)

    # Example enemy (You would create an Enemy class similarly to Player)
    enemy = Character(all_sprites, 500, 300, 50, 50)  # Just a placeholder enemy for now

    # Game loop
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update sprites
        all_sprites.update()

        # Draw everything
        screen.fill((30, 30, 30))
        all_sprites.draw(screen)

        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)

    # Quit Pygame
    pygame.quit()


# Run the game
if __name__ == "__main__":
    main()