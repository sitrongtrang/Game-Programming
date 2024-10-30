import pygame
import sys
from classes.MenuButton import MenuButton
from classes.LevelButton import LevelButton
from classes.Spritesheet import Spritesheet
import json

with open("data/stat/character.json") as file:
    settings = json.load(file)


class GameMenu:
    def __init__(self, screen, background_music, start_time):
        self.screen = screen
        self.background_music = background_music
        self.start_time = start_time
        self.hp_bar = Spritesheet("images/hp_bar.png")
        self.coin_image = Spritesheet("images/font.png")
        self.coin = settings["coin"]
        self.level = settings["level"]
        self.currrent_hp = settings["current_hp"]
        self.max_hp = settings["max_hp"]

    ##? change screen menu
    def update(self, pause_time):
        with open("data/stat/character.json") as file:
            settings = json.load(file)
        self.coin = settings["coin"]
        self.level = settings["level"]
        self.current_hp = settings["current_hp"]
        self.drawGameMenu(pause_time)

    ##? draw background elements for all menus
    def drawBackground(self):
        # if self.background_music_is_on:
        # self.background_music.play() ##! cập nhật lại sau
        self.screen.blit(
            pygame.transform.scale(self.background_image, self.screen.get_size()),
            (0, 0),
        )

    ##? draw main menu
    def drawGameMenu(self, pause_time):
        # how to render 2 images on top of each other image at 0,0 0,1
        # self.screen.blit(self.hp_bar.image_at(0, 0, 1), (0, 0))

        self.drawHpBar()
        self.drawHpFrame()
        self.drawCoin()
        self.drawLevel()
        self.drawTime(pause_time)

    def drawHpBar(self):
        # Calculate HP bar width based on current HP
        if self.current_hp / self.max_hp == 1:
            hp_bar_image = self.hp_bar.image_at(1, 0, 3.5)
            self.screen.blit(hp_bar_image, (40, 5))
        elif self.current_hp / self.max_hp >= 0.8:
            hp_bar_image = self.hp_bar.image_at(2, 0, 3.5)
            self.screen.blit(hp_bar_image, (40, 5))
        elif self.current_hp / self.max_hp >= 0.6:
            hp_bar_image = self.hp_bar.image_at(3, 0, 3.5)
            self.screen.blit(hp_bar_image, (40, 5))
        elif self.current_hp / self.max_hp >= 0.4:
            hp_bar_image = self.hp_bar.image_at(4, 0, 3.5)
            self.screen.blit(hp_bar_image, (40, 5))
        elif self.current_hp / self.max_hp >= 0.2:
            hp_bar_image = self.hp_bar.image_at(5, 0, 3.5)
            self.screen.blit(hp_bar_image, (40, 5))
        elif self.current_hp / self.max_hp > 0:
            hp_bar_image = self.hp_bar.image_at(6, 0, 3.5)
            self.screen.blit(hp_bar_image, (40, 5))
        else:
            pass

    def drawHpFrame(self):
        # Draw the HP frame at (0, 0)
        hp_frame_image = self.hp_bar.image_at(0, 0, 3.5)

        hp_frame_image.set_alpha(128)
        self.screen.blit(hp_frame_image, (40, 5))

    def drawCoin(self):
        coin_image = self.coin_image.image_at(0, 2, 3, xTileSize=8, yTileSize=8)
        multiply_image = self.coin_image.image_at(8, 5, 2, xTileSize=8, yTileSize=8)
        self.screen.blit(coin_image, (260, 30))
        self.screen.blit(multiply_image, (280, 39))
        if self.coin < 10:
            self.drawText("0" + str(self.coin), 300, 44, (255, 255, 255))
        else:
            self.drawText(str(self.coin), 300, 44, (255, 255, 255))

    def drawLevel(self):
        self.drawText("Level: ", 425, 25, (255, 255, 255))
        self.drawText(str(self.level), 425, 50, (255, 255, 255))

    def drawTime(self, pause_time):
        time = pygame.time.get_ticks() - self.start_time - pause_time
        if time // 1000 > 999:
            self.start_time = pygame.time.get_ticks()
        self.drawText("Time: ", 650, 25, (255, 255, 255))
        if time // 1000 < 10:
            self.drawText("00" + str(time // 1000), 650, 50, (255, 255, 255))
        elif time // 1000 < 100:
            self.drawText("0" + str(time // 1000), 650, 50, (255, 255, 255))
        else:
            self.drawText(str(time // 1000), 650, 50, (255, 255, 255))

    def drawText(self, text, x, y, color):
        font = pygame.font.Font("fonts/font.ttf", 20)
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(midleft=(x, y))
        self.screen.blit(text_surf, text_rect)
