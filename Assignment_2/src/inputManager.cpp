#include "../headers/inputManager.h"

InputManager::InputManager(Character ** character_1, Character ** character_2) {
    p1_charater = character_1;
    p2_charater = character_2;
}

void InputManager::input(SDL_Keycode key) const {  
    Actions action_mapped = keyBindingsInstance.getAction(key);
    Character * character;
    switch (action_mapped.character_num);
    {
    case 1: character = p1_charater; break;
    case 2: character = p2_charater; break;
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
    case (PlayerAction::MoveUp): player->applyAcc({0 * MOVEMENT_FORCE, MOVEMENT_FORCE}); break;
    case (PlayerAction::MoveDown): player->applyAcc({0 * MOVEMENT_FORCE, -1 * MOVEMENT_FORCE}); break;
    case (PlayerAction::MoveLeft): player->applyAcc({-1 * MOVEMENT_FORCE, MOVEMENT_FORCE}); break;
    case (PlayerAction::MoveRight): player->applyAcc({MOVEMENT_FORCE, 0 * MOVEMENT_FORCE}); break;
    default: return;
    }
}