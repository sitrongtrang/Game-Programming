import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 100
PLAYER_SPEED = 5

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scrolling Background with Player and Platforms")

# Load background images
backgrounds = ["images/menu_background_image.png", "images/menu_background_image.png"]  # Replace with actual file paths
bg_images = [pygame.image.load(bg).convert() for bg in backgrounds]

# Calculate the total width of all background images combined
total_bg_width = len(bg_images) * SCREEN_WIDTH

# Player setup
player = pygame.Rect(0, SCREEN_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
player_color = (255, 0, 0)  # Red color for the player

# Platform setup
platform_width = 100
platform_height = 20
platform_color = (0, 255, 0)  # Green color for platforms
platforms = []

# Generate random platforms
for i in range(5):
    platform_x = random.randint(0, total_bg_width - platform_width)
    platform_y = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT - platform_height)
    platforms.append(pygame.Rect(platform_x, platform_y, platform_width, platform_height))

# Camera position
camera_x = 0

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_d]:
        player.x += PLAYER_SPEED

    # Clamp player position to screen bounds
    player.x = max(0, min(player.x, total_bg_width - PLAYER_WIDTH))

    # Update camera to follow player, centered on the screen
    camera_x = max(0, min(player.x - SCREEN_WIDTH // 2, total_bg_width - SCREEN_WIDTH))

    # Draw background images in sequence
    for i, bg_image in enumerate(bg_images):
        bg_x = i * SCREEN_WIDTH
        screen.blit(bg_image, (bg_x - camera_x, 0))

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, platform_color, (platform.x - camera_x, platform.y, platform.width, platform.height))

    # Draw player
    pygame.draw.rect(screen, player_color, (player.x - camera_x, player.y, PLAYER_WIDTH, PLAYER_HEIGHT))

    # Update display
    pygame.display.flip()
    clock.tick(60)