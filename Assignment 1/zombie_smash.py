import pygame
import sys
from random import randint
from Zombie import Zombie
from Pit import Pit
from Button import Button
from menu_button import Menu_Button
pygame.init()

screen_width = 800
screen_height = 600

BLUR_OVERLAY = (0,0,0, 130)
PRESET_COLOURS = {
    'red' : (255, 0, 0),
    'green' : (0, 255, 0),
    'blue' : (0, 0, 255),
    'black' : (0, 0, 0),
    'white' : (255,255,255),
    'yellow' : (255,255,0),
    'heavy_green':(24,175,24)
}


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Zombie Game")

original_zombie_sprite = pygame.image.load('sprites/zombie.png')
zombie_width = 100
zombie_height = 100

zombie_sprite = pygame.transform.scale(original_zombie_sprite, (zombie_width, zombie_height))

background_sprite = pygame.image.load('sprites/background.png')
background_sprite = pygame.transform.scale(background_sprite, (screen_width, screen_height))

font = pygame.font.Font(None, 36)

# Sound effect and music setup
pygame.mixer.music.load('musics/music.mp3')
pygame.mixer.music.play(-1, 0.0, 5000)
hit_fx = pygame.mixer.Sound('sounds/coin.wav')


def add_zombie():
    centers = pits.centers
    max_attempts = 10  # Number of attempts to find a valid spawn location
    for _ in range(max_attempts):
        zombie_x, zombie_y = centers[randint(0, len(centers) - 1)]
        new_zombie_rect = pygame.Rect(zombie_x - zombie_width // 2, zombie_y - zombie_height // 2, zombie_width,
                                      zombie_height)
        overlap = any(new_zombie_rect.colliderect(pygame.Rect(z.x, z.y, z.width, z.height)) for z in zombies)

        if not overlap:
            zombie = Zombie(zombie_x - zombie_width // 2, zombie_y - zombie_height // 2, zombie_width, zombie_height,
                            zombie_sprite)
            zombies.append(zombie)
            zombie.spawn()
            break

def comment_score(score):
    comment = {
        "excelent": ("You are a true zombie terminator!", (100, 255, 100)),
        "good": ("You have guard us well!", (50, 255, 50)),
        "bad": ("You tried... I guess?",  PRESET_COLOURS["red"]),
        "else" : ("The zombie apocalypse is here because of you!", PRESET_COLOURS["red"])
    }
    ladder = {
        "excelent": 18,
        "good": 9,
        "bad": 0,
    }
    response = ["excelent", "good", "bad"]
    for res in response:
        if score >= ladder[res]:
            return comment[res]
    return comment["else"]

def end_screen():

    def blur(screenshoot): 
        overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        overlay.fill(BLUR_OVERLAY)
        screen.blit(overlay, (0, 0)) 


    zombies.clear()
    screenshot = screen.copy()
    blur(screenshot) 

    score = hit - miss 
    score_text = font.render(f"Score: {score if score > 0 else 0}", True, PRESET_COLOURS["white"])
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, screen_height // 2 - score_text.get_height() // 2))   
    comment, comment_color = comment_score(score)
    comment_text = font.render(f"{comment}", True, comment_color)
    screen.blit(comment_text, (screen_width // 2 - comment_text.get_width() // 2, screen_height // 2 + comment_text.get_height() // 2))

    play_button.draw(screen)
    exit_button.draw(screen)

    pygame.display.flip()

big_font = pygame.font.Font("fonts/font.ttf", 42)
small_font = pygame.font.Font(None, 36)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)
    
def main_menu():
    global start_ticks
    while True:
        main_menu_background = pygame.image.load('sprites/main_menu_background.jpg')
        main_menu_background = pygame.transform.scale(main_menu_background, (screen_width, screen_height))
        
        small_background = pygame.transform.smoothscale(main_menu_background, (screen_width // 8, screen_height // 8))
        blurred_background = pygame.transform.smoothscale(small_background, (screen_width, screen_height))
        
        screen.blit(blurred_background, (0, 0))
        
        draw_text('WHACK A ZOMBIE', big_font, PRESET_COLOURS["white"], screen, screen_width // 2, 150)
        start_button = Menu_Button(screen_width // 2 - 125, 275,1,PRESET_COLOURS["black"],40, "START")
        start_button.draw(screen)
        
        quit_button = Menu_Button(screen_width // 2 - 125/1.25, 375,1.25,PRESET_COLOURS["black"],36, "QUIT")
        quit_button.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_clicked(event.pos):
                    start_ticks = pygame.time.get_ticks()
                    return 
                if quit_button.is_clicked(event.pos):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

def pause_menu():
    global pause_end_time,pause_start_time,start_ticks,pause_time,is_paused,hit,miss,ingame
    pause_start_time = pygame.time.get_ticks()
    while True:
        small_background = pygame.transform.smoothscale(background_sprite, (screen_width // 8, screen_height // 8))
        blurred_background = pygame.transform.smoothscale(small_background, (screen_width, screen_height))
        
        screen.blit(blurred_background, (0, 0))
        draw_text('PAUSE', big_font, PRESET_COLOURS["black"], screen, screen_width // 2, 100)
        return_button = Menu_Button(screen_width // 2 - 125, 200,1,PRESET_COLOURS["black"],30, "RETURN")
        return_button.draw(screen)
        restart_button = Menu_Button(screen_width // 2 - 125, 300,1,PRESET_COLOURS["black"],30, "RESTART")
        restart_button.draw(screen)
        back_button = Menu_Button(screen_width // 2 - 125, 400,1,PRESET_COLOURS["black"],30, "MENU")
        back_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_SPACE:
                    pause_end_time = pygame.time.get_ticks()
                    pause_time += pause_end_time - pause_start_time
                    is_paused = False
                    return  
                if event.key == pygame.K_ESCAPE:
                    start_ticks = pygame.time.get_ticks()
                    return main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.is_clicked(event.pos):
                    pause_end_time = pygame.time.get_ticks()
                    pause_time += pause_end_time - pause_start_time
                    is_paused = False
                    return
                if restart_button.is_clicked(event.pos):
                    hit = 0
                    miss = 0
                    start_ticks = pygame.time.get_ticks()
                    ingame = True
                    pause_time=0
                    zombies.clear()
                    is_paused = False
                    return
                if back_button.is_clicked(event.pos):
                    hit = 0
                    miss = 0
                    start_ticks = pygame.time.get_ticks()
                    ingame = True
                    pause_time=0
                    zombies.clear()
                    is_paused = False
                    return main_menu()
        pygame.display.flip()

running = True
hit = 0
miss = 0
times = 30 * 1000
start_ticks= pygame.time.get_ticks()
pits = Pit(140, 193, 665, 511)
zombies = []
last_spawn = 0
ingame = True
is_paused = False
pause_start_time = pygame.time.get_ticks()
pause_end_time = pygame.time.get_ticks()
pause_time= 0 

play_button = Button(200, 400, (0, 180, 0), "Play Again")
exit_button = Button(400, 400, (180,0,0), "Exit")

def main_game():
    global zombies, hit, miss, times, start_ticks, play_button, exit_button, play_button, exit_button, ingame, last_spawn,running,is_paused,pause_time
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and (times + pause_time - ( pygame.time.get_ticks() - start_ticks) ) // 1000>0:
                if event.key == pygame.K_p or event.key == pygame.K_SPACE:
                    is_paused = True
                    pause_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and ingame and event.button == 1:
                # Normal loop
                for zombie in zombies:
                    if zombie.is_smashed(event.pos):
                        # Call zomebie death   
                        zombie.stun()
                        zombie.death()
                        hit += 1
                        hit_fx.play()
                        break
                else:
                    miss += 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.is_clicked(event.pos):
                    hit = 0
                    miss = 0
                    start_ticks = pygame.time.get_ticks()
                    ingame = True
                    pause_time=0
                    zombies.clear()
                elif exit_button.is_clicked(event.pos):
                    running = False
                pass

        screen.blit(background_sprite, (0, 0))

        # Update
        times_left = (times + pause_time - ( pygame.time.get_ticks() - start_ticks) ) // 1000
        if times_left <= 0:
            # Game end branch
            # 
            ingame = False
            end_screen()
            pygame.display.flip()
            continue

        time_text = font.render(f"Time: {times_left if times_left >= 0 else 0}", True, (0, 0, 0))
        time_rect = time_text.get_rect(topleft=(10, 10))
        screen.blit(time_text, time_rect)

        hit_text = font.render(f"Hits: {hit}", True, (0, 0, 0))
        hit_rect = hit_text.get_rect(topright=(screen_width - 10, 10))
        screen.blit(hit_text, hit_rect)

        miss_text = font.render(f"Misses: {miss}", True, (0, 0, 0))
        miss_rect = miss_text.get_rect(topright=(screen_width - 10, hit_rect.bottom + 10))
        screen.blit(miss_text, miss_rect)
        if not is_paused:
            current_time = pygame.time.get_ticks()
            # Remove zombies that have been stunned for 1 second
            zombies = [zombie for zombie in zombies if not zombie.is_stunned_for_duration()]
            zombies = [zombie for zombie in zombies if current_time - zombie.appear_time < zombie.stay_time + pause_time]

            for zombie in zombies:
                zombie.update(zombies)

            #Draw
            for zombie in zombies:
                zombie.draw(screen)

            if current_time - last_spawn - pause_time >= 1000:
                spawn = randint(0, 1)
                if spawn:
                    last_spawn = pygame.time.get_ticks()
                    add_zombie()

        pygame.display.flip()

    pygame.quit()
    sys.exit()
    
main_menu()
main_game()