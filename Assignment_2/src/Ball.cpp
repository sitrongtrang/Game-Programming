#include "Ball.h"

Ball::Ball(float mass, float radius, SDL_FPoint initPos, SDL_FPoint initVel, SDL_FPoint initAcc) 
    : Physics(mass, initPos, initVel, initAcc), radius(radius) {}

void Ball::onCollision(Physics& other) {
    return;
} 

bool Ball::detectCollision(Physics& other) {
    return false;
}

void Ball::collideSurface(Physics& surface) {
    
    SDL_FPoint normal = surface.getNormal();

    float dotProduct = this->vel.x * normal.x + this->vel.y * normal.y;

    SDL_FPoint newVel = {this->vel.x - 2 * dotProduct * normal.x, this->vel.y - 2 * dotProduct * normal.y};
    this->setVel(newVel);
}

void Ball::draw() {
    RenderCircle(this->pos.x, this->pos.y, this->radius, CIRCLE_SEGMENTS);
}