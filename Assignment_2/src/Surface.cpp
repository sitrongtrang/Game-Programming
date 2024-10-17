#include "Surface.h"

Surface::Surface(float width, float height, SDL_FPoint initPos, SDL_FPoint normal) 
    : Physics(1000000, initPos), width(width), height(height), normal(normal) {}

    // Depends on the colliding box of the object
    // TODO: implement after colliding boxes are done

float Surface::getWidth() const { return width; }
float Surface::getHeight() const {return height; }
    
SDL_FPoint Surface::getNormal() const { return normal; }

bool Surface::detectCollision(Physics& other) {
    return false;
}

void Surface::onCollision(Physics& other) {
    return;
}

void Surface::draw() {
    RenderRectangle(this->pos.x, this->pos.y, SCREEN_WIDTH, SCREEN_HEIGHT);
}