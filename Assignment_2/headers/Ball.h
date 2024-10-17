#ifndef BALL_H
#define BALL_H

#include "Physics.h"

class Ball : public Physics {
private:
    float radius;
public:
    Ball(float mass, float radius, SDL_FPoint initPos, SDL_FPoint initVel={0.0f, 0.0f}, SDL_FPoint initAcc={0.0f, 0.0f});

    bool detectCollision(Physics& other) override;
    void onCollision(Physics& other) override;
    void collideSurface(Physics& surface) override; 

    void draw() override;
};

#endif