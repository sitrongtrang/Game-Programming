#ifndef SURFACE_H
#define SURFACE_H

#include "Physics.h"

class Surface : public Physics {
private:
    float width, height; 
    SDL_FPoint normal;

public:
    Surface(SDL_FPoint initPos, SDL_FPoint normal, float width = SCREEN_WIDTH, float height = SCREEN_HEIGHT);

    float getWidth() const override;
    float getHeight() const override;
    SDL_FPoint getNormal() const override;

    bool detectCollision(Physics* other) override;
    void onCollision(Physics* other) override;

    void draw() override;
};

#endif