#include "Surface.h"

Surface::Surface(SDL_FPoint initPos) 
    : Physics(std::numeric_limits<float>::infinity(), initPos) {}

SDL_FPoint Surface::getNormal() {
    
}

bool Surface::detectCollision(Physics& other) {

}

void Surface::onCollision(Physics& other) {

}