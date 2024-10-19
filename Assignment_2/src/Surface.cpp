#include "Surface.h"

Surface::Surface(SDL_FPoint initPos, SDL_FPoint normal, float width, float height) 
    : Physics(INF, ColliderType::Rectangle, initPos), width(width), height(height), normal(normal) {}

float Surface::getWidth() const { return width; }
float Surface::getHeight() const {return height; }
    
SDL_FPoint Surface::getNormal() const { return normal; }

bool Surface::detectCollision(Physics* other) {
    if (this == other) return false;
    if (other->getColliderType() == ColliderType::Circle) {
        return sphere_rectCollision(other->getPos(), other->getRadius(), this->getPos(), this->getWidth(), this->getHeight());
    } else {
        return rect_rectCollision(this->getPos(), this->getWidth(), this->getHeight(), other->getPos(), other->getWidth(), other->getHeight());
    }
}

void Surface::onCollision(Physics* other) {
    return;
}

void Surface::draw() {
    RenderRectangle(this->pos.x, this->pos.y, this->width, this->height);
}