#ifndef CONSTANT_H
#define CONSTANT_H

#include "imgui.h"
#include "imgui_impl_sdl2.h"
#include "imgui_impl_opengl3.h"
#include <SDL.h>
#include <SDL_opengl.h>
#include <SDL_image.h>
#include <stdio.h>
#include <chrono>

const int SCREEN_WIDTH = 1280;
const int SCREEN_HEIGHT = 720;
const int PLAYER_WIDTH = 20;
const int PLAYER_HEIGHT = 100;
const int BALL_SIZE = 15;

extern std::chrono::time_point<std::chrono::steady_clock> startTime;
extern std::chrono::time_point<std::chrono::steady_clock> pauseTime;

const int countdownDuration = 60;
extern int pausedDuration;

enum GameState
{
    INTRODUCTION,
    MAIN_MENU,
    PLAYING,
    PAUSED,
    GAME_OVER,
    QUIT
};

#endif // CONSTANT_H