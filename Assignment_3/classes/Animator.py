import pygame
from classes.Animation import Animation

class Animator:
    def __init__(self, surface):
        self.animations = {"none" : None}
        self.current_anim = "none"
        self.lastTick = 0
        self.surface = surface


    
    def add_animation(self, name, spriteFile, frameSize, frameNum, frameInterval, spacing = 0, loop = True):
        new_anim = Animation(self.surface, name, spriteFile, frameSize,  frameNum, frameInterval, spacing, loop)
        self.animations[name] = new_anim   
    
    def change_anim(self, anim):
        if self.current_anim != "none" and self.animations[self.current_anim].is_runing():
            return

        if  anim not in self.animations:
            print(f"Warning: Animation '{anim}' not found.")
            return
        
        # Change anim
        if self.current_anim != "none" and self.current_anim != anim:
            self.animations[self.current_anim].resetStat()
     
        self.current_anim = anim
        self.animations[self.current_anim].draw()
        

    def update(self):
        # get deltatime
        t = pygame.time.get_ticks()
        deltaTime = (t - self.lastTick) / 1000.0
        self.lastTick = t

        #
        if self.current_anim != "none":
            self.animations[self.current_anim].update(deltaTime)

    