#ifndef UTILS_H
#define UTILS_H

#include "../headers/menu/Game_over_menu.h"
#include "../headers/menu/Introduction.h"
#include "../headers/menu/Main_menu.h"
#include "../headers/menu/Pause_menu.h"
#include "../headers/menu/Game_menu.h"
#include <math.h>
#include <limits>
#include <SDL2/SDL.h>


// Constants
const float PI = 3.14159265358979;
const float MU = 0.05f; // friction coefficient
const float K = 20.0f; // stiffness coefficient
const float INF = std::numeric_limits<float>::infinity(); // infinite

// Screen dimensions
const int SCREEN_WIDTH = 1280;
const int SCREEN_HEIGHT = 720;
#define NUM_CHARACTER 3 
// Player dimensions
const int PLAYER_WIDTH = 20;
const int PLAYER_HEIGHT = 100;

// Ball stats
const float BALL_RAD = 0.05f;
const float BALL_MASS = 0.1f;

// Wind stats
const float COOLDOWN = 10.0f;
const float WIND_FORCE_MAX = 5.0f;
const float WIND_DURATION_MAX = 3.0f;
const int WIND_CHANCE = 10;
const int CHANGE_WIND_DIR_CHANCE =  5;

// Footballer stats
const int NUM_FOOTBALLER = 3; // per character
const float FOOTBALLER_RAD = 0.03f; // size
const float FOOTBALLER_MASS = 3.0f; // mass

// Character stats
const int NUM_CHAR = 3; // per team
const float CHAR_RAD = 0.05f; // size
const float MOVEMENT_FORCE = 0.3f;

// Rope length
const float ROPE_LENGTH = 0.3f;

const int CIRCLE_SEGMENTS = 1000;

float randRange(float min, float max);

void RenderRectangle(float rect_x, float rect_y, float width, float height);

void RenderCircle(float circ_x, float circ_y, float radius, int num_segments);

SDL_FPoint* getFootballerInitPos(float charX, float charY, float radius);

#endif // UTILS_H
