#ifndef SURFACE_H
#define SURFACE_H

#include "Physics.h"

class Surface : public Physics {
private:
    float width, height; 
    SDL_FPoint normal;

public:
    Surface(float width, float height, SDL_FPoint initPos, SDL_FPoint normal);

    float getWidth() const;
    float getHeight() const;
    SDL_FPoint getNormal() const override;

    bool detectCollision(Physics& other) override;
    void onCollision(Physics& other) override;

    void draw() override;
};

#endif