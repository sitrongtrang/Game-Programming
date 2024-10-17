#ifndef INPUTMANAGER_H
#define INPUTMANAGER_H

#include"keyBinding.h"
#include"Character.h"



class InputManager {
private:
    Character ** p1_charater; 
    Character ** p2_charater; 
protected:
    
public:
    void input(SDL_Keycode key);
    InputManager(Character ** character_1, Character ** character_2);
};

extern InputManager inputManager;
#endif
