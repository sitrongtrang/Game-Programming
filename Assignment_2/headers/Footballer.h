#pragma once

#include "Physics.h"

class Footballer : public Physics {
protected:
    bool obstructedX, obstructedY; // footballer is obstructed in x/y direction
public:
    Footballer(float mass, SDL_FPoint initPos, SDL_FPoint initVel={0.0f, 0.0f}, SDL_FPoint initAcc={0.0f, 0.0f});

    void update(float deltaTime) override;

    void applyRopeConstraint(SDL_FPoint source, float ropeLength) // physics for being dragged by the rope

    bool getObstructedX();
    bool getObstructedY();

    void setObstructedX(bool obs);
    void setObstructedY(bool obs);

    bool detectCollision(Physics& other) override;
    void onCollision(Physics& other) override;
    void collideSurface(Physics& surface) override;
}

