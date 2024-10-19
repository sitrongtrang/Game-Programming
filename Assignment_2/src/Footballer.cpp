#include "Footballer.h"
#include "Character.h"

Footballer::Footballer(float mass, float radius, float ropeLength, Character* puller, SDL_FPoint initPos, SDL_FPoint initVel, SDL_FPoint initAcc) 
    : Physics(mass, initPos, initVel, initAcc), radius(radius), obstructedX(false), obstructedY(false), ropeLength(ropeLength), puller(puller) {}

void Footballer::update(float deltaTime) {

    this->draw();
    this->applyRopeConstraint(); 
    this->applyForce(this->getFrictionForce());

    float newX = this->obstructedX? this->pos.x : this->pos.x + this->vel.x * deltaTime; // only change position if not obstructed
    float newY = this->obstructedY? this->pos.y : this->pos.y + this->vel.y * deltaTime; // only change position if not obstructed
    SDL_FPoint newPos = {newX, newY};
    this->setPos(newPos);

    SDL_FPoint newVel = {this->vel.x + this->acc.x * deltaTime, this->vel.y + this->acc.y * deltaTime};
    this->setVel(newVel);
    
    SDL_FPoint newAcc = {0.0f, 0.0f}; 
    this->setAcc(newAcc);

    this->setObstructedX(false);
    this->setObstructedY(false);
}

void Footballer::applyRopeConstraint() {

    SDL_FPoint direction = {this->puller->getPos().x - this->pos.x, this->puller->getPos().y - this->pos.y};

    float dist = sqrt(direction.x * direction.x + direction.y * direction.y);

    if (dist >= this->ropeLength) { // If the distance is greater than the rope length, apply tension
        direction.x /= dist;
        direction.y /= dist;

        // Calculate the stretch distance beyond the rope's length
        float stretch = dist - this->ropeLength;

        // Apply a force proportional to how much the rope is stretched (like Hooke's law)
        SDL_FPoint force = {K * stretch * direction.x, K * stretch * direction.y};

        // Apply the calculated force to pull the character
        this->applyForce(force);
        // this->puller->applyRopeConstraint(force);
    } 
}

SDL_FPoint Footballer::getFrictionForce() {
    if (this->vel.x == 0 && this->vel.y == 0)
        return {0, 0};
    float friction_magnitude = MU * this->mass * 9.8f; // F_friction = μ * m * g
    float friction_x = friction_magnitude * (-this->vel.x)/sqrt(this->vel.x * this->vel.x + this->vel.y * this->vel.y);
    float friction_y = friction_magnitude * (-this->vel.y)/sqrt(this->vel.x * this->vel.x + this->vel.y * this->vel.y);
    SDL_FPoint f_friction = {friction_x, friction_y};
    return f_friction;
}

bool Footballer::getObstructedX() { return this->obstructedX; }
bool Footballer::getObstructedY() { return this->obstructedY; }

void Footballer::setObstructedX(bool obsX) { this->obstructedX = obsX; }
void Footballer::setObstructedY(bool obsY) { this->obstructedY = obsY; }

void Footballer::onCollision(Physics& other) {
    return;
} 

bool Footballer::detectCollision(Physics& other) {
    return false;
}

void Footballer::collideSurface(Physics& surface) {

    SDL_FPoint normal = surface.getNormal();

    // Velocity along the normal
    float velAlongNormal = this->vel.x * normal.x + this->vel.y * normal.y;

    // If objects are moving away from each other, do nothing
    if (velAlongNormal >= 0) {
        return;
    }

    if (this->vel.x * normal.x < 0) {
        this->setObstructedX(true);
    }

    if (this->vel.y * normal.y < 0) {
        this->setObstructedY(true);
    }

}

void Footballer::draw() {
    RenderCircle(this->pos.x, this->pos.y, this->radius, CIRCLE_SEGMENTS);
}

