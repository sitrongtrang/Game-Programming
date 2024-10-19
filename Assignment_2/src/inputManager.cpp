#include "../headers/inputManager.h"

InputManager::InputManager(Character ** character_1, Character ** character_2) {
    p1_charater_list = character_1;
    p2_charater_list = character_2;
    p1 = character_1[0];
    p2 = character_2[0];
}

void InputManager::input(SDL_Keycode key) {  
    Actions action_mapped = keyBindingsInstance.getAction(key);
    Character * character;
    Character ** character_list;
    switch (action_mapped.character_num)
    {
        case 1: character = p1; character_list =  p1_charater_list; break;
        case 2: character = p2; character_list =  p2_charater_list; break;
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
        case (PlayerAction::Action3):{
            Character * active_player = changePlayer(character_list, action_mapped.action);
            if (!active_player) return;
            if (action_mapped.character_num == 1) 
                p1 = active_player;
            else
                p2 = active_player;
            break;}
        default:
            return;
    }
}; 

Character * InputManager::changePlayer(Character ** player_list, PlayerAction action) const {
    int char_num;
    switch (action)
    {
        case (PlayerAction::Action1): char_num= 0 ;break;
        case (PlayerAction::Action2): char_num= 1 ;break;
        case (PlayerAction::Action3): char_num= 2 ;break;
        default: return nullptr;
    }
    return player_list[char_num];
}

void InputManager::movePlayer(Character * player, PlayerAction action) const {
    switch (action)
    {
        case (PlayerAction::MoveUp): player->setVel({0 * MOVEMENT_FORCE, MOVEMENT_FORCE}); break;
        case (PlayerAction::MoveDown): player->setVel({0 * MOVEMENT_FORCE, -1 * MOVEMENT_FORCE}); break;
        case (PlayerAction::MoveLeft): player->setVel({-1 * MOVEMENT_FORCE, MOVEMENT_FORCE}); break;
        case (PlayerAction::MoveRight): player->setVel({MOVEMENT_FORCE, 0 * MOVEMENT_FORCE}); break;
        default: return;
    }
}