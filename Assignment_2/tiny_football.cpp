#include <SDL2/SDL.h>
#include <SDL2/SDL_ttf.h>
#include <iostream>
#include <cstdlib>
#include <imgui.h>
#include <imgui_impl_sdl2.h>
#include <imgui_impl_opengl3.h>
// #include "./headers/keySetMenu.h"
#include "./headers/utils.h"

struct Player {
    int x, y;
    int velY;
};

struct Ball {
    int x, y;
    int velX, velY;
};

void handlePlayerInput(SDL_Event& e, Player& player, int upKey, int downKey) {
    if (e.type == SDL_KEYDOWN) {
        if (e.key.keysym.sym == upKey) {
            player.velY = -5;
        } else if (e.key.keysym.sym == downKey) {
            player.velY = 5;
        }
    }
    if (e.type == SDL_KEYUP) {
        if (e.key.keysym.sym == upKey || e.key.keysym.sym == downKey) {
            player.velY = 0;
        }
    }
}

void movePlayer(Player& player) {
    player.y += player.velY;

    if (player.y < 0) {
        player.y = 0;
    } else if (player.y + PLAYER_HEIGHT > SCREEN_HEIGHT) {
        player.y = SCREEN_HEIGHT - PLAYER_HEIGHT;
    }
}

void moveBall(Ball& ball, Player& player1, Player& player2) {
    ball.x += ball.velX;
    ball.y += ball.velY;

    if (ball.y <= 0 || ball.y >= SCREEN_HEIGHT - BALL_SIZE) {
        ball.velY = -ball.velY;
    }

    if ((ball.x <= player1.x + PLAYER_WIDTH && ball.y + BALL_SIZE >= player1.y && ball.y <= player1.y + PLAYER_HEIGHT) ||
        (ball.x + BALL_SIZE >= player2.x && ball.y + BALL_SIZE >= player2.y && ball.y <= player2.y + PLAYER_HEIGHT)) {
        ball.velX = -ball.velX;
    }

    if (ball.x <= 0 || ball.x >= SCREEN_WIDTH - BALL_SIZE) {
        ball.x = SCREEN_WIDTH / 2;
        ball.y = SCREEN_HEIGHT / 2;
        ball.velX = (rand() % 2 == 0) ? 5 : -5;
        ball.velY = (rand() % 2 == 0) ? 5 : -5;
    }
}

bool initTTF() {
    if (TTF_Init() == -1) {
        std::cerr << "TTF could not initialize! TTF_Error: " << TTF_GetError() << std::endl;
        return false;
    }
    return true;
}

int main(int argc, char* args[]) {
    // Initialize SDL
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cerr << "SDL could not initialize! SDL_Error: " << SDL_GetError() << std::endl;
        return -1;
    }
    if (!initTTF()) {
        SDL_Quit();
        return -1;
    }

    SDL_Window* window = SDL_CreateWindow("Tiny Football", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);
    if (window == nullptr) {
        std::cerr << "Window could not be created! SDL_Error: " << SDL_GetError() << std::endl;
        return -1;
    }

    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (renderer == nullptr) {
        std::cerr << "Renderer could not be created! SDL_Error: " << SDL_GetError() << std::endl;
        return -1;
    }
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 3);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 2);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE);
    // Setup ImGui context
    IMGUI_CHECKVERSION();
    ImGui::CreateContext();
    ImGui_ImplSDL2_InitForOpenGL(window, renderer); // Initialize ImGui for SDL
    ImGui_ImplOpenGL3_Init("#version 130"); // Set GLSL version


    Player player1 = { 50, SCREEN_HEIGHT / 2 - PLAYER_HEIGHT / 2, 0 };
    Player player2 = { SCREEN_WIDTH - 50 - PLAYER_WIDTH, SCREEN_HEIGHT / 2 - PLAYER_HEIGHT / 2, 0 };
    Ball ball = { SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 5, 5 };

    bool quit = false;
    SDL_Event e;

    while (!quit) {
        // Start a new ImGui frame
        ImGui_ImplSDL2_NewFrame(); // No parameters needed here
        ImGui_ImplOpenGL3_NewFrame(); 
        ImGui::NewFrame();

        // Poll events
        while (SDL_PollEvent(&e) != 0) {
            if (e.type == SDL_QUIT) {
                quit = true;
            }


            // Handle key events if the menu is not visible

            handlePlayerInput(e, player1, SDLK_w, SDLK_s);
            handlePlayerInput(e, player2, SDLK_UP, SDLK_DOWN);


        }

        // Move players and ball when not in the key set menu

        movePlayer(player1);
        movePlayer(player2);
        moveBall(ball, player1, player2);


        // Clear screen
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);

        // Render players and ball
        SDL_Rect player1Rect = { player1.x, player1.y, PLAYER_WIDTH, PLAYER_HEIGHT };
        SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
        SDL_RenderFillRect(renderer, &player1Rect);

        SDL_Rect player2Rect = { player2.x, player2.y, PLAYER_WIDTH, PLAYER_HEIGHT };
        SDL_SetRenderDrawColor(renderer, 0, 0, 255, 255);
        SDL_RenderFillRect(renderer, &player2Rect);

        SDL_Rect ballRect = { ball.x, ball.y, BALL_SIZE, BALL_SIZE };
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        SDL_RenderFillRect(renderer, &ballRect);


        // Render ImGui
        ImGui::Render();
        ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());

        // Update screen
        SDL_RenderPresent(renderer);

        // Frame rate control
        SDL_Delay(16);
    }

    // Cleanup
    ImGui_ImplOpenGL3_Shutdown();
    ImGui_ImplSDL2_Shutdown();
    ImGui::DestroyContext();

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
