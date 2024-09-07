import pygame
from random import randint
from os import walk
from os.path import join

class Zombie:
    def __init__(self, x, y, width, height, sprite_image) -> None:
        self.load_img()
        self.state, self.frame_index = 'spawn' , 0

        self.appear_time = pygame.time.get_ticks()
        self.stay_time = randint(3000, 5000)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.sprite = pygame.transform.scale(sprite_image, (self.width, self.height))
        
        self.deathStart = 0
        self.deathDur = 600
        self.spawnStart = 0
        self.spawnDur = 300

    def draw(self, screen):
        # pygame.draw.rect(screen, green, (self.x, self.y, self.width, self.height))
        self.animate(0.1)

        screen.blit(self.sprite, (self.x, self.y))

    def is_smashed(self, pos):
        if self.state == 'death': return False

        return pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(pos)
    
    def load_img(self):
        self.frames = {'spawn' : [], 'idle' : [], 'death' : []}
        
        for state in self.frames.keys():
            for folder_path, sub_folders, file_names in walk(join('sprites', 'Zombie', state)):
                if file_names:
                    for file_name in sorted(file_names, key= lambda name: int(name.split('.')[0])):
                        full_path = join(folder_path, file_name)
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(surf)
        
    def animate(self, dt):
        # get state

        # animate
        self.frame_index += 0.5 * dt
        new_sprite = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]
        self.sprite = pygame.transform.scale(new_sprite, (self.width, self.height))

    def update(self, zomList):
        if self.state == 'spawn':
            now = pygame.time.get_ticks()
            if (now - self.spawnStart) > self.spawnDur:
                self.state = 'idle'
                self.frame_index = 0          
        elif self.state == 'death':
            now = pygame.time.get_ticks()
            if (now - self.deathStart) > self.deathDur:
                zomList.remove(self)
        

    def death(self):
        if self.state != 'death':
            self.deathStart = pygame.time.get_ticks()
            self.state = 'death'
            self.frame_index = 0
           
    def spawn(self):
        self.spawnStart = pygame.time.get_ticks()
        
        

    