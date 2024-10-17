#ifndef WIND_H
#define WIND_H

#include <SDL2/SDL.h>

class Wind {
private:
    static Wind* instance;
    SDL_FPoint direction;     // Wind direction, each coordinate between -5 and 5
    float duration;           // Wind duration in seconds
    float timeLeft;           // Time left for the current wind effect
    float cooldown;           // 10-second cooldown after wind stops
    bool windActive;          // Whether wind is currently active

    Wind();

public:
    static Wind* getInstance();

    void update(float deltaTime);

    SDL_FPoint getDirection() const;
    bool isWindActive() const;
};

#endif
