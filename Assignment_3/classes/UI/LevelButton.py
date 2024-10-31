import pygame
import math


class LevelButton:
    def __init__(self, x, y, ratio, color, font, text):
        self.text = text
        self.width = 150 / ratio
        self.height = 150 / ratio
        self.x = x
        self.y = y
        self.font = math.ceil(font / ratio)
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.isHover = False
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.set_alpha(0)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def drawButton(self, screen):
        screen.blit(self.image, self.rect.topleft)
        border_color = (128, 128, 128)
        pygame.draw.rect(screen, border_color, self.rect, 5)
        button_font = pygame.font.Font("fonts/font.ttf", self.font)
        text_surf = button_font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(
            center=(
                self.rect.x + self.rect.width // 2,
                self.rect.y + self.rect.height // 2,
            )
        )

        screen.blit(text_surf, text_rect)

    def drawHoverButton(self, screen):

        screen.blit(self.image, self.rect.topleft)
        border_color = (255, 255, 255)
        pygame.draw.rect(screen, border_color, self.rect, 5)
        button_font = pygame.font.Font("fonts/font.ttf", self.font)
        text_surf = button_font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(
            center=(
                self.rect.x + self.rect.width // 2,
                self.rect.y + self.rect.height // 2,
            )
        )

        screen.blit(text_surf, text_rect)