#include "Character.h"
#include <iostream>


Character::Character(float radius, SDL_FPoint initPos, SDL_FPoint initVel, SDL_FPoint initAcc) 
    : radius(radius), pos(initPos), vel(initVel), acc(initAcc),
        sprSheet("./assets/Player/Slime-Sheet.png", 1, 5, 5, 0.1f) {
        
        for (int i = 0; i < NUM_FOOTBALLER; i++) {
            footballers[i] = nullptr;
        }

        // for test only
        sprSheet.select_sprite(4, 0);
    

    }

Character::~Character() {}

void Character::update(float deltaTime)
{
   
    this->draw();
    
    sprSheet.update(deltaTime);
     
    SDL_FPoint newPos = {this->pos.x + this->vel.x * deltaTime, this->pos.y + this->vel.y * deltaTime};
    this->setPos(newPos);

    SDL_FPoint newVel = {this->vel.x + this->acc.x * deltaTime, this->vel.y + this->acc.y * deltaTime};
    this->setVel(newVel);

    SDL_FPoint newAcc = {0.0f, 0.0f}; 
    this->setAcc(newAcc);
}

void Character::applyRopeConstraint(SDL_FPoint force) {
    this->setAcc({acc.x - force.x / 10, acc.y - force.y / 10});
}

SDL_FPoint Character::getPos() const { return pos; }
SDL_FPoint Character::getVel() const { return vel; }
SDL_FPoint Character::getAcc() const { return acc; }
Footballer* Character::getFootballer(int i) const { return footballers[i]; }

void Character::setPos(SDL_FPoint newPos) { 
    if (newPos.x > -1.0f + radius && newPos.x < 1.0f - radius) {
        pos.x = newPos.x;
    }

    if (newPos.y > -1.0f + radius && newPos.y < 1.0f - radius) {
        pos.y = newPos.y;
    }
}
void Character::setVel(SDL_FPoint newVel) { vel = newVel; }
void Character::setAcc(SDL_FPoint newAcc) { acc = newAcc; }
void Character::setFootballer(int i, Footballer* footballer) {
    footballers[i] = footballer;
}

void Character::draw() {
    
    sprSheet.draw(this->pos.x, this->pos.y, this->radius *2, this->radius *2);
}
