#include "GameManager.h"
#include <stdio.h>

GameManager* GameManager::instance = nullptr;

GameManager::GameManager() {
    wind = Wind::getInstance();

    for (int i = 0; i < NUM_CHAR; i++) {
        SDL_FPoint pullerAPos = {-0.3f * (i % 2 + 1), (i-1) * 0.5f};
        SDL_FPoint pullerBPos = {0.3f * (i % 2 + 1), (i-1) * 0.5f};

       
        teamACharacters[i] = new Character(CHAR_RAD, pullerAPos);
        teamBCharacters[i] = new Character(CHAR_RAD, pullerBPos);

        SDL_FPoint* footballerAInitPos = getFootballerInitPos(pullerAPos.x, pullerAPos.y, -ROPE_LENGTH);
        SDL_FPoint* footballerBInitPos = getFootballerInitPos(pullerBPos.x, pullerBPos.y, ROPE_LENGTH);

        for (int j = 0; j < NUM_FOOTBALLER; j++) {
            teamAFootballers[i * NUM_FOOTBALLER + j] = new Footballer(FOOTBALLER_MASS, FOOTBALLER_RAD, ROPE_LENGTH, teamACharacters[i], footballerAInitPos[j]);
            teamACharacters[i]->setFootballer(j, teamAFootballers[i * NUM_FOOTBALLER + j]);
            teamBFootballers[i * NUM_FOOTBALLER + j] = new Footballer(FOOTBALLER_MASS, FOOTBALLER_RAD, ROPE_LENGTH, teamBCharacters[i], footballerBInitPos[j]);
            teamBCharacters[i]->setFootballer(j, teamBFootballers[i * NUM_FOOTBALLER + j]);

            physics[i * NUM_FOOTBALLER + j] = teamAFootballers[i * NUM_FOOTBALLER + j];
            physics[i * NUM_FOOTBALLER + j + NUM_FOOTBALLER * NUM_CHAR] = teamBFootballers[i * NUM_FOOTBALLER + j];
        }
    }

    ball = new Ball(BALL_MASS, BALL_RAD, {0.0f, 0.0f});
    physics[2 * NUM_FOOTBALLER * NUM_CHAR] = ball;

    topEdge = new Surface({0.0f, 1.5f}, {0.0f, -1.0f}, SCREEN_WIDTH, 1.0f);
    bottomEdge = new Surface({0.0f, -1.5f}, {0.0f, 1.0f}, SCREEN_WIDTH, 1.0f);
    leftEdge = new Surface({-1.5f, 0.0f}, {1.0f, 0.0f}, 1.0f, SCREEN_HEIGHT);
    rightEdge = new Surface({1.5f, 0.0f}, {-1.0f, 0.0f}, 1.0f, SCREEN_HEIGHT);

    physics[2 * NUM_FOOTBALLER * NUM_CHAR + 1] = topEdge;
    physics[2 * NUM_FOOTBALLER * NUM_CHAR + 2] = bottomEdge;
    physics[2 * NUM_FOOTBALLER * NUM_CHAR + 3] = leftEdge;
    physics[2 * NUM_FOOTBALLER * NUM_CHAR + 4] = rightEdge;
}

GameManager* GameManager::getInstance() {
    if (!instance) {
        instance = new GameManager();

    }
    return instance;
}

void GameManager::update(float deltaTime) {
    
    wind->update(deltaTime);
    ball->applyForce(wind->getDirection());
    
    for (Character* character : teamACharacters) {
        character->update(deltaTime); 
    }
    
    for (Character* character : teamBCharacters) {
        character->update(deltaTime);
    }

    for (Physics* object : physics) {
        object->update(deltaTime); 
    }

    for (Physics* object : physics) {
        for (Physics* other : physics) {
            if (object->detectCollision(other)) {
                object->handleCollision(other);
            }
        }
    }
}

Character* GameManager::getTeamACharacter(int index) const {
    if (index >= 0 && index < NUM_CHAR) {
        return teamACharacters[index];
    }
    return nullptr; 
}

Character* GameManager::getTeamBCharacter(int index) const {
    if (index >= 0 && index < NUM_CHAR) {
        return teamBCharacters[index];
    }
    return nullptr;
}

Physics* GameManager::getPhysicsObject(int index) const {
    if (index >= 0 && index < MAX_PHYSICS_OBJECTS) {
        return physics[index];
    }
    return nullptr; 
}

Character** GameManager::getTeamACharacters() { return teamACharacters; }  
Character** GameManager::getTeamBCharacters() { return teamBCharacters; }
