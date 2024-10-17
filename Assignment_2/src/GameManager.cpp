#include "GameManager.h"

GameManager* GameManager::instance = nullptr;

GameManager::GameManager() {
    wind = Wind::getInstance();

    Footballer* teamAFootballers[NUM_FOOTBALLER * NUM_CHAR];
    Footballer* teamBFootballers[NUM_FOOTBALLER * NUM_CHAR];

    Character* teamACharacters[NUM_CHAR];  
    Character* teamBCharacters[NUM_CHAR];  

    for (int i = 0; i < NUM_FOOTBALLER; i++) {
        teamACharacters[i] = new Character({0.0f, 0.0f});
        teamBCharacters[i] = new Character({0.0f, 0.0f});
    }

    for (int i = 0; i < NUM_FOOTBALLER * NUM_CHAR; i++) {
        teamAFootballers[i] = new Footballer(300, 0.1f, ROPE_LENGTH, teamACharacters[i / NUM_FOOTBALLER], {0.0f, 0.0f});
        teamACharacters[i / NUM_FOOTBALLER]->setFootballer(i % NUM_FOOTBALLER, teamAFootballers[i]);
        teamBFootballers[i] = new Footballer(300, 0.1f, ROPE_LENGTH, teamBCharacters[i / NUM_FOOTBALLER], {0.0f, 0.0f});
        teamBCharacters[i / NUM_FOOTBALLER]->setFootballer(i % NUM_FOOTBALLER, teamBFootballers[i]);
    }
}

GameManager* GameManager::getInstance() {
    if (!instance) {
        instance = new GameManager();
    }
    return instance;
}

void GameManager::update(float deltaTime) {
    wind->update(deltaTime);

    for (Character* character : teamACharacters) {
        character->update(deltaTime); 
    }
    
    for (Character* character : teamBCharacters) {
        character->update(deltaTime);
    }

    for (Physics* object : physics) {
        object->update(deltaTime); 
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

