#ifndef CHARACTER_H
#define CHARACTER_H

#include <SDL2/SDL.h>
#include "Footballer.h"

#define NUM_FOOTBALLER 3

class Character {
private:
    Footballer* footballers[NUM_FOOTBALLER];
    SDL_FPoint pos; 
    SDL_FPoint vel; 

public:
    Character(SDL_FPoint initPos, SDL_FPoint initVel = {0.0f, 0.0f});

    ~Character();

    void update(float deltaTime);

    SDL_FPoint getPos() const;
    SDL_FPoint getVel() const;
    Footballer getFootballer(int i) const;

    void setPos(SDL_FPoint newPos);
    void setVel(SDL_FPoint newVel);
    void applyAcc(SDL_FPoint force);
};

#endif