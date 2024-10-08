#pragma once

#include <SDL2/SDL.h>

class Physics {
protected:
    float mass;        // Mass of the object
    SDL_FPoint pos;    // Position (2D vector)
    SDL_FPoint vel;    // Velocity (2D vector)
    SDL_FPoint acc;    // Acceleration (2D vector) 

public:

    Physics(float mass, SDL_FPoint initPos, SDL_FPoint initVel= {0.0f, 0.0f}, SDL_FPoint initAcc = {0.0f, 0.0f});

    virtual ~Physics();

    void applyForce(SDL_FPoint force); // Apply force from external forces (drag, wind, sand, etc.)

    void update(float deltaTime); // Update pos, vel

    // Getters
    float getMass() const;
    SDL_FPoint getPos() const;
    SDL_FPoint getVel() const;
    SDL_FPoint getAcc() const;

    // Setters
    void setPos(SDL_FPoint newPos);
    void setVel(SDL_FPoint newVel);
    void setAcc(SDL_FPoint newAcc);

    // Collision
    virtual bool isColliding(Physics& other) = 0; // Detect collision
    virtual void onCollision(Physics& other) = 0; // Collision response (animation, event triggers, etc.)
    virtual void collideWall(Physics& wall); // Collide with wall
    void handleCollision(Physics& other); // Update velocity after collision
};
