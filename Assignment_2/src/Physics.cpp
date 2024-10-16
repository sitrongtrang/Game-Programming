#include "Physics.h"
#include <math.h>

Physics::Physics(float mass, SDL_FPoint initPos, SDL_FPoint initVel, SDL_FPoint initAcc)
    : mass(mass), pos(initPos), vel(initVel), acc(initAcc) {}

Physics::~Physics() {}

void Physics::applyForce(SDL_FPoint force)
{
    SDL_FPoint newAcc = {this->acc.x + force.x / this->mass, this->acc.y + force.y / this->mass};
    this->setAcc(newAcc);
}

void Physics::update(float deltaTime)
{
    SDL_FPoint newPos = {this->pos.x + this->vel.x * deltaTime, this->pos.y + this->vel.y * deltaTime};
    this->setPos(newPos);

    SDL_FPoint newVel = {this->vel.x + this->acc.x * deltaTime, this->vel.y + this->acc.y * deltaTime};
    this->setVel(newVel);

    SDL_FPoint newAcc = {0.0f, 0.0f}; // reset every frame, if force is contiuous, reapplied next frame
    this->setAcc(newAcc);
}

float Physics::getMass() const { return this->mass; }
SDL_FPoint Physics::getPos() const { return this->pos; }
SDL_FPoint Physics::getVel() const { return this->vel; }
SDL_FPoint Physics::getAcc() const { return this->acc; }
SDL_FPoint Physics::getNormal() const { return {0, 0}; }

void Physics::setPos(SDL_FPoint newPos) { this->pos = newPos; }
void Physics::setVel(SDL_FPoint newVel) { this->vel = newVel; }
void Physics::setAcc(SDL_FPoint newAcc) { this->acc = newAcc; }

void Physics::handleCollision(Physics &other)
{

    if (other.getMass() == 1000000)
    {
        this->collideSurface(other);
    }

    if (this->mass == 1000000)
    {
        return;
    }

    SDL_FPoint normal = {other.getPos().x - this->pos.x, other.getPos().y - this->pos.y};
    float normalLength = std::sqrt(normal.x * normal.x + normal.y * normal.y);
    normal.x /= normalLength;
    normal.y /= normalLength;

    SDL_FPoint relVel = {other.getVel().x - this->vel.x, other.getVel().y - this->vel.y};

    // Velocity along the normal
    float velAlongNormal = relVel.x * normal.x + relVel.y * normal.y;

    // If objects are moving away from each other, do nothing
    if (velAlongNormal >= 0)
    {
        return;
    }

    // Calculate restitution (perfectly elastic collision => restitution = 1)
    float restitution = 1.0f;

    // Calculate impulse scalar
    float impulseScalar = -(1 + restitution) * velAlongNormal;
    impulseScalar /= (1 / this->mass + 1 / other.getMass());

    // Apply impulse
    SDL_FPoint impulse = {impulseScalar * normal.x, impulseScalar * normal.y};

    SDL_FPoint newVel = {this->vel.x - (1 / this->mass) * impulse.x, this->vel.y - (1 / this->mass) * impulse.y};
    this->setVel(newVel);

    SDL_FPoint otherNewVel = {other.getVel().x + (1 / other.getMass()) * impulse.x, other.getVel().y + (1 / other.getMass()) * impulse.y};
    other.setVel(otherNewVel);

    this->onCollision(other);
    other.onCollision(*this);
}

void Physics::collideSurface(Physics &surface)
{
    return;
}
