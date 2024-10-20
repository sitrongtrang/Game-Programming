// #include "imgui.h"
// #include "imgui_impl_sdl2.h"
// #include "imgui_impl_opengl3.h"
// #include <SDL.h>
// #include <SDL_opengl.h>
// #include <SDL_image.h>
// #include <stdio.h>
// #include <chrono>
#include "../headers/Constant.h"
#include "../headers/menu/Game_over_menu.h"
#include "../headers/menu/Introduction.h"
#include "../headers/menu/Main_menu.h"
#include "../headers/menu/Pause_menu.h"
#include "../headers/menu/Game_menu.h"
#include "../headers/utils.h"
#include "../headers/keySetMenu.h"
#include "../headers/keyBinding.h"
#include "../headers/Ball.h"
#include "../headers/Surface.h"
#include "../headers/inputManager.h"
#include "../headers/Character.h"
#include "../headers/GameManager.h"
#include <stdio.h>

// float square_x = 0.0f;    // Square's X position
// float square_y = 0.0f;    // Square's Y position
// float square_size = 0.1f; // Size of the square

int score1 = 0;
int score2 = 0;
bool game_running = true;
bool game_paused = false;

// Clear color variable
ImVec4 clear_color = ImVec4(0.0f, 0.0f, 0.0f, 1.0f);
KeySetMenu keySetMenu(keyBindingsInstance);

// Function to update the game logic
// void UpdateGame()
// {
//     const Uint8 *state = SDL_GetKeyboardState(NULL);
//     if (state[SDL_SCANCODE_UP])
//         square_y += 0.01f; // Move up
//     if (state[SDL_SCANCODE_DOWN])
//         square_y -= 0.01f; // Move down
//     if (state[SDL_SCANCODE_LEFT])
//         square_x -= 0.01f; // Move left
//     if (state[SDL_SCANCODE_RIGHT])
//         square_x += 0.01f; // Move right
// }
GLuint LoadTextureFromFile(const char *filename)
{
    SDL_Surface *surface = IMG_Load(filename);
    if (!surface)
    {
        printf("Error: %s\n", IMG_GetError());
        return 0;
    }

    GLuint textureID;
    glGenTextures(1, &textureID);
    glBindTexture(GL_TEXTURE_2D, textureID);

    // Set texture parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

    // Load the texture into OpenGL
    int mode = surface->format->BytesPerPixel == 4 ? GL_RGBA : GL_RGB;
    glTexImage2D(GL_TEXTURE_2D, 0, mode, surface->w, surface->h, 0, mode, GL_UNSIGNED_BYTE, surface->pixels);

    // Unbind the texture
    glBindTexture(GL_TEXTURE_2D, 0);

    // Free the SDL surface
    SDL_FreeSurface(surface);

    return textureID;
}

// Function to render a simple square


int main(int, char **)
{
    // Initialize SDL
    GameManager * gameManager = GameManager::getInstance();
    InputManager* inputManager = new InputManager();

    if (SDL_Init(SDL_INIT_VIDEO | SDL_INIT_TIMER | SDL_INIT_GAMECONTROLLER) != 0)
    {
        printf("Error: %s\n", SDL_GetError());
        return -1;
    }

    // Set up OpenGL context and SDL window
    const char *glsl_version = "#version 130";
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_FLAGS, 0);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 3);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 0);

    SDL_Window *window = SDL_CreateWindow("Tiny Football Game",
                                          SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                                          SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_OPENGL | SDL_WINDOW_RESIZABLE);
    SDL_GLContext gl_context = SDL_GL_CreateContext(window);
    SDL_GL_MakeCurrent(window, gl_context);
    SDL_GL_SetSwapInterval(1); // Enable vsync

    // Initialize Dear ImGui context
    IMGUI_CHECKVERSION();
    ImGui::CreateContext();
    ImGuiIO &io = ImGui::GetIO();
    (void)io;
    ImGui::StyleColorsDark();

    // Set up ImGui for SDL and OpenGL
    ImGui_ImplSDL2_InitForOpenGL(window, gl_context);
    ImGui_ImplOpenGL3_Init(glsl_version);

    // Load and set the window icon
    SDL_Surface *icon_surface = IMG_Load("./images/game_icon.jpg");

    if (icon_surface)
    {
        SDL_Surface *resized_icon_surface = SDL_CreateRGBSurface(0, 1440, 1440, 32, 0, 0, 0, 0);
        SDL_BlitScaled(icon_surface, NULL, resized_icon_surface, NULL);
        SDL_SetWindowIcon(window, resized_icon_surface);
        SDL_FreeSurface(resized_icon_surface);
    }

    GLuint background_texture = LoadTextureFromFile("./images/main_menu.jpg");
    io.Fonts->AddFontFromFileTTF("./fonts/font.ttf", 24.0f);

    startTime = std::chrono::steady_clock::now();
    GameState state = GameState::INTRODUCTION;
    // Main loop

    while (game_running)
    {
        SDL_Event event;
        while (SDL_PollEvent(&event))
        {
            ImGui_ImplSDL2_ProcessEvent(&event);
            if (event.type == SDL_QUIT)
            {
                game_running = false;
            }
            if (event.type == SDL_KEYDOWN && event.key.keysym.sym == SDLK_ESCAPE)
            {
                game_paused = !game_paused;
                if (game_paused)
                {
                    pauseTime = std::chrono::steady_clock::now();
                }
                else
                {
                    pausedDuration += std::chrono::duration_cast<std::chrono::seconds>(std::chrono::steady_clock::now() - pauseTime).count();
                }
            } else if (event.type== SDL_KEYDOWN) {
                if (state == GameState::PLAYING)
                    inputManager->input(event.key.keysym.sym);
            } else if (event.type== SDL_KEYUP) {
                if (state == GameState::PLAYING)
                    inputManager->release(event.key.keysym.sym);
            }
        }

        // Start the ImGui frame
        ImGui_ImplOpenGL3_NewFrame();
        ImGui_ImplSDL2_NewFrame();
        ImGui::NewFrame();
        glClear(GL_COLOR_BUFFER_BIT);
        if (state == GameState::INTRODUCTION)
        {
            SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
            renderIntroduction(renderer, "./images/hcmut_icon.jpg", 5000);
            state = GameState::MAIN_MENU;
            SDL_DestroyRenderer(renderer);
        }
        else if (state == GameState::MAIN_MENU)
        {
            renderBackground(background_texture);
            renderMainMenu(state);
        }
        else if (state == GameState::NEW_GAME) 
        {
            gameManager->newGame(inputManager);
            state = GameState::PLAYING;
        }
        else if (game_paused)
        {
            keySetMenu.Render(game_paused);
            // renderPauseMenu(state, score1, score2);
        }
        else if (state == GameState::GAME_OVER)
        {
            renderGameOver(state, score1, score2);
        }
        else if (state == GameState::PLAYING)
        {

            renderGameMenu(state, score1, score2);
            // UpdateGame();
            // RenderSquare();
            // Character * test = gameManager->getTeamBCharacter(0);
            // // ball->draw();
            // test->update(0.016f);
            // test->draw();
            // surface->draw();
            gameManager->update(0.016f);
        }

        // Rendering
        ImGui::Render();
        ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());
        SDL_GL_SwapWindow(window);
    }

    // Cleanup
    ImGui_ImplOpenGL3_Shutdown();
    ImGui_ImplSDL2_Shutdown();
    ImGui::DestroyContext();

    SDL_GL_DeleteContext(gl_context);
    SDL_DestroyWindow(window);

    SDL_Quit();

    return 0;
}