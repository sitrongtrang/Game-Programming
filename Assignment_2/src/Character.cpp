#include "Character.h"

Character::Character(SDL_FPoint initPos, SDL_FPoint initVel, SDL_FPoint initAcc) 
    : pos(initPos), vel(initVel), acc(initAcc) {
        for (int i = 0; i < NUM_FOOTBALLER; i++) {
            footballers[i] = nullptr;
        }
    }

Character::~Character() {}

void Character::update(float deltaTime)
{
    SDL_FPoint newPos = {this->pos.x + this->vel.x * deltaTime, this->pos.y + this->vel.y * deltaTime};
    this->setPos(newPos);

    SDL_FPoint newVel = {this->vel.x + this->acc.x * deltaTime, this->vel.y + this->acc.y * deltaTime};
    this->setVel(newVel);

    SDL_FPoint newAcc = {0.0f, 0.0f}; 
    this->setAcc(newAcc);
}

SDL_FPoint Character::getPos() const { return pos; }
SDL_FPoint Character::getVel() const { return vel; }
Footballer* Character::getFootballer(int i) const { return footballers[i]; }

void Character::setPos(SDL_FPoint newPos) { 
    if (newPos.x < SCREEN_WIDTH && newPos.x > 0) {
        pos.x = newPos.x;
    }

    if (newPos.y < SCREEN_WIDTH && newPos.y > 0) {
        pos.y = newPos.y;
    }
}
void Character::setVel(SDL_FPoint newVel) { vel = newVel; }
void Character::setAcc(SDL_FPoint newAcc) { this->acc = newAcc; }
void Character::setFootballer(int i, Footballer* footballer) {
    footballers[i] = footballer;
}
