#include "GameManager.h"
#include <stdio.h>

GameManager* GameManager::instance = nullptr;

GameManager::GameManager() {
    wind = Wind::getInstance();

    topEdge = new Surface({0.0f, 1.5f}, {0.0f, -1.0f}, SCREEN_WIDTH, 1.0f);
    bottomEdge = new Surface({0.0f, -1.5f}, {0.0f, 1.0f}, SCREEN_WIDTH, 1.0f);
    leftEdge = new Surface({-1.5f, 0.0f}, {1.0f, 0.0f}, 1.0f, SCREEN_HEIGHT);
    rightEdge = new Surface({1.5f, 0.0f}, {-1.0f, 0.0f}, 1.0f, SCREEN_HEIGHT);

    goalAEdges[0] = new Surface({-0.85f, 0.2f}, {0.0f, 1.0f}, 0.2f, 0.1f);
    goalAEdges[1] = new Surface({-0.95f, 0.0f}, {1.0f, 0.0f}, 0.1f, 0.4f);
    goalAEdges[2] = new Surface({-0.85f, -0.2f}, {0.0f, -1.0f}, 0.2f, 0.1f);

    goalBEdges[0] = new Surface({0.85f, 0.2f}, {0.0f, 1.0f}, 0.2f, 0.1f);
    goalBEdges[1] = new Surface({0.95f, 0.0f}, {-1.0f, 0.0f}, 0.1f, 0.4f);
    goalBEdges[2] = new Surface({0.85f, -0.2f}, {0.0f, -1.0f}, 0.2f, 0.1f);
}

GameManager* GameManager::getInstance() {
    if (!instance) {
        instance = new GameManager();

    }
    return instance;
}

void GameManager::newGame(InputManager* inputManager) {
    for (int i = 0; i < NUM_CHAR; i++) {
        SDL_FPoint pullerAPos = {-0.3f * (i % 2 + 1), (i-1) * 0.5f};
        SDL_FPoint pullerBPos = {0.3f * (i % 2 + 1), (i-1) * 0.5f};

       
        teamACharacters[i] = new Character(0, CHAR_RAD, pullerAPos);
        teamBCharacters[i] = new Character(1, CHAR_RAD, pullerBPos);

        SDL_FPoint* footballerAInitPos = getFootballerInitPos(pullerAPos.x, pullerAPos.y, -ROPE_LENGTH);
        SDL_FPoint* footballerBInitPos = getFootballerInitPos(pullerBPos.x, pullerBPos.y, ROPE_LENGTH);

        for (int j = 0; j < NUM_FOOTBALLER; j++) {
            teamAFootballers[i * NUM_FOOTBALLER + j] = new Footballer(0, FOOTBALLER_MASS, FOOTBALLER_RAD, ROPE_LENGTH, teamACharacters[i], footballerAInitPos[j]);
            teamACharacters[i]->setFootballer(j, teamAFootballers[i * NUM_FOOTBALLER + j]);
            teamBFootballers[i * NUM_FOOTBALLER + j] = new Footballer(1, FOOTBALLER_MASS, FOOTBALLER_RAD, ROPE_LENGTH, teamBCharacters[i], footballerBInitPos[j]);
            teamBCharacters[i]->setFootballer(j, teamBFootballers[i * NUM_FOOTBALLER + j]);

            physics[i * NUM_FOOTBALLER + j] = teamAFootballers[i * NUM_FOOTBALLER + j];
            physics[i * NUM_FOOTBALLER + j + NUM_FOOTBALLER * NUM_CHAR] = teamBFootballers[i * NUM_FOOTBALLER + j];
        }
    }

    ball = new Ball(BALL_MASS, BALL_RAD, {0.0f, 0.0f});
    physics[2 * NUM_FOOTBALLER * NUM_CHAR] = ball;

    physics[2 * NUM_FOOTBALLER * NUM_CHAR + 1] = topEdge;
    physics[2 * NUM_FOOTBALLER * NUM_CHAR + 2] = bottomEdge;
    physics[2 * NUM_FOOTBALLER * NUM_CHAR + 3] = leftEdge;
    physics[2 * NUM_FOOTBALLER * NUM_CHAR + 4] = rightEdge;

    for (int i = 0; i < 3; i++) {
        physics[2 * NUM_FOOTBALLER * NUM_CHAR + 5 + i] = goalAEdges[i];
        physics[2 * NUM_FOOTBALLER * NUM_CHAR + 8 + i] = goalBEdges[i];
    }

    inputManager->setCharacters(teamACharacters, teamBCharacters);
}

void GameManager::update(float deltaTime, int& score1, int& score2, SoundPlayer* soundPlayer) {
    
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

    for (int i = 0; i < 2 * NUM_FOOTBALLER * NUM_CHAR + 11; i++) {
        for (int j = 0; j < 2 * NUM_FOOTBALLER * NUM_CHAR + 11; j++) {
            if (physics[i]->detectCollision(physics[j])) {
                physics[i]->handleCollision(physics[j]);
                // printf("Object %d collides with object %d", i, j);
                if (physics[i] == ball) {
                    if (j < 2 * NUM_FOOTBALLER * NUM_CHAR) soundPlayer->playSound("kick");
                    if (physics[j] == goalAEdges[1] && ball->getPos().x < 0.9) {
                        ball->setPos({0.0f, 0.0f});
                        ball->setVel({0.0f, 0.0f});
                        ball->resetBall(RESET_BALL);
                        soundPlayer->playSound("goal");
                        score2++;
                    }
                    if (physics[j] == goalBEdges[1] && ball->getPos().x > -0.9) {
                        ball->setPos({0.0f, 0.0f});
                        ball->setVel({0.0f, 0.0f});
                        ball->resetBall(RESET_BALL);
                        soundPlayer->playSound("goal");
                        score1++;
                    }
                }
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
    if (index >= 0 && index < 2 * NUM_FOOTBALLER * NUM_CHAR + 11) {
        return physics[index];
    }
    return nullptr; 
}


Character** GameManager::getTeamACharacters() { return teamACharacters; }  
Character** GameManager::getTeamBCharacters() { return teamBCharacters; }
