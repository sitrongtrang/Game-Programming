#include "../headers/inputManager.h"

InputManager::InputManager(Character ** character_1, Character ** character_2) {
    p1_charater_list = character_1;
    p2_charater_list = character_2;
    p1 = character_1[0];
    p2 = character_2[0];
}

void InputManager::input(SDL_Keycode key) const {  
    Actions action_mapped = keyBindingsInstance.getAction(key);
    Character * character;
    switch (action_mapped.character_num)
    {
    case 1: character = p1; break;
    case 2: character = p2; break;
    default: return;
    }

    switch (action_mapped.action)
    {
    case (PlayerAction::MoveUp):
    case (PlayerAction::MoveDown):
    case (PlayerAction::MoveLeft):
    case (PlayerAction::MoveRight):
        movePlayer(character, action_mapped.action);
        break;
    case (PlayerAction::Action1):
    case (PlayerAction::Action2):
    case (PlayerAction::Action3):
        changePlayer(character, action_mapped.action);
        break;
    default:
        return;
    }
}; 

void InputManager::changePlayer(Character * player, PlayerAction action) const {
    int char_num;
    switch (action)
    {
    case (PlayerAction::Action1): char_num= 0 ;break;
    case (PlayerAction::Action2): char_num= 1 ;break;
    case (PlayerAction::Action3): char_num= 2 ;break;
    default: return;
    }
}

void InputManager::movePlayer(Character * player, PlayerAction action) const {
    switch (action)
    {
    case (PlayerAction::MoveUp): player->setAcc({0 * MOVEMENT_FORCE, MOVEMENT_FORCE}); break;
    case (PlayerAction::MoveDown): player->setAcc({0 * MOVEMENT_FORCE, -1 * MOVEMENT_FORCE}); break;
    case (PlayerAction::MoveLeft): player->setAcc({-1 * MOVEMENT_FORCE, MOVEMENT_FORCE}); break;
    case (PlayerAction::MoveRight): player->setAcc({MOVEMENT_FORCE, 0 * MOVEMENT_FORCE}); break;
    default: return;
    }
}