
import pygame

class Animation:
    def __init__(self, surface, name, spriteFile, frameSize,  frameNum, frameInterval, spacing = 0, loop = True):
        self.name = name
        self.surface = surface
        self.spriteFile = spriteFile
        self.frameSize = frameSize
        self.frameNum = frameNum
        self.frameInterval = frameInterval
        self.spacing = spacing
        self.loop = loop
    

        self.sheet = None
        self.load_spritesheet()
        self.resetStat()

    def resetStat(self):
        self.frame = 0
        self.frameTimer = self.frameInterval
        self.looped = False

    def load_spritesheet(self):
        try:
            self.sheet = pygame.image.load(self.spriteFile).convert_alpha()
        except pygame.error:
            print("Unable to load spritesheet image:", self.spriteFile)
            raise SystemExit
        

    def run(self, surface):
        pass

    def draw(self):
        area = pygame.Rect(self.frame * self.frameSize[0]  + self.frame * self.spacing, 0, self.frameSize[0], self.frameSize[1])
        self.surface.fill((0, 0, 0, 0))
        self.surface.set_alpha(255)
        self.surface.blit(self.sheet, (0, 0), area)
    #print(area)

    def update(self, deltaTime):
        

        if self.frameTimer > 0:
            self.frameTimer -= deltaTime
        else:
            if not (not self.loop and (self.frame+1 == self.frameNum)):
                self.frame = (self.frame +1) % self.frameNum
            else:
                self.looped = True
     
            self.frameTimer = self.frameInterval
            self.draw()
    
    def is_runing(self):
        isRuning = ((self.loop == False) and (self.looped == False))
       
        return isRuning