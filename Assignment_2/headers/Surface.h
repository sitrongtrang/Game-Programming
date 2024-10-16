#ifndef SURFACE_H
#define SURFACE_H

#include "Physics.h"

class Surface : public Physics {
public:
    Surface(SDL_FPoint initPos);
    
    SDL_FPoint getNormal() override;

    bool detectCollision(Physics& other) override;
    void onCollision(Physics& other) override;
};

#endif