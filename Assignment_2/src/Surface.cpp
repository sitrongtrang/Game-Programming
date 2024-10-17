#include "Surface.h"

Surface::Surface(SDL_FPoint initPos) 
    : Physics(1000000, initPos) {}

    // Depends on the colliding box of the object
    // TODO: implement after colliding boxes are done
    
SDL_FPoint Surface::getNormal() const {
    SDL_FPoint normal = {0, 1};
    return normal;
}

bool Surface::detectCollision(Physics& other) {
    return false;
}

void Surface::onCollision(Physics& other) {
    return;
}