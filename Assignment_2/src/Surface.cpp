#include "Surface.h"

Surface::Surface(SDL_FPoint initPos, SDL_FPoint normal, float width, float height) 
    : Physics(INF, initPos), width(width), height(height), normal(normal) {}

float Surface::getWidth() const { return width; }
float Surface::getHeight() const {return height; }
    
SDL_FPoint Surface::getNormal() const { return normal; }

bool Surface::detectCollision(Physics* other) {
    return false;
}

void Surface::onCollision(Physics* other) {
    return;
}

void Surface::draw() {
    RenderRectangle(this->pos.x, this->pos.y, this->width, this->height);
}