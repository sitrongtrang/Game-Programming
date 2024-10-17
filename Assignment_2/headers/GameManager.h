#ifndef GAMEMANAGER_H
#define GAMEMANAGER_H

#include "Wind.h"         
#include "Character.h"  
#include "Footballer.h"
#include "Physics.h"
#include "utils.h"

const int MAX_PHYSICS_OBJECTS = 20; // Maximum number of physics objects

class GameManager {
private:
    static GameManager* instance;

    Character* teamACharacters[NUM_CHAR];  
    Character* teamBCharacters[NUM_CHAR];  
    Physics* physics[MAX_PHYSICS_OBJECTS]; // Physics objects

    Wind* wind; 

    GameManager();

public:
    static GameManager* getInstance();

    void update(float deltaTime);

    Character* getTeamACharacter(int index) const;
    Character* getTeamBCharacter(int index) const;
    Physics* getPhysicsObject(int index) const;

    int getPhysicsObjectCount() const { return MAX_PHYSICS_OBJECTS; }

    Wind* getWind() const { return wind; }
};

#endif // GAMEMANAGER_H
