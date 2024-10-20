#ifndef INPUTMANAGER_H
#define INPUTMANAGER_H

#include "keyBinding.h"
#include "Character.h"


class InputManager {
private:

protected:
    void changePlayer(int player, PlayerAction action)  ;
    void movePlayer(Character * player, PlayerAction action) const;
    Character ** p1_character_list; 
    Character ** p2_character_list; 
    int char_num[2];


public:
    void input(SDL_Keycode key);
    InputManager(Character ** character_1, Character ** character_2);
};

#endif
extern InputManager inputManager;
