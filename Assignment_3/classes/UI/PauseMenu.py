import pygame
import sys
from classes.UI.PauseButton import PauseButton
from classes.SoundPlayer import SoundPlayer
import json

with open("data/settings/settings.json") as file:
    settings = json.load(file)


class PauseMenu:
    def __init__(self, screen, start_time, pause_time_start, pause_time, game_manager):
        self.screen = screen
        self.start_time = start_time
        self.pause_time = pause_time
        self.pause_time_start = pause_time_start
        self.isSetting = False
        self.sound_effect_is_on = settings["sound_effect"]
        self.background_music_is_on = settings["background_music"]
        self.resume_button = PauseButton(
            screen.get_width() // 2 - 125, 200, 1, (0, 0, 0), 24, "RESUME"
        )
        self.restart_button = PauseButton(
            screen.get_width() // 2 - 125, 300, 1, (0, 0, 0), 24, "RESTART"
        )
        self.option_button = PauseButton(
            screen.get_width() // 2 - 125, 400, 1, (0, 0, 0), 24, "OPTIONS"
        )
        self.main_menu_button = PauseButton(
            screen.get_width() // 2 - 125, 500, 1, (0, 0, 0), 24, "MENU"
        )
        self.background_music_button = PauseButton(
            screen.get_width() // 2 - 125,
            200,
            1,
            (0, 0, 0),
            24,
            ("MUSIC: OFF" if not self.background_music_is_on else "MUSIC: ON"),
        )
        self.sound_effect_button = PauseButton(
            screen.get_width() // 2 - 125,
            300,
            1,
            (0, 0, 0),
            24,
            ("SFX: OFF" if not self.sound_effect_is_on else "SFX: ON"),
        )
        self.back_button = PauseButton(
            screen.get_width() // 2 - 125, 400, 1, (0, 0, 0), 24, "BACK"
        )
        self.state = 0
        self.game_manager = game_manager

    def updateSettingFile(self, value_to_update, new_value):
        with open("data/settings/settings.json") as file:
            settings = json.load(file)
        settings[value_to_update] = new_value
        with open("data/settings/settings.json", "w") as file:
            json.dump(settings, file, indent=4)

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

        if self.isSetting:
            with open("data/settings/settings.json") as file:
                settings = json.load(file)
            self.background_music_is_on = settings.get(
                "background_music", self.background_music_is_on
            )
            self.sound_effect_is_on = settings.get(
                "sound_effect", self.sound_effect_is_on
            )
            self.drawOptionMenu()
        else:
            self.drawPauseMenu()

    def checkInput(self, game_state):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                SoundPlayer.get_instance().play_sound("click")
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if self.isSetting:
                        if self.state > 0:
                            self.state -= 1
                        else:
                            self.state = 2
                    else:
                        if self.state > 0:
                            self.state -= 1
                        else:
                            self.state = 3
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if self.isSetting:
                        if self.state < 2:
                            self.state += 1
                        else:
                            self.state = 0
                    else:
                        if self.state < 3:
                            self.state += 1
                        else:
                            self.state = 0
                elif event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    game_state["pause"] = False
                    game_state["game"] = True
                elif event.key == pygame.K_RETURN:
                    if self.state == 0:
                        if self.isSetting:
                            self.updateSettingFile(
                                "background_music", not self.background_music_is_on
                            )
                        else:
                            game_state["pause"] = False
                            game_state["game"] = True
                            self.pause_time += (
                                pygame.time.get_ticks() - self.pause_time_start
                            )
                    elif self.state == 1:
                        if self.isSetting:
                            self.updateSettingFile(
                                "sound_effect", not self.sound_effect_is_on
                            )
                        else:
                            game_state["pause"] = False
                            game_state["game"] = True
                            self.game_manager.new_game()
                            self.start_time = pygame.time.get_ticks()
                            self.pause_time = 0
                            self.updateCharacterFile("coin", 0)
                            self.updateCharacterFile("current_hp")
                    elif self.state == 2:
                        if self.isSetting:
                            self.isSetting = False
                        else:
                            self.isSetting = True
                    elif self.state == 3:
                        game_state["pause"] = False
                        game_state["menu"] = True
                        self.start_time = None
                        self.pause_time = 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                SoundPlayer.get_instance().play_sound("click")
                if self.resume_button.is_clicked(event.pos):
                    game_state["pause"] = False
                    game_state["game"] = True
                    self.pause_time = pygame.time.get_ticks() - self.pause_time_start

                elif self.restart_button.is_clicked(event.pos):
                    game_state["pause"] = False
                    game_state["game"] = True
                    self.game_manager.new_game()
                    self.start_time = pygame.time.get_ticks()
                    self.pause_time = 0
                    self.updateCharacterFile("coin", 0)
                    self.updateCharacterFile("current_hp")

                elif self.option_button.is_clicked(event.pos):
                    self.isSetting = True
                elif self.main_menu_button.is_clicked(event.pos):
                    game_state["pause"] = False
                    game_state["menu"] = True
                    self.start_time = None
                    self.pause_time = 0
                elif self.background_music_button.is_clicked(event.pos):
                    self.updateSettingFile(
                        "background_music", not self.background_music_is_on
                    )
                elif self.sound_effect_button.is_clicked(event.pos):
                    self.updateSettingFile("sound_effect", not self.sound_effect_is_on)
                elif self.back_button.is_clicked(event.pos):
                    self.isSetting = False
                elif self.main_menu_button.is_clicked(event.pos):
                    game_state["pause"] = False
                    game_state["menu"] = True
                    self.start_time = None
                    self.pause_time = 0
                    self.updateCharacterFile("coin", 0)
                    self.updateCharacterFile("current_hp")

    def drawPauseMenu(self):
        # background = pygame.Surface(self.screen.get_size())
        # background.fill((0, 0, 0))
        # background.set_alpha(128)
        # self.screen.blit(background, (0, 0))
        if self.state == 0:
            self.resume_button.drawHoverButton(self.screen)
            self.restart_button.drawButton(self.screen)
            self.option_button.drawButton(self.screen)
            self.main_menu_button.drawButton(self.screen)
        elif self.state == 1:
            self.resume_button.drawButton(self.screen)
            self.restart_button.drawHoverButton(self.screen)
            self.option_button.drawButton(self.screen)
            self.main_menu_button.drawButton(self.screen)
        elif self.state == 2:
            self.resume_button.drawButton(self.screen)
            self.restart_button.drawButton(self.screen)
            self.option_button.drawHoverButton(self.screen)
            self.main_menu_button.drawButton(self.screen)
        elif self.state == 3:
            self.resume_button.drawButton(self.screen)
            self.restart_button.drawButton(self.screen)
            self.option_button.drawButton(self.screen)
            self.main_menu_button.drawHoverButton(self.screen)

    def drawOptionMenu(self):
        # background = pygame.Surface(self.screen.get_size())
        # background.fill((0, 0, 0))
        # background.set_alpha(128)
        # self.screen.blit(background, (0, 0))
        self.background_music_button.text = "MUSIC: " + (
            "OFF" if not self.background_music_is_on else "ON"
        )
        self.sound_effect_button.text = "SFX: " + (
            "OFF" if not self.sound_effect_is_on else "ON"
        )
        if self.state == 0:
            self.background_music_button.drawHoverButton(self.screen)
            self.sound_effect_button.drawButton(self.screen)
            self.back_button.drawButton(self.screen)
        elif self.state == 1:
            self.background_music_button.drawButton(self.screen)
            self.sound_effect_button.drawHoverButton(self.screen)
            self.back_button.drawButton(self.screen)
        elif self.state == 2:
            self.background_music_button.drawButton(self.screen)
            self.sound_effect_button.drawButton(self.screen)
            self.back_button.drawHoverButton(self.screen)