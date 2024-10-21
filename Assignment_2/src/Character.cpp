#include "Character.h"
#include <iostream>


Character::Character(int teamNum, float radius, SDL_FPoint initPos, SDL_FPoint initVel, SDL_FPoint initAcc) 
    : radius(radius), pos(initPos), vel(initVel), acc(initAcc),
        sprSheet(CHARACTER_SPRITE[teamNum], 1, 5, 5, 0.1f) {
        
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
    drawRope();
    sprSheet.draw(this->pos.x, this->pos.y, this->radius *2, this->radius *2);
    
}

void Character::drawRope() {
    glColor3f(0.8f, 0.6f, 0.2f);  
    glLineWidth(4.0f);  

    for (int i = 0; i < NUM_FOOTBALLER; i++) {
        if (footballers[i] != nullptr) {
           
            SDL_FPoint footballerPos = footballers[i]->getPos();
            float footballerRadius = footballers[i]->getRadius(); 

            // Adjust positions to center of character and footballer
            float characterCenterX = this->pos.x + this->radius;
            float characterCenterY = this->pos.y + this->radius;

            float footballerCenterX = footballerPos.x + footballerRadius;
            float footballerCenterY = footballerPos.y + footballerRadius;

           
            const int segments = 20;  
            float dx = (footballerCenterX - characterCenterX) / segments;
            float dy = (footballerCenterY - characterCenterY) / segments;

            glBegin(GL_LINE_STRIP);  

            for (int j = 0; j <= segments; j++) {
                float segmentX = characterCenterX + j * dx;
                float segmentY = characterCenterY + j * dy;

               
                float waveAmplitude = 0.006f;
                float waveFrequency = 5.0f;
                float offset = sin(j * waveFrequency) * waveAmplitude;

                
                if (abs(footballerCenterX - characterCenterX) > abs(footballerCenterY - characterCenterY)) {
                    segmentY += offset;
                } else {
                    segmentX += offset;
                }

                glVertex2f(segmentX, segmentY);
            }
            glEnd();
        }
    }

  
    glColor3f(1.0f, 1.0f, 1.0f);  
    glLineWidth(1.0f);  
}
