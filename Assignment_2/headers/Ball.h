#ifndef BALL_H
#define BALL_H

#include "Physics.h"
#include "Spritesheet.h"
class Ball : public Physics {
private:
    float radius;
    Spritesheet sprSheet;
    float newBall;

public:
    Ball(float mass, float radius, SDL_FPoint initPos, SDL_FPoint initVel={0.0f, 0.0f}, SDL_FPoint initAcc={0.0f, 0.0f});

    float getRadius() const override;

    bool detectCollision(Physics* other) override;
    void onCollision(Physics* other) override;
    void collideSurface(Physics* surface) override; 

    void resetBall(float resetBall);

    void draw() override;
    void update(float deltatime) override;
};

#endif