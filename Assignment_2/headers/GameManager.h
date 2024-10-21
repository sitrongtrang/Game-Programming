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

class GameManager {
private:
    static GameManager* instance;

    Ball* ball;

    Character* teamACharacters[NUM_CHAR];  
    Character* teamBCharacters[NUM_CHAR];  
    Footballer* teamAFootballers[NUM_FOOTBALLER * NUM_CHAR];
    Footballer* teamBFootballers[NUM_FOOTBALLER * NUM_CHAR];
    Physics* physics[2 * NUM_FOOTBALLER * NUM_CHAR + 11]; 

    Surface* topEdge, *bottomEdge, *leftEdge, *rightEdge;

    Surface* goalAEdges[3], *goalBEdges[3];

    Wind* wind; 

    SDL_Renderer *renderer;

    GameManager();

public:
    static GameManager* getInstance();

    void update(float deltaTime, int& score1, int& score2);
    SDL_Surface* GetSurf();

    void newGame(InputManager* inputManager);

    Character* getTeamACharacter(int index) const;
    Character* getTeamBCharacter(int index) const;
    Physics* getPhysicsObject(int index) const;
    Character** getTeamACharacters();  
    Character** getTeamBCharacters();
    int getPhysicsObjectCount() const;
    void ballInGoal(int& score1, int& score2);

    Wind* getWind() const { return wind; }
};

#endif // GAMEMANAGER_H
