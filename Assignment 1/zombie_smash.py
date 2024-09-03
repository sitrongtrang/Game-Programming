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

original_zombie_sprite = pygame.image.load('zombie.png')
zombie_width = 100
zombie_height = 100
zombie_sprite = pygame.transform.scale(original_zombie_sprite, (zombie_width, zombie_height))

background_sprite = pygame.image.load('background.png')
background_sprite = pygame.transform.scale(background_sprite, (screen_width, screen_height))

class Pit:
    def __init__(self, start_x, start_y, end_x, end_y, rows=3, cols=3):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.rows = rows
        self.cols = cols
        self.centers = self._calculate_centers()

    def _calculate_centers(self):
        centers = []
        for row in range(self.rows):
            for col in range(self.cols):
                x = self.start_x + col * (self.end_x - self.start_x) // (self.cols - 1)
                y = self.start_y + row * (self.end_y - self.start_y) // (self.rows - 1)
                centers.append((x, y))
        return centers

pits = Pit(140, 193, 665, 511)

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

    centers = pits.centers
    zombie_x, zombie_y = centers[randint(0, len(centers) - 1)]
    zombie = Zombie(zombie_x - zombie_width // 2, zombie_y - zombie_height // 2, zombie_width, zombie_height, zombie_sprite)
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

    screen.blit(background_sprite, (0, 0))

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
