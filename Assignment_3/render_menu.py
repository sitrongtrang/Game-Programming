import pygame
import sys
from random import randint
from classes.MainMenu import MainMenu
from classes.GameMenu import GameMenu
from classes.PauseMenu import PauseMenu
from classes.GameOverMenu import GameOverMenu

##! delete after finalize game
# running = True
pygame.init()

screen_width = 800
screen_height = 600

BLUR_OVERLAY = (0, 0, 0, 130)
PRESET_COLOURS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "yellow": (255, 255, 0),
    "heavy_green": (24, 175, 24),
}


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario")
game_state = {
    "menu": True,
    "game": False,
    "pause": False,
    "game_over": False,
}


def blur_surface(surface, amount):
    array = pygame.surfarray.pixels3d(surface)
    for _ in range(amount):
        array[1:, :] = (array[1:, :] + array[:-1, :]) // 2
        array[:, 1:] = (array[:, 1:] + array[:, :-1]) // 2
        array[1:, :] = (array[1:, :] + array[:-1, :]) // 2
        array[:, 1:] = (array[:, 1:] + array[:, :-1]) // 2
    return surface


# background_music=pygame.mixer.Sound("") ##! cần cập nhật sau
def main():
    clock = pygame.time.Clock()
    running = True
    main_menu = MainMenu(screen, "images/menu_background_image.png", "", "")
    game_menu = GameMenu(screen, "", None)
    pause_menu = PauseMenu(screen, None, None, 0)
    game_over_menu = GameOverMenu(screen, None, False)
    temp_gameplay_test = pygame.image.load("images/menu_background_image.png")
    while running:
        screen.fill((0, 0, 0))
        if game_state["menu"]:
            main_menu.update(game_state)
        elif game_state["game"]:
            if game_menu.start_time is None:
                game_menu.start_time = pygame.time.get_ticks()
            ##! gameplay here
            screen.blit(temp_gameplay_test, (0, 0))
            game_menu.update(pause_menu.pause_time)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                        game_state["pause"] = True
                        game_state["game"] = False
                        paused_screen = screen.copy()
                        paused_screen = blur_surface(paused_screen, 5)
                        pause_menu.pause_time_start = pygame.time.get_ticks()
                    if event.key == pygame.K_SPACE:  ##! xóa sau khi finalize
                        end_screen = screen.copy()  ##! xóa sau khi finalize
                        end_screen = blur_surface(
                            end_screen, 5
                        )  ##! xóa sau khi finalize
                        game_state["game"] = False  ##! xóa sau khi finalize
                        game_state["game_over"] = True  ##! xóa sau khi finalize

        elif game_state["pause"]:
            screen.blit(paused_screen, (0, 0))
            pause_menu.start_time = game_menu.start_time
            pause_menu.update(game_state)
            game_menu.start_time = pause_menu.start_time

        elif game_state["game_over"]:
            screen.blit(end_screen, (0, 0))
            game_over_menu.start_time = game_menu.start_time
            game_over_menu.update(game_state)
            game_menu.start_time = game_over_menu.start_time
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
