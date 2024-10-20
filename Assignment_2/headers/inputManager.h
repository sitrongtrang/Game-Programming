#ifndef INPUTMANAGER_H
#define INPUTMANAGER_H

#include "keyBinding.h"
#include "Character.h"
#include <set>


class InputManager {
private:
    std::set<SDL_Keycode> pressedKeys;

protected:
    void changePlayer(int player, PlayerAction action)  ;
    void movePlayer(Character * player, PlayerAction action) const;
    Character ** p1_character_list; 
    Character ** p2_character_list; 
    int char_num[2];
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
