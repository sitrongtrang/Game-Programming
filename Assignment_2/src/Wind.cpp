#include "wind.h"
#include <cstdlib>  
#include <ctime>   
#include "utils.h" 

Wind* Wind::instance = nullptr;

Wind::Wind() : direction({0, 0}), duration(0), timeLeft(0), cooldown(0), windActive(false) {
    std::srand(static_cast<unsigned int>(std::time(nullptr)));
}

Wind* Wind::getInstance() {
    if (!instance) {
        instance = new Wind();
    }
    return instance;
}

void Wind::update(float deltaTime) {
    if (cooldown > 0) {
        // Cooldown is in effect, decrement cooldown time
        cooldown -= deltaTime;
    } else if (windActive) {
        // Wind is currently active, decrement the duration timer
        timeLeft -= deltaTime;

        if (rand() % 100 < CHANGE_WIND_DIR_CHANCE) { // chance of wind changing direction
            direction.x = randRange(-WIND_FORCE_MAX, WIND_FORCE_MAX);
            direction.y = randRange(-WIND_FORCE_MAX, WIND_FORCE_MAX);
        }

        if (timeLeft <= 0) {
            // Wind duration has expired, stop the wind
            windActive = false;
            direction = {0.0f, 0.0f};
            cooldown = COOLDOWN;  // Start cooldown
        }
    } else {
        // No wind is active and no cooldown is in effect, randomly decide to create wind
        if (rand() % 100 < WIND_CHANCE) { // chance of creating wind
            direction.x = randRange(-WIND_FORCE_MAX, WIND_FORCE_MAX);
            direction.y = randRange(-WIND_FORCE_MAX, WIND_FORCE_MAX);
            duration = randRange(1.0f, WIND_DURATION_MAX);
            timeLeft = duration;
            windActive = true; // Activate wind
        }
    }
}
