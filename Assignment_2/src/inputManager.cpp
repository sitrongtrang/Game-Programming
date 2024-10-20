#include "../headers/inputManager.h"

InputManager::InputManager(Character ** character_1, Character ** character_2) {
    p1_character_list = character_1;
    p2_character_list = character_2;
    
    char_num[0] = 0;  // For player 1
    char_num[1] = 0;  // For player 2
}

void InputManager::input(SDL_Keycode key) {  
void InputManager::input(SDL_Keycode key) {  
    Actions action_mapped = keyBindingsInstance.getAction(key);
    Character * character;
    Character ** character_list;
    switch (action_mapped.character_num)
    {
    case 0: character = p1_character_list[char_num[0]]; break;
    case 1: character = p2_character_list[char_num[1]]; break;
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
        changePlayer(action_mapped.character_num, action_mapped.action);
        break;
    default:
        return;
    }
}; 

void InputManager::changePlayer(int player, PlayerAction action)  {
    switch (action)
    {
    case (PlayerAction::Action1): char_num[player]= 0 ;break;
    case (PlayerAction::Action2): char_num[player]= 1 ;break;
    case (PlayerAction::Action3): char_num[player]= 2 ;break;
    default: return;
    }
    return player_list[char_num];
}

void InputManager::movePlayer(Character * player, PlayerAction action) const {
    switch (action)
    {
        case (PlayerAction::MoveUp): player->setVel({0 * MOVEMENT_FORCE, MOVEMENT_FORCE}); break;
        case (PlayerAction::MoveDown): player->setVel({0 * MOVEMENT_FORCE, -1 * MOVEMENT_FORCE}); break;
        case (PlayerAction::MoveLeft): player->setVel({-1 * MOVEMENT_FORCE, 0 * MOVEMENT_FORCE}); break;
        case (PlayerAction::MoveRight): player->setVel({MOVEMENT_FORCE, 0 * MOVEMENT_FORCE}); break;
        default: return;
    }
}

void InputManager::stopPlayerIfNoKeysPressed(Character *player) const {
    if (pressedKeys.empty()) {
        stopPlayer(player); 
    }
}

void InputManager::stopPlayer(Character * player) const {
    player->setVel({0, 0});
}

void InputManager::release(SDL_Keycode key) {
    Actions action_mapped = keyBindingsInstance.getAction(key);
    Character * character;
    switch (action_mapped.character_num)
    {
        case 1: character = p1; break;
        case 2: character = p2; break;
        default: return;
    }
    switch(action_mapped.action)
    {
        case (PlayerAction::MoveUp):
        case (PlayerAction::MoveDown):
        case (PlayerAction::MoveLeft):
        case (PlayerAction::MoveRight):
            // stopPlayer(character);
            pressedKeys.erase(key);
            stopPlayerIfNoKeysPressed(character);
            break;
        default:
            return;
    }
}