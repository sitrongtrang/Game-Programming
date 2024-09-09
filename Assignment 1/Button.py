import pygame

class Button:
    def __init__(self,x,y, color ,text):
        self.text = text
        self.width = 150
        self.height = 50
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        button_font = pygame.font.Font(None,30)
        text_surf = button_font.render(self.text, True, (255,255,255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)