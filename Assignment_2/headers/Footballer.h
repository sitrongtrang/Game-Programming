#pragma once

#include "Physics.h"

class Footballer : public Physics {
protected:
    bool obstructedX, obstructedY; // footballer is obstructed in x/y direction
    float ropeLength;
public:
    Footballer(float mass, SDL_FPoint initPos, SDL_FPoint initVel={0.0f, 0.0f}, SDL_FPoint initAcc={0.0f, 0.0f}, float ropeLength);

    void update(float deltaTime) override;

    void applyRopeConstraint(SDL_FPoint source) // physics for being dragged by the rope
    SDL_FPoint getFrictionForce(); // calculate friction force

    bool getObstructedX();
    bool getObstructedY();

    void setObstructedX(bool obsX);
    void setObstructedY(bool obsY);

    bool detectCollision(Physics& other) override;
    void onCollision(Physics& other) override;
    void collideSurface(Physics& surface) override;
}

