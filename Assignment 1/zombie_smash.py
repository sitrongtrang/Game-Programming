import pygame
import sys
from random import randint
from Zombie import Zombie
from Pit import Pit

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Zombie Game")

original_zombie_sprite = pygame.image.load('sprites/zombie.png')
zombie_width = 100
zombie_height = 100
zombie_sprite = pygame.transform.scale(original_zombie_sprite, (zombie_width, zombie_height))

background_sprite = pygame.image.load('sprites/background.png')
background_sprite = pygame.transform.scale(background_sprite, (screen_width, screen_height))

font = pygame.font.Font(None, 36)

# Sound effect and music setup
pygame.mixer.music.load('musics/music.mp3')
pygame.mixer.music.play(-1, 0.0, 5000)
hit_fx = pygame.mixer.Sound('sounds/coin.wav')

def add_zombie():

    centers = pits.centers
    zombie_x, zombie_y = centers[randint(0, len(centers) - 1)]
    zombie = Zombie(zombie_x - zombie_width // 2, zombie_y - zombie_height // 2, zombie_width, zombie_height, zombie_sprite)
    zombies.append(zombie)
    zombie.spawn()

running = True
hit = 0
miss = 0
pits = Pit(140, 193, 665, 511)
zombies = []
last_spawn = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for zombie in zombies[:]:
                if zombie.is_smashed(event.pos):
                    # Call zomebie death   
                    #zombies.remove(zombie)
                    zombie.death()
                    hit += 1
                    hit_fx.play()
                    break
            else:
                miss += 1

    screen.blit(background_sprite, (0, 0))


    # Update
    hit_text = font.render(f"Hits: {hit}", True, (0, 0, 0))
    hit_rect = hit_text.get_rect(topright=(screen_width - 10, 10)) 
    screen.blit(hit_text, hit_rect)

    miss_text = font.render(f"Misses: {miss}", True, (0, 0, 0))
    miss_rect = miss_text.get_rect(topright=(screen_width - 10, hit_rect.bottom + 10)) 
    screen.blit(miss_text, miss_rect)

    current_time = pygame.time.get_ticks()

    zombies = [zombie for zombie in zombies if current_time - zombie.appear_time < zombie.stay_time]

    for zombie in zombies:
        zombie.update(zombies)

    #Draw
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
