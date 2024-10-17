#ifndef UTILS_H
#define UTILS_H

// Screen dimensions
const int SCREEN_WIDTH = 1280;
const int SCREEN_HEIGHT = 720;

// Player dimensions
const int PLAYER_WIDTH = 20;
const int PLAYER_HEIGHT = 100;

// Ball size
const int BALL_SIZE = 15;

const float COOLDOWN = 10.0f;
const float WIND_FORCE_MAX = 5.0f;
const float WIND_DURATION_MAX = 3.0f;
const int WIND_CHANCE = 10;
const int CHANGE_WIND_DIR_CHANCE =  5;

float randRange(float min, float max);

#endif // UTILS_H
