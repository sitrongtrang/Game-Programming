#pragma once

#include "Physics.h"

class Surface : public Physics {
public:
    Surface(SDL_FPoint initPos);

    // Depends on the colliding box of the object
    // TODO: implement after colliding boxes are done
    SDL_FPoint getNormal();

    bool detectCollision(Physics& other) override;
    void onCollision(Physics& other) override;
}