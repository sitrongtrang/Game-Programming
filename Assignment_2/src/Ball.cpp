#include "Ball.h"

Ball::Ball(float mass, SDL_FPoint initPos, SDL_FPoint initVel, SDL_FPoint initAcc) 
    : Physics(mass, initPos, initVel, initAcc) {}

void Ball::onCollision(Physics& other) {
    
} 

bool Ball::detectCollision(Physics& other) {

}

void Ball::collideSurface(Physics& surface) {
    
    SDL_FPoint normal = surface.getNormal();

    float dotProduct = this->vel.x * normal.x + this->vel.y * normal.y;

    SDL_FPoint newVel = {this->vel.x - 2 * dotProduct * normal.x, this->vel.y - 2 * dotProduct * normal.y};
    this->setVel(newVel);
}