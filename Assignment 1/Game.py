import pygame
from random import randint
from Pit import Pit
from Zombie import Zombie

class Game:
    def __init__(self, screen_width, screen_height, zombie_width, zombie_height, hit_fx, font):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.zombie_width = zombie_width
        self.zombie_height = zombie_height
        self.zombie_sprite = pygame.transform.scale(pygame.image.load('sprites/zombie.png'), (zombie_width, zombie_height))
        self.background_sprite = pygame.transform.scale(pygame.image.load('sprites/background.png'), (screen_width, screen_height))
        self.hit_fx = hit_fx
        self.font = font
        
        self.running = True
        self.new_game = True
        self.new_game_time = 0
        self.game_over = False
        self.game_over_time = 0
        self.hit = 0
        self.miss = 0
        self.pits = Pit(140, 193, 665, 511)
        self.zombies = []
        self.last_spawn = 0

    def add_zombie(self):
        centers = self.pits.centers
        max_attempts = 10  # Number of attempts to find a valid spawn location
        for _ in range(max_attempts):
            zombie_x, zombie_y = centers[randint(0, len(centers) - 1)]
            new_zombie_rect = pygame.Rect(zombie_x - self.zombie_width // 2, zombie_y - self.zombie_height // 2, 
                                          self.zombie_width, self.zombie_height)
            overlap = any(new_zombie_rect.colliderect(pygame.Rect(z.x, z.y, z.width, z.height)) for z in self.zombies)

            if not overlap:
                zombie = Zombie(zombie_x - self.zombie_width // 2, zombie_y - self.zombie_height // 2, 
                                self.zombie_width, self.zombie_height, self.zombie_sprite)
                self.zombies.append(zombie)
                zombie.spawn()
                break

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for zombie in self.zombies[:]:
                    if zombie.is_smashed(event.pos):
                        # Call zomebie death   
                        zombie.stun()
                        zombie.death()
                        self.hit += 1
                        self.hit_fx.play()
                        break
                else:
                    self.miss += 1

        self.screen.blit(self.background_sprite, (0, 0))


        # Update
        hit_text = self.font.render(f"Hits: {self.hit}", True, (0, 0, 0))
        hit_rect = hit_text.get_rect(topright=(self.screen_width - 10, 10))
        self.screen.blit(hit_text, hit_rect)

        miss_text = self.font.render(f"Misses: {self.miss}", True, (0, 0, 0))
        miss_rect = miss_text.get_rect(topright=(self.screen_width - 10, hit_rect.bottom + 10))
        self.screen.blit(miss_text, miss_rect)

        current_time = pygame.time.get_ticks()

        # Remove zombies that have been stunned for 1 second
        zombies = [zombie for zombie in self.zombies if not zombie.is_stunned_for_duration()]
        zombies = [zombie for zombie in self.zombies if current_time - zombie.appear_time < zombie.stay_time]

        for zombie in self.zombies:
            zombie.update(zombies)

        #Draw
        for zombie in self.zombies:
            zombie.draw(self.screen)

        if current_time - self.last_spawn >= 1000:
            spawn = randint(0, 1)
            if spawn:
                self.last_spawn = pygame.time.get_ticks()
                self.add_zombie()

        pygame.display.flip()

    def resetgame(self):
        self.screen.fill((0, 0, 0))
        self.hit = 0
        self.miss = 0
        self.zombies = []
        self.game_over = True
        self.game_over_time = pygame.time.get_ticks()

    def initgame(self):
        self.hit = 0
        self.miss = 0
        self.zombies = []
        self.last_spawn = pygame.time.get_ticks()
        self.new_game_time = pygame.time.get_ticks()
        self.new_game = False
        self.game_over = False

    def run(self):
        if self.new_game:
            self.initgame()
        if not self.game_over:
            self.loop()
            if pygame.time.get_ticks() - self.new_game_time >= 30000:
                self.resetgame()
        if pygame.time.get_ticks() - self.game_over_time >= 10000:
            self.new_game = True