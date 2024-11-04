
import pygame

class Animation:
    def __init__(self, surface, name, spriteFile, frameSize,  frameNum, frameInterval):
        self.name = name
        self.surface = surface
        self.spriteFile = spriteFile
        self.frameSize = frameSize
        self.frameNum = frameNum
        self.frameInterval = frameInterval

        self.sheet = None
        self.load_spritesheet()
        self.resetStat()

    def resetStat(self):
        self.frame = 0
        self.frameTimer = self.frameInterval

    def load_spritesheet(self):
        try:
            self.sheet = pygame.image.load(self.spriteFile).convert_alpha()
        except pygame.error:
            print("Unable to load spritesheet image:", self.spriteFile)
            raise SystemExit
        

    def run(self, surface):
        pass

    def draw(self):
        area = pygame.Rect(self.frame * self.frameSize[0] , 0, self.frameSize[0], self.frameSize[1])
        # self.surface.blit(self.sprite, (0, 0), area)
        print(area)

    def update(self, deltaTime):

        if self.frameTimer > 0:
            self.frameTimer -= deltaTime
        else:
            self.frame = (self.frame +1) % self.frameNum
            self.frameTimer = self.frameInterval
            self.draw()