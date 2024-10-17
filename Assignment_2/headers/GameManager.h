#ifndef GAMEMANAGER_H
#define GAMEMANAGER_H

#include "Wind.h"         
#include "Character.h"  
#include "Footballer.h"
#include "Physics.h"
#include "inputManager.h"
#include "utils.h"

const int MAX_PHYSICS_OBJECTS = 20; // Maximum number of physics objects

class GameManager {
private:
    static GameManager* instance;

    Character* teamACharacters[NUM_CHAR];  
    Character* teamBCharacters[NUM_CHAR];  
    Footballer* teamAFootballers[NUM_FOOTBALLER * NUM_CHAR];
    Footballer* teamBFootballers[NUM_FOOTBALLER * NUM_CHAR];
    Physics* physics[2 * NUM_FOOTBALLER * NUM_CHAR]; 

    Wind* wind; 

    SDL_Surface *window_surface;

    GameManager(SDL_Surface *window_surf);

public:
    static GameManager* getInstance(SDL_Surface *window_surf);

    void update(float deltaTime);
    SDL_Surface* GetSurf();

    Character* getTeamACharacter(int index) const;
    Character* getTeamBCharacter(int index) const;
    Physics* getPhysicsObject(int index) const;
    Character** getTeamACharacters();  
    Character** getTeamBCharacters();
    int getPhysicsObjectCount() const { return MAX_PHYSICS_OBJECTS; }

    Wind* getWind() const { return wind; }
};

#endif // GAMEMANAGER_H
