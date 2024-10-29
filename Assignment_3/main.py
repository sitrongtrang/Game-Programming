import pygame
import random

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

# Character settings
CHARACTER_WIDTH, CHARACTER_HEIGHT = 50, 50
character_x, character_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - CHARACTER_HEIGHT - 100
character_speed_x, character_speed_y = 0, 0
jump_speed = -15
gravity = 1
is_jumping = False

# Platform settings
platform_width, platform_height = 100, 20
platforms = [
    pygame.Rect(200, SCREEN_HEIGHT - 150, platform_width, platform_height),
    pygame.Rect(500, SCREEN_HEIGHT - 300, platform_width, platform_height)
]
platform_speed = 2

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                character_speed_y = jump_speed
                is_jumping = True

    # Character movement
    character_speed_y += gravity
    character_y += character_speed_y

    # Ground check
    if character_y + CHARACTER_HEIGHT > SCREEN_HEIGHT:
        character_y = SCREEN_HEIGHT - CHARACTER_HEIGHT
        character_speed_y = 0
        is_jumping = False

    # Platform collision
    character_rect = pygame.Rect(character_x, character_y, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    for platform in platforms:
        if character_rect.colliderect(platform) and character_speed_y > 0:
            character_y = platform.y - CHARACTER_HEIGHT
            character_speed_y = 0
            is_jumping = False

    # Draw character
    pygame.draw.rect(screen, BLUE, character_rect)

    # Draw platforms and move them
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)
        if platform.right < 0:  # Reset platform when it moves off screen
            platform.x = SCREEN_WIDTH
            platform.y = random.randint(200, SCREEN_HEIGHT - 50)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
