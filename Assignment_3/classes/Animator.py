import pygame
import Animation

         

class Animator:
    def __init__(self, surface):
        self.animations = {"none" : None}
        self.current_anim = "none"
        self.lastTick = 0
        self.surface = surface
    
    def add_animation(self, name, spriteFile, frameSize,  frameNum, frameInterval):
        new_anim = Animation(self.surface, name, spriteFile, frameSize,  frameNum, frameInterval)
        self.animations[name] = new_anim
    
    def change_anim(self, anim):
        self.current_anim = anim

    def update(self):
        # get deltatime
        t = pygame.time.get_ticks()
        deltaTime = (t - self.lastTick()) / 1000.0
        self.lastTick = t

        #
        self.animations[self.current_anim].update(deltaTime)