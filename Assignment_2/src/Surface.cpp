#include "Surface.h"

Surface::Surface(SDL_FPoint initPos) 
    : Physics(std::numeric_limits<float>::infinity(), initPos) {}

    // Depends on the colliding box of the object
    // TODO: implement after colliding boxes are done
    
SDL_FPoint Surface::getNormal() {
    
}

bool Surface::detectCollision(Physics& other) {

}

void Surface::onCollision(Physics& other) {

}