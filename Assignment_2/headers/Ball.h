#pragma once

#include "Physics.h"

class Ball : public Physics {
private:
    void reflect(SDL_FPoint normal);

public:
    Ball(float mass, SDL_FPoint initPos, SDL_FPoint initVel = {0.0f, 0.0f}, SDL_FPoint initAcc = {0.0f, 0.0f});

    bool isColliding(Physics& other) override;
    void onCollision(Physics& other) override;
    void collideWall(Physics& wall) override; // Reflect
}