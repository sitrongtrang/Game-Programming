#pragma once

#include "Physics.h"

class Footballer : public Physics {
public:
    Footballer(float mass, SDL_FPoint initPos, SDL_FPoint initVel = {0.0f, 0.0f}, SDL_FPoint initAcc = {0.0f, 0.0f});

    bool isColliding(Physics& other) override;
    void onCollision(Physics& other) override;
}

