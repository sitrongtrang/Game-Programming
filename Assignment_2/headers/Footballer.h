#ifndef FOOTBALLER_H
#define FOOTBALLER_H

#include "Physics.h"
#include <math.h>

class Character;

class Footballer : public Physics {
protected:
    bool obstructedX, obstructedY; // footballer is obstructed in x/y direction
    float ropeLength;
    float radius;
    Character* puller; 
public:
    Footballer(float mass, float radius, float ropeLength, Character* puller, SDL_FPoint initPos, SDL_FPoint initVel={0.0f, 0.0f}, SDL_FPoint initAcc={0.0f, 0.0f});

    void update(float deltaTime) override;

    void applyRopeConstraint(); // physics for being dragged by the rope
    SDL_FPoint getFrictionForce(); // calculate friction force

    bool getObstructedX();
    bool getObstructedY();

    void setObstructedX(bool obsX);
    void setObstructedY(bool obsY);

    bool detectCollision(Physics& other) override;
    void onCollision(Physics& other) override;
    void collideSurface(Physics& surface) override;

    void draw() override;
};

#endif

