import pygame
import math


class PauseButton:
    def __init__(self, x, y, ratio, color, font, text):
        self.text = text
        self.width = 250 / ratio
        self.height = 50 / ratio
        self.x = x
        self.y = y
        self.font = math.ceil(font / ratio)
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.isHover = False
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def drawButton(self, screen):
        self.image.fill(self.color)
        self.image.set_alpha(0)
        screen.blit(self.image, self.rect.topleft)
        # pygame.draw.rect(screen, self.color, self.rect)
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
        self.image.fill([self.color[0] + 50, self.color[1] + 50, self.color[2] + 50])
        self.image.set_alpha(64)
        screen.blit(self.image, self.rect.topleft)
        button_font = pygame.font.Font("fonts/font.ttf", self.font)
        text_surf = button_font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(
            center=(
                self.rect.x + self.rect.width // 2,
                self.rect.y + self.rect.height // 2,
            )
        )

        screen.blit(text_surf, text_rect)
