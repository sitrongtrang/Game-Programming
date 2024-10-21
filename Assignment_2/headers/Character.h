#ifndef CHARACTER_H
#define CHARACTER_H

#include <SDL2/SDL.h>
#include "utils.h"
#include "Spritesheet.h"
#include "Footballer.h"

class Character {
private:
    Footballer* footballers[NUM_FOOTBALLER];
    SDL_FPoint pos; 
    SDL_FPoint vel; 
    SDL_FPoint acc;
    float radius;

    Spritesheet sprSheet;
    
    

public:
    Character(int teamNum, float radius, SDL_FPoint initPos, SDL_FPoint initVel = {0.0f, 0.0f}, SDL_FPoint initAcc = {0.0f, 0.0f});

    ~Character();

    void update(float deltaTime);

    void applyRopeConstraint(SDL_FPoint force);

    SDL_FPoint getPos() const;
    SDL_FPoint getVel() const;
    SDL_FPoint getAcc() const;
    Footballer* getFootballer(int i) const;

    void setPos(SDL_FPoint newPos);
    void setVel(SDL_FPoint newVel);
    void setAcc(SDL_FPoint newAcc);
    void setFootballer(int i, Footballer* footballer);

    void draw();
    void drawRope();
};

#endif