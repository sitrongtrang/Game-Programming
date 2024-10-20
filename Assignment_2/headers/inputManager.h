#ifndef INPUTMANAGER_H
#define INPUTMANAGER_H

#include "keyBinding.h"
#include "Character.h"
#include <set>


class InputManager {
private:
    Character ** p1_charater_list; 
    Character ** p2_charater_list; 
    std::set<SDL_Keycode> pressedKeys;
protected:
    Character * p1;
    Character * p2;
    Character * changePlayer(Character ** player, PlayerAction action) const ;
    void movePlayer(Character * player, PlayerAction action) const;
    void stopPlayer(Character * player) const;
public:
    void input(SDL_Keycode key);
    void release(SDL_Keycode key);
    void stopPlayerIfNoKeysPressed(Character *player) const;
    void setCharacters(Character** character_1, Character** character_2);
    InputManager();
};

#endif
extern InputManager inputManager;
