import pygame
import sys
from random import randint

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Zombie Game")

white = (255, 255, 255)
green = (0, 255, 0)

zombie_sprite = pygame.image.load('zombie.png')

# background_sprite = pygame.image.load('background.png')
# background_sprite = pygame.transform.scale(background_sprite, (screen_width, screen_height))


class Zombie:
    def __init__(self, x, y, width, height, sprite_image) -> None:
        self.appear_time = pygame.time.get_ticks()
        self.stay_time = randint(3000, 5000)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.sprite = pygame.transform.scale(sprite_image, (self.width, self.height))

    def draw(self, screen):
        # pygame.draw.rect(screen, green, (self.x, self.y, self.width, self.height))
        screen.blit(self.sprite, (self.x, self.y))

    def is_smashed(self, pos):
        return pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(pos)

zombies = []
last_spawn = 0

def add_zombie():
    zombie = Zombie(randint(0, screen_width - 50), randint(0, screen_height - 50), 50, 50, zombie_sprite)
    zombies.append(zombie)

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for zombie in zombies[:]:
                if zombie.is_smashed(event.pos):
                    zombies.remove(zombie)

    screen.fill(white)

    current_time = pygame.time.get_ticks()

    zombies = [zombie for zombie in zombies if current_time - zombie.appear_time < zombie.stay_time]

    for zombie in zombies:
        zombie.draw(screen)

    if current_time - last_spawn >= 1000:
        spawn = randint(0, 1)
        if spawn:
            last_spawn = pygame.time.get_ticks()
            add_zombie()

    pygame.display.flip()

pygame.quit()
sys.exit()
