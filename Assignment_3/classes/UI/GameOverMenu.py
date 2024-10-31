import pygame
import sys
from classes.UI.PauseButton import PauseButton
from classes.UI.LevelButton import LevelButton
import json

with open("data/stat/character.json") as file:
    character = json.load(file)


class GameOverMenu:
    def __init__(self, screen, start_time, player_win):
        self.screen = screen
        self.start_time = start_time
        self.player_win = player_win
        self.restart_button = PauseButton(25, 400, 1, (0, 0, 0), 24, "RESTART")
        self.choose_level_button = PauseButton(275, 400, 1, (0, 0, 0), 24, "NEW LEVEL")
        self.main_menu_button = PauseButton(525, 400, 1, (0, 0, 0), 24, "MENU")
        self.level_one_button = LevelButton(100, 150, 1, (0, 0, 0), 24, "1 - 1")
        self.level_two_button = LevelButton(325, 150, 1, (0, 0, 0), 24, "1 - 2")
        self.back_button = LevelButton(550, 150, 1, (0, 0, 0), 24, "BACK")
        self.is_choosing_level = False
        self.state = 0

    def updateSettingFile(self, value_to_update, new_value):
        character[value_to_update] = new_value
        with open("data/stat/character.json", "w") as file:
            json.dump(character, file, indent=4)

    def updateCharacterFile(self, value_to_update, new_value=""):
        with open("data/stat/character.json") as file:
            character = json.load(file)
        if value_to_update == "current_hp":
            character["current_hp"] = character["max_hp"]
        else:
            character[value_to_update] = new_value
        with open("data/stat/character.json", "w") as file:
            json.dump(character, file, indent=4)

    def update(self, game_state):
        self.checkInput(game_state)
        if self.is_choosing_level:
            self.drawChoosingLevelMenu()
        else:
            self.drawGameOverMenu()

    def checkInput(self, game_state):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if self.state < 2:
                        self.state += 1
                    else:
                        self.state = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_s:
                    if self.state > 0:
                        self.state -= 1
                    else:
                        self.state = 2
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    if self.state == 0:
                        if self.is_choosing_level:
                            game_state["game_over"] = False
                            game_state["game"] = True
                            self.start_time = None
                            self.pause_time = 0
                            self.updateCharacterFile("coin", 0)
                            self.updateCharacterFile("current_hp")
                            self.updateCharacterFile("level", "1-1")
                            self.is_choosing_level = False
                        else:
                            game_state["game_over"] = False
                            game_state["game"] = True
                            self.start_time = pygame.time.get_ticks()
                            self.pause_time = 0
                            self.updateCharacterFile("coin", 0)
                            self.updateCharacterFile("current_hp")
                    if self.state == 1:
                        if self.is_choosing_level:
                            game_state["game_over"] = False
                            game_state["game"] = True
                            self.start_time = pygame.time.get_ticks()
                            self.pause_time = 0
                            self.updateCharacterFile("coin", 0)
                            self.updateCharacterFile("current_hp")
                            self.updateCharacterFile("level", "1-2")
                            self.is_choosing_level = False
                        else:
                            self.is_choosing_level = True
                            self.state = 0
                    if self.state == 2:
                        if self.is_choosing_level:
                            self.is_choosing_level = False
                            self.state = 0
                        else:
                            game_state["game_over"] = False
                            game_state["menu"] = True
                            self.start_time = None
                            self.pause_time = 0
                            self.updateCharacterFile("coin", 0)
                            self.updateCharacterFile("current_hp")

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.restart_button.is_clicked(event.pos):
                    game_state["game_over"] = False
                    game_state["game"] = True
                    self.start_time = pygame.time.get_ticks()
                    self.pause_time = 0
                    self.updateCharacterFile("coin", 0)
                    self.updateCharacterFile("current_hp")

                if self.choose_level_button.is_clicked(event.pos):
                    self.is_choosing_level = True
                if self.main_menu_button.is_clicked(event.pos):
                    game_state["game_over"] = False
                    game_state["menu"] = True
                    self.start_time = None
                    self.pause_time = 0
                    self.updateCharacterFile("coin", 0)
                    self.updateCharacterFile("current_hp")

                if self.back_button.is_clicked(event.pos):
                    self.is_choosing_level = False
                    self.state = 0
                if self.choose_level_button.is_clicked(event.pos):
                    self.is_choosing_level = True
                    self.state = 0
                if self.level_one_button.is_clicked(event.pos):
                    game_state["game_over"] = False
                    game_state["game"] = True
                    self.start_time = pygame.time.get_ticks()
                    self.pause_time = 0
                    self.updateCharacterFile("coin", 0)
                    self.updateCharacterFile("current_hp")
                    self.updateCharacterFile("level", "1-1")
                    self.is_choosing_level = False
                if self.level_two_button.is_clicked(event.pos):
                    game_state["game_over"] = False
                    game_state["game"] = True
                    self.start_time = pygame.time.get_ticks()
                    self.pause_time = 0
                    self.updateCharacterFile("coin", 0)
                    self.updateCharacterFile("current_hp")
                    self.updateCharacterFile("level", "1-2")
                    self.is_choosing_level = False

    def drawGameOverMenu(self):
        # background = pygame.Surface(self.screen.get_size())
        # background.fill((0, 0, 0))
        # background.set_alpha(128)
        # self.screen.blit(background, (0, 0))
        # Now show stat of the player
        with open("data/stat/character.json") as file:
            character = json.load(file)
        if self.player_win:
            self.drawText("Level Pass", 200, 150, (255, 255, 255), 40)
            self.drawText("Congratulations", 300, 200, (255, 255, 255), 13)
        else:
            self.drawText("Game Over", 225, 150, (255, 255, 255), 40)
            self.drawText("Better Luck Next Time", 275, 200, (255, 255, 255), 13)
        self.drawText("Coin: " + str(character["coin"]), 300, 250, (255, 255, 255), 20)
        self.drawText("Level: " + character["level"], 300, 300, (255, 255, 255), 20)
        self.drawText("Time: ", 300, 350, (255, 255, 255), 20)  ##! cập nhật sau

        if self.state == 0:
            self.restart_button.drawHoverButton(self.screen)
            self.choose_level_button.drawButton(self.screen)
            self.main_menu_button.drawButton(self.screen)
        elif self.state == 1:
            self.restart_button.drawButton(self.screen)
            self.choose_level_button.drawHoverButton(self.screen)
            self.main_menu_button.drawButton(self.screen)
        elif self.state == 2:
            self.restart_button.drawButton(self.screen)
            self.choose_level_button.drawButton(self.screen)
            self.main_menu_button.drawHoverButton(self.screen)

    def drawChoosingLevelMenu(self):
        # background = pygame.Surface(self.screen.get_size())
        # background.fill((0, 0, 0))
        # background.set_alpha(128)
        # self.screen.blit(background, (0, 0))
        if self.state == 0:
            self.level_one_button.drawHoverButton(self.screen)
            self.level_two_button.drawButton(self.screen)
            self.back_button.drawButton(self.screen)
        elif self.state == 1:
            self.level_one_button.drawButton(self.screen)
            self.level_two_button.drawHoverButton(self.screen)
            self.back_button.drawButton(self.screen)
        elif self.state == 2:
            self.level_one_button.drawButton(self.screen)
            self.level_two_button.drawButton(self.screen)
            self.back_button.drawHoverButton(self.screen)

    def drawText(self, text, x, y, color, size):
        font = pygame.font.Font("fonts/font.ttf", size)
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(midleft=(x, y))
        self.screen.blit(text_surf, text_rect)