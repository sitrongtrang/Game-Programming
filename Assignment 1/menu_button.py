import pygame
import math

class Menu_Button:
    def __init__(self,x,y,ratio, color,font ,text):
        self.text = text
        self.width = 250/ratio
        self.height = 75/ratio
        self.x = x
        self.y = y
        self.font = math.ceil(font/ratio)
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        button_font = pygame.font.Font("fonts/font.ttf",self.font)
        text_surf = button_font.render(self.text, True, (255,255,255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)