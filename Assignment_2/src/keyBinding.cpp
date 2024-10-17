#include "../headers/keyBinding.h"
#include "keyBinding.h"
#include "keySetMenu.h"
#include <iostream>
#include <unordered_map>

// Global instance of KeyBinding
KeyBinding keyBindingsInstance;

// Constructor to initialize key bindings
KeyBinding::KeyBinding() {
    initializeDefaultKeyBindings();
}

// Initialize default key bindings
void KeyBinding::initializeDefaultKeyBindings() {
    player1Bindings.moveUp = SDLK_w;
    player1Bindings.moveDown = SDLK_s;
    player1Bindings.moveLeft = SDLK_a;
    player1Bindings.moveRight = SDLK_d;
    player1Bindings.action1 = SDLK_e;
    player1Bindings.action2 = SDLK_q;
    player1Bindings.action3 = SDLK_r;

    player2Bindings.moveUp = SDLK_UP;
    player2Bindings.moveDown = SDLK_DOWN;
    player2Bindings.moveLeft = SDLK_LEFT;
    player2Bindings.moveRight = SDLK_RIGHT;
    player2Bindings.action1 = SDLK_RETURN;
    player2Bindings.action2 = SDLK_RSHIFT;
    player2Bindings.action3 = SDLK_RCTRL;
}

// Change key for Player 1
void KeyBinding::changePlayer1Key(PlayerAction action,KeySetState& waitingForKey) {
    switch (action) {
        case PlayerAction::MoveUp:    changeKey(player1Bindings.moveUp,waitingForKey); break;
        case PlayerAction::MoveDown:  changeKey(player1Bindings.moveDown,waitingForKey); break;
        case PlayerAction::MoveLeft:  changeKey(player1Bindings.moveLeft,waitingForKey); break;
        case PlayerAction::MoveRight: changeKey(player1Bindings.moveRight,waitingForKey); break;
        case PlayerAction::Action1:   changeKey(player1Bindings.action1,waitingForKey); break;
        case PlayerAction::Action2:   changeKey(player1Bindings.action2,waitingForKey); break;
        case PlayerAction::Action3:   changeKey(player1Bindings.action3,waitingForKey); break;
    }
}

// Change key for Player 2
void KeyBinding::changePlayer2Key(PlayerAction action,KeySetState& waitingForKey) {
    switch (action) {
        case PlayerAction::MoveUp:    changeKey(player2Bindings.moveUp,waitingForKey); break;
        case PlayerAction::MoveDown:  changeKey(player2Bindings.moveDown,waitingForKey); break;
        case PlayerAction::MoveLeft:  changeKey(player2Bindings.moveLeft,waitingForKey); break;
        case PlayerAction::MoveRight: changeKey(player2Bindings.moveRight,waitingForKey); break;
        case PlayerAction::Action1:   changeKey(player2Bindings.action1,waitingForKey); break;
        case PlayerAction::Action2:   changeKey(player2Bindings.action2,waitingForKey); break;
        case PlayerAction::Action3:   changeKey(player2Bindings.action3,waitingForKey); break;
    }

}

// Change key by capturing user input
void KeyBinding::changeKey(SDL_Keycode& key,KeySetState& waitingForKey) {
    SDL_Event event;

    while (waitingForKey!=KeySetState::NotWaiting) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_KEYDOWN) {
                key = event.key.keysym.sym;  // Update key binding
                if (hasSingleDuplicateKey()){
                    waitingForKey=KeySetState::DupplicateKey;
                }
                else{
                    waitingForKey=KeySetState::NotWaiting;
                }
                printf("Key pressed: %s\n", SDL_GetKeyName(key));
            }
        }
    }
}

// Reset to default
void KeyBinding::resetKeyBindings() {
    initializeDefaultKeyBindings();
}

// Get Player 1 key
SDL_Keycode KeyBinding::getPlayer1Key(PlayerAction action) const {
    switch (action) {
        case PlayerAction::MoveUp:    return player1Bindings.moveUp;
        case PlayerAction::MoveDown:  return player1Bindings.moveDown;
        case PlayerAction::MoveLeft:  return player1Bindings.moveLeft;
        case PlayerAction::MoveRight: return player1Bindings.moveRight;
        case PlayerAction::Action1:   return player1Bindings.action1;
        case PlayerAction::Action2:   return player1Bindings.action2;
        case PlayerAction::Action3:   return player1Bindings.action3;
    }
    return SDLK_UNKNOWN; // Invalid action
}

// Get Player 2 key
SDL_Keycode KeyBinding::getPlayer2Key(PlayerAction action) const {
    switch (action) {
        case PlayerAction::MoveUp:    return player2Bindings.moveUp;
        case PlayerAction::MoveDown:  return player2Bindings.moveDown;
        case PlayerAction::MoveLeft:  return player2Bindings.moveLeft;
        case PlayerAction::MoveRight: return player2Bindings.moveRight;
        case PlayerAction::Action1:   return player2Bindings.action1;
        case PlayerAction::Action2:   return player2Bindings.action2;
        case PlayerAction::Action3:   return player2Bindings.action3;
    }
    return SDLK_UNKNOWN; // Invalid action
}
bool KeyBinding::hasSingleDuplicateKey() const {
    std::unordered_map<SDL_Keycode, int> keyUsage; // To store key and its count of usage
    int duplicateCount = 0; // Count of keys that are used more than once

    // Helper lambda to add key usage
    auto addKeyUsage = [&](SDL_Keycode key) {
        if (keyUsage.find(key) != keyUsage.end()) {
            keyUsage[key]++;
        } else {
            keyUsage[key] = 1;
        }
    };

    // Check Player 1 bindings
    addKeyUsage(getPlayer1Key(PlayerAction::MoveUp));
    addKeyUsage(getPlayer1Key(PlayerAction::MoveDown));
    addKeyUsage(getPlayer1Key(PlayerAction::MoveLeft));
    addKeyUsage(getPlayer1Key(PlayerAction::MoveRight));
    addKeyUsage(getPlayer1Key(PlayerAction::Action1));
    addKeyUsage(getPlayer1Key(PlayerAction::Action2));
    addKeyUsage(getPlayer1Key(PlayerAction::Action3));

    // Check Player 2 bindings
    addKeyUsage(getPlayer2Key(PlayerAction::MoveUp));
    addKeyUsage(getPlayer2Key(PlayerAction::MoveDown));
    addKeyUsage(getPlayer2Key(PlayerAction::MoveLeft));
    addKeyUsage(getPlayer2Key(PlayerAction::MoveRight));
    addKeyUsage(getPlayer2Key(PlayerAction::Action1));
    addKeyUsage(getPlayer2Key(PlayerAction::Action2));
    addKeyUsage(getPlayer2Key(PlayerAction::Action3));

    // Count how many keys are used more than once
    for (const auto& entry : keyUsage) {
        if (entry.second > 1) {
            duplicateCount++;
        }
    }

    // Return true if there is exactly one duplicate
    return duplicateCount == 1;
}


Actions KeyBinding::getAction(SDL_Keycode key) const {
    Actions action;
    if (key == player1Bindings.moveUp) {
        action.character_num = 1;
        action.action = PlayerAction::MoveUp;
    } else if (key == player1Bindings.moveDown) {
        action.character_num = 1;
        action.action = PlayerAction::MoveDown;
    } else if (key == player1Bindings.moveLeft) {
        action.character_num = 1;
        action.action = PlayerAction::MoveLeft;
    } else if (key == player1Bindings.moveRight) {
        action.character_num = 1;
        action.action = PlayerAction::MoveRight;
    } else if (key == player1Bindings.action1) {
        action.character_num = 1;
        action.action = PlayerAction::Action1;
    } else if (key == player1Bindings.action2) {
        action.character_num = 1;
        action.action = PlayerAction::Action2;
    } else if (key == player1Bindings.action3) {
        action.character_num = 1;
        action.action = PlayerAction::Action3;
    } else if (key == player2Bindings.moveUp) {
        action.character_num = 2;
        action.action = PlayerAction::MoveUp;
    } else if (key == player2Bindings.moveDown) {
        action.character_num = 2;
        action.action = PlayerAction::MoveDown;
    } else if (key == player2Bindings.moveLeft) {
        action.character_num = 2;
        action.action = PlayerAction::MoveLeft;
    } else if (key == player2Bindings.moveRight) {
        action.character_num = 2;
        action.action = PlayerAction::MoveRight;
    } else if (key == player2Bindings.action1) {
        action.character_num = 2;
        action.action = PlayerAction::Action1;
    } else if (key == player2Bindings.action2) {
        action.character_num = 2;
        action.action = PlayerAction::Action2;
    } else if (key == player2Bindings.action3) {
        action.character_num = 2;
        action.action = PlayerAction::Action3;
    } else {
        action.character_num = 0;
        action.action = PlayerAction::None;
    }
    return action;
}