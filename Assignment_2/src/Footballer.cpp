#include "Footballer.h"

Footballer::Footballer(float mass, SDL_FPoint initPos, SDL_FPoint initVel, SDL_FPoint initAcc) 
    : Physics(mass, initPos, initVel, initAcc) {}

void Footballer::onCollision(Physics& other) {
    
} 

bool Footballer::isColliding(Physics& other) {

}

