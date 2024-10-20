#ifndef GAMEMANAGER_H
#define GAMEMANAGER_H

#include "Wind.h"    
#include "Ball.h"    
#include "Surface.h" 
#include "Character.h"  
#include "Footballer.h"
#include "Physics.h"
#include "inputManager.h"
#include "utils.h"

const int MAX_PHYSICS_OBJECTS = 20; // Maximum number of physics objects

class GameManager {
private:
    static GameManager* instance;

    Ball* ball;

    Character* teamACharacters[NUM_CHAR];  
    Character* teamBCharacters[NUM_CHAR];  
    Footballer* teamAFootballers[NUM_FOOTBALLER * NUM_CHAR];
    Footballer* teamBFootballers[NUM_FOOTBALLER * NUM_CHAR];
    Physics* physics[2 * NUM_FOOTBALLER * NUM_CHAR + 5]; 

    Surface* topEdge, *bottomEdge, *leftEdge, *rightEdge;

    Wind* wind; 

    GameManager();

public:
    static GameManager* getInstance();

    void update(float deltaTime);

    void newGame(InputManager* inputManager);

    Character* getTeamACharacter(int index) const;
    Character* getTeamBCharacter(int index) const;
    Physics* getPhysicsObject(int index) const;
    Character** getTeamACharacters();  
    Character** getTeamBCharacters();
    int getPhysicsObjectCount() const { return MAX_PHYSICS_OBJECTS; }

    Wind* getWind() const { return wind; }
};

#endif // GAMEMANAGER_H
