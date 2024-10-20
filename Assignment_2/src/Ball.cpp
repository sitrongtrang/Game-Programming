#include "Ball.h"

Ball::Ball(float mass, float radius, SDL_FPoint initPos, SDL_FPoint initVel, SDL_FPoint initAcc) 
    : Physics(mass, ColliderType::Circle, initPos, initVel, initAcc), radius(radius),
    sprSheet("./assets/Ball/MyBall-Sheet.png", 1, 4, 4, 0.1f)  {
        std::cerr <<"Flag " <<std::endl;
        sprSheet.select_sprite(0, 0);
    }


float Ball::getRadius() const { return this->radius; }

void Ball::onCollision(Physics* other) {
    return;
} 

bool Ball::detectCollision(Physics* other) {
    if (this == other) return false;
    if (other->getColliderType() == ColliderType::Circle) {
        return sphere_sphereCollision(this->pos, this->radius, other->getPos(), other->getRadius());
    } else {
        return sphere_rectCollision(this->pos, this->radius, other->getPos(), other->getWidth(), other->getHeight());
    }
    // return false;
}

void Ball::collideSurface(Physics* surface) {
    
    SDL_FPoint normal = surface->getNormal();

    float dotProduct = this->vel.x * normal.x + this->vel.y * normal.y;

    SDL_FPoint newVel = {this->vel.x - 2 * dotProduct * normal.x, this->vel.y - 2 * dotProduct * normal.y};
    this->setVel(newVel);
}

void Ball::draw() {
    //RenderCircle(this->pos.x, this->pos.y, this->radius, CIRCLE_SEGMENTS);
    sprSheet.draw(this->pos.x, this->pos.y, this->radius *2, this->radius *2);
}