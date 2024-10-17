#ifndef INPUTMANAGER_H
#define INPUTMANAGER_H

#include "keyBinding.h"
#include "Character.h"

#define MOVEMENT_FORCE 1.0f

class InputManager {
private:
    Character ** p1_charater_list; 
    Character ** p2_charater_list; 
protected:
    Character * p1;
    Character * p2;
    void changePlayer(Character * player, PlayerAction action) const ;
    void movePlayer(Character * player, PlayerAction action) const;
public:
    void input(SDL_Keycode key) const;
    InputManager(Character ** character_1, Character ** character_2);
};

#endif
extern InputManager inputManager;
