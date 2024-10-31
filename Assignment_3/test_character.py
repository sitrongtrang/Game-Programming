import pygame
from classes.Player import Player
from classes.Enemy import Enemy
from classes.CollisionManager import CollisionManager
from classes.Items.BaseItem import BaseItem


def main():
    pygame.init()

    # Set up display
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("My Game")

    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    # Initialize player and add to all_sprites
    player = Player(all_sprites, 100, 300, 50, 50)

    # Initialize enemy, add to both enemies and all_sprites
    enemy = Enemy(all_sprites, 500, 300, 50, 50)
    enemies.add(enemy)

    # Initialize Collision Manager
    collision_manager = CollisionManager(player, enemies)

    platform_width, platform_height = 100, 20
    platforms = [
        pygame.Rect(200, screen_height - 150, platform_width, platform_height),
        pygame.Rect(500, screen_height - 300, platform_width, platform_height)
    ]

    item = BaseItem(500, 550, 50, 50)

    # Game loop
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle collisions
        collision_manager.update()

        # Update all sprites at once
        all_sprites.update()

        # Draw everything at once
        screen.fill((30, 30, 30))
        all_sprites.draw(screen)
        pygame.display.flip()

        for platform in platforms:
            pygame.draw.rect(screen, (0, 255, 0), platform)

        item.draw(screen)

        # Control the frame rate
        clock.tick(60)

    # Quit Pygame
    pygame.quit()


# Run the game
if __name__ == "__main__":
    main()
