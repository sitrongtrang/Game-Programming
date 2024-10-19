#ifndef PHYSICS_H
#define PHYSICS_H

#include <SDL2/SDL.h>
#include "utils.h"

enum class ColliderType {
    Rectangle,
    Circle,
};

class Physics
{
protected:
    float mass;     // Mass of the object
    ColliderType colliderType; 
    SDL_FPoint pos; // Position (2D vector)
    SDL_FPoint vel; // Velocity (2D vector)
    SDL_FPoint acc; // Acceleration (2D vector)

public:
    Physics(float mass, ColliderType colliderType, SDL_FPoint initPos, SDL_FPoint initVel = {0.0f, 0.0f}, SDL_FPoint initAcc = {0.0f, 0.0f});

    virtual ~Physics();

    void applyForce(SDL_FPoint force); // Affected by external forces (drag, wind, sand, etc.)

    virtual void update(float deltaTime); // Update position, velocity, acceleration

    virtual void draw() = 0;

    // Getters
    float getMass() const;
    ColliderType getColliderType() const;
    SDL_FPoint getPos() const;
    SDL_FPoint getVel() const;
    SDL_FPoint getAcc() const;
    virtual float getRadius() const;
    virtual float getWidth() const;
    virtual float getHeight() const;
    virtual SDL_FPoint getNormal() const;

    // Setters
    void setPos(SDL_FPoint newPos);
    void setVel(SDL_FPoint newVel);
    void setAcc(SDL_FPoint newAcc);

    // Collision
    virtual bool detectCollision(Physics* other) = 0; // Detect collision
    virtual void onCollision(Physics* other) = 0;     // Collision response (collide animation, event triggers, etc.)
    virtual void collideSurface(Physics* surface);    // Collide with surface
    void handleCollision(Physics* other);             // Update velocity after collision
};

#endif