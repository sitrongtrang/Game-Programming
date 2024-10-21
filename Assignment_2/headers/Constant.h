#ifndef CONSTANT_H
#define CONSTANT_H

#include "imgui.h"
#include "imgui_impl_sdl2.h"
#include "imgui_impl_opengl3.h"
#include <SDL2/SDL.h>
#include <SDL2/SDL_opengl.h>
#include <SDL2/SDL_image.h>
#include <stdio.h>
#include <iostream>
#include <chrono>

extern std::chrono::time_point<std::chrono::steady_clock> startTime;
extern std::chrono::time_point<std::chrono::steady_clock> pauseTime;

const int countdownDuration = 60;
extern int pausedDuration;

const char CHARACTER_SPRITE[2][256] = {
    "./assets/Player/Slime-Sheet.png",
    "./assets/Player/SlimeBlue-Sheet.png"
};

const char FOOTBALLER_SPRITE[2][256] = {
    "./assets/Footballer/Footballer.png",
    "./assets/Footballer/Footballer2.png"
};
enum GameState
{
    INTRODUCTION,
    MAIN_MENU,
    NEW_GAME,
    PLAYING,
    PAUSED,
    GAME_OVER,
    QUIT
};

#endif // CONSTANT_H