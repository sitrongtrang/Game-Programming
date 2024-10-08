#include "Ball.h"

Ball::Ball(float mass, SDL_FPoint initPos, SDL_FPoint initVel, SDL_FPoint initAcc) 
    : Physics(mass, initPos, initVel, initAcc) {}

void Ball::onCollision(Physics& other) {
    
} 

bool Ball::isColliding(Physics& other) {

}

void Ball::collideWall(Physics& wall) {
    reflect(wall.getNormal());
}

void Ball::reflect(SDL_FPoint normal){
    float dotProduct = vel.x * normal.x + vel.y * normal.y;

    SDL_FPoint newVel = {vel.x - 2 * dotProduct * normal.x, vel.y - 2 * dotProduct * normal.y};
    setVel(newVel);
}