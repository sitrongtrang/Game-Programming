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
    drawRope();
    sprSheet.draw(this->pos.x, this->pos.y, this->radius *2, this->radius *2);
    
}

void Character::drawRope() {
    glColor3f(0.8f, 0.6f, 0.2f);  // Rope color (brownish)
    glLineWidth(4.0f);  // Thicker line for rope effect

    for (int i = 0; i < NUM_FOOTBALLER; i++) {
        if (footballers[i] != nullptr) {
            // Get footballer's position and adjust for center
            SDL_FPoint footballerPos = footballers[i]->getPos();
            float footballerRadius = footballers[i]->getRadius();  // Assuming Footballer has radius

            // Adjust positions to center of character and footballer
            float characterCenterX = this->pos.x + this->radius;
            float characterCenterY = this->pos.y + this->radius;

            float footballerCenterX = footballerPos.x + footballerRadius;
            float footballerCenterY = footballerPos.y + footballerRadius;

            // Let's divide the line into segments to create a rope-like look
            const int segments = 20;  // More segments for smoother rope
            float dx = (footballerCenterX - characterCenterX) / segments;
            float dy = (footballerCenterY - characterCenterY) / segments;

            glBegin(GL_LINE_STRIP);  // Continuous line

            for (int j = 0; j <= segments; j++) {
                float segmentX = characterCenterX + j * dx;
                float segmentY = characterCenterY + j * dy;

                // Optional wave effect
                float waveAmplitude = 0.006f;
                float waveFrequency = 5.0f;
                float offset = sin(j * waveFrequency) * waveAmplitude;

                // Apply wave effect to Y axis for horizontal ropes, X axis for vertical ropes
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

    // Reset to default settings
    glColor3f(1.0f, 1.0f, 1.0f);  // Reset color
    glLineWidth(1.0f);  // Reset line width
}
