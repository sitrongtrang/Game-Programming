import pygame
import sys
from classes.UI.MenuButton import MenuButton
from classes.UI.LevelButton import LevelButton
import json

with open("data/settings/settings.json") as setting_file:
    settings = json.load(setting_file)
with open("data/stat/character.json") as character_file:
    character = json.load(character_file)


class MainMenu:
    def __init__(self, screen, background_image, background_music, sound_effect, game_manager):
        self.screen = screen
        self.background_image = pygame.image.load(background_image)
        self.background_music = background_music
        self.sound_effect = sound_effect
        self.background_music_is_on = settings.get("background_music", False)
        self.sound_effect_is_on = settings.get("sound_effect", False)
        self.is_setting = False
        self.is_choosing_level = False
        self.choose_level_button = MenuButton(
            150, 350, 1, (0, 0, 0), 24, "CHOOSE LEVEL"
        )
        self.setting_button = MenuButton(150, 400, 1, (0, 0, 0), 24, "SETTINGS")
        self.quit_button = MenuButton(150, 450, 1, (0, 0, 0), 24, "QUIT")
        self.background_music_button = MenuButton(
            150, 350, 1, (0, 0, 0), 24, "MUSIC: OFF"
        )
        self.sfx_button = MenuButton(150, 400, 1, (0, 0, 0), 24, "SFX: OFF")
        self.back_button = MenuButton(150, 450, 1, (0, 0, 0), 24, "BACK")
        self.level_one_button = LevelButton(100, 150, 1, (0, 0, 0), 24, "1 - 1")
        self.level_two_button = LevelButton(325, 150, 1, (0, 0, 0), 24, "1 - 2")
        self.return_button = LevelButton(550, 150, 1, (0, 0, 0), 24, "BACK")
        self.state = 0
        self.game_manager = game_manager

    def updateSettingFile(self, value_to_update, new_value):
        with open("data/settings/settings.json") as setting_file:
            settings = json.load(setting_file)
        settings[value_to_update] = new_value
        with open("data/settings/settings.json", "w") as file:
            json.dump(settings, file, indent=4)

    def updateCharacterFile(self, value_to_update, new_value):
        with open("data/stat/character.json") as file:
            character = json.load(file)
        character[value_to_update] = new_value
        with open("data/stat/character.json", "w") as file:
            json.dump(character, file, indent=4)

    ##? change screen menu
    def update(self, game_state):
        self.checkInput(game_state)
        if self.is_choosing_level:
            self.screen.fill((0, 0, 0))
            self.drawBackground()
            self.drawChooseLevelMenu()
        elif self.is_setting:
            with open("data/settings/settings.json") as setting_file:
                settings = json.load(setting_file)
            self.background_music_is_on = settings["background_music"]
            self.sound_effect_is_on = settings["sound_effect"]
            self.screen.fill((0, 0, 0))
            self.drawBackground()
            self.drawSettingMenu()
        else:
            self.screen.fill((0, 0, 0))
            self.drawBackground()
            self.drawMainMenu()

    ##? handle input from player
    def checkInput(self, game_state):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.is_setting or self.is_choosing_level:
                        self.is_setting = False
                        self.is_choosing_level = False
                    else:
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if self.state < 2:
                        self.state += 1
                    else:
                        self.state = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if self.state > 0:
                        self.state -= 1
                    else:
                        self.state = 2
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if self.is_choosing_level:
                        if self.state > 0:
                            self.state -= 1
                        else:
                            self.state = 2
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if self.is_choosing_level:
                        if self.state < 2:
                            self.state += 1
                        else:
                            self.state = 0
                elif event.key == pygame.K_RETURN:
                    if self.state == 0:
                        if self.is_setting:
                            self.updateSettingFile(
                                "background_music", not self.background_music_is_on
                            )
                        elif self.is_choosing_level:
                            game_state["menu"] = False
                            game_state["game"] = True
                            self.game_manager.new_game("1-1")
                            self.updateCharacterFile("level", "1-1")
                        else:
                            self.playSoundEffect()
                            self.is_choosing_level = True
                            self.state = 0
                    elif self.state == 1:
                        if self.is_setting:
                            self.updateSettingFile(
                                "sound_effect", not self.sound_effect_is_on
                            )
                        elif self.is_choosing_level:
                            game_state["menu"] = False
                            game_state["game"] = True
                            self.game_manager.new_game("1-2")
                            self.updateCharacterFile("level", "1-2")
                        else:
                            self.playSoundEffect()
                            self.is_setting = True
                            self.state = 0
                    elif self.state == 2:
                        if self.is_setting or self.is_choosing_level:
                            self.playSoundEffect()
                            self.is_setting = False
                            self.is_choosing_level = False
                            self.state = 0
                        else:
                            self.playSoundEffect()
                            self.state = 2
                            pygame.quit()
                            sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.quit_button.is_clicked(event.pos):
                    self.playSoundEffect()
                    self.state = 2
                    pygame.quit()
                    sys.exit()
                elif self.setting_button.is_clicked(event.pos):
                    self.playSoundEffect()
                    self.is_setting = True
                    self.state = 1
                elif self.choose_level_button.is_clicked(event.pos):
                    self.playSoundEffect()
                    self.is_choosing_level = True
                    self.state = 0
                elif self.background_music_button.is_clicked(event.pos):
                    self.updateSettingFile(
                        "background_music", not self.background_music_is_on
                    )
                elif self.sfx_button.is_clicked(event.pos):
                    self.updateSettingFile("sound_effect", not self.sound_effect_is_on)
                elif self.back_button.is_clicked(event.pos):
                    self.is_setting = False
                    self.state = 0
                elif self.level_one_button.is_clicked(event.pos):
                    game_state["menu"] = False
                    game_state["game"] = True
                    self.game_manager.new_game("1-1")
                    self.updateCharacterFile("level", "1-1")
                elif self.level_two_button.is_clicked(event.pos):
                    game_state["menu"] = False
                    game_state["game"] = True
                    self.game_manager.new_game("1-2")
                    self.updateCharacterFile("level", "1-2")
                elif self.return_button.is_clicked(event.pos):
                    self.is_choosing_level = False
                    self.state = 0

    ##? draw background elements for all menus
    def drawBackground(self):
        # if self.background_music_is_on:
        # self.background_music.play() ##! cập nhật lại sau
        self.screen.blit(
            pygame.transform.scale(self.background_image, self.screen.get_size()),
            (0, 0),
        )  ##! cập nhật lại sau

    ##? play sound effect when clicking
    def playSoundEffect(self):
        # if self.sound_effect_is_on:
        #     self.sound_effect.play()
        pass

    ##? draw main menu
    def drawMainMenu(self):
        image = pygame.image.load("images/title_screen.png")
        image = pygame.transform.scale(image, (500, 200))
        self.screen.blit(image, (150, 100))
        if self.state == 0:
            self.choose_level_button.drawHoverButton(self.screen)
            self.setting_button.drawButton(self.screen)
            self.quit_button.drawButton(self.screen)
        elif self.state == 1:
            self.choose_level_button.drawButton(self.screen)
            self.setting_button.drawHoverButton(self.screen)
            self.quit_button.drawButton(self.screen)
        elif self.state == 2:
            self.choose_level_button.drawButton(self.screen)
            self.setting_button.drawButton(self.screen)
            self.quit_button.drawHoverButton(self.screen)
        # pygame.display.flip()

    ##? draw setting menu
    def drawSettingMenu(self):
        if self.background_music_is_on:
            self.background_music_button.text = "MUSIC: ON"
        else:
            self.background_music_button.text = "MUSIC: OFF"
        if self.sound_effect_is_on:
            self.sfx_button.text = "SFX: ON"
        else:
            self.sfx_button.text = "SFX: OFF"
        if self.state == 0:
            self.background_music_button.drawHoverButton(self.screen)
            self.sfx_button.drawButton(self.screen)
            self.back_button.drawButton(self.screen)
        elif self.state == 1:
            self.background_music_button.drawButton(self.screen)
            self.sfx_button.drawHoverButton(self.screen)
            self.back_button.drawButton(self.screen)
        elif self.state == 2:
            self.background_music_button.drawButton(self.screen)
            self.sfx_button.drawButton(self.screen)
            self.back_button.drawHoverButton(self.screen)

        pygame.display.flip()

    ##? draw choosing level menu
    def drawChooseLevelMenu(self):
        if self.state == 0:
            self.level_one_button.drawHoverButton(self.screen)
            self.level_two_button.drawButton(self.screen)
            self.return_button.drawButton(self.screen)
        elif self.state == 1:
            self.level_one_button.drawButton(self.screen)
            self.level_two_button.drawHoverButton(self.screen)
            self.return_button.drawButton(self.screen)
        elif self.state == 2:
            self.level_one_button.drawButton(self.screen)
            self.level_two_button.drawButton(self.screen)
            self.return_button.drawHoverButton(self.screen)
        pygame.display.flip()
