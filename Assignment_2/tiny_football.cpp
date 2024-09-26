#include <SDL2/SDL.h>
#include <iostream>
#include <cstdlib>

const int SCREEN_WIDTH = 800;
const int SCREEN_HEIGHT = 600;
const int PLAYER_WIDTH = 20;
const int PLAYER_HEIGHT = 100;
const int BALL_SIZE = 15;

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

int main(int argc, char* args[]) {
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cerr << "SDL could not initialize! SDL_Error: " << SDL_GetError() << std::endl;
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

    Player player1 = { 50, SCREEN_HEIGHT / 2 - PLAYER_HEIGHT / 2, 0 };
    Player player2 = { SCREEN_WIDTH - 50 - PLAYER_WIDTH, SCREEN_HEIGHT / 2 - PLAYER_HEIGHT / 2, 0 };
    Ball ball = { SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 5, 5 };

    bool quit = false;
    SDL_Event e;

    while (!quit) {
        while (SDL_PollEvent(&e) != 0) {
            if (e.type == SDL_QUIT) {
                quit = true;
            }

            // Xử lý phím cho cả hai người chơi
            handlePlayerInput(e, player1, SDLK_w, SDLK_s);
            handlePlayerInput(e, player2, SDLK_UP, SDLK_DOWN);
        }

        // Di chuyển người chơi
        movePlayer(player1);
        movePlayer(player2);

        // Di chuyển bóng
        moveBall(ball, player1, player2);

        // Clear màn hình
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);

        // Vẽ người chơi 1
        SDL_Rect player1Rect = { player1.x, player1.y, PLAYER_WIDTH, PLAYER_HEIGHT };
        SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
        SDL_RenderFillRect(renderer, &player1Rect);

        // Vẽ người chơi 2
        SDL_Rect player2Rect = { player2.x, player2.y, PLAYER_WIDTH, PLAYER_HEIGHT };
        SDL_SetRenderDrawColor(renderer, 0, 0, 255, 255);
        SDL_RenderFillRect(renderer, &player2Rect);

        // Vẽ bóng
        SDL_Rect ballRect = { ball.x, ball.y, BALL_SIZE, BALL_SIZE };
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        SDL_RenderFillRect(renderer, &ballRect);

        // Cập nhật màn hình
        SDL_RenderPresent(renderer);

        // Tốc độ khung hình
        SDL_Delay(16);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
