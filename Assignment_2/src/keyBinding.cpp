#include "../headers/keyBinding.h"
#include "keyBinding.h"

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
void KeyBinding::changePlayer1Key(PlayerAction action,bool& waitingForKey) {
    switch (action) {
        case PlayerAction::MoveUp:    changeKey(player1Bindings.moveUp); break;
        case PlayerAction::MoveDown:  changeKey(player1Bindings.moveDown); break;
        case PlayerAction::MoveLeft:  changeKey(player1Bindings.moveLeft); break;
        case PlayerAction::MoveRight: changeKey(player1Bindings.moveRight); break;
        case PlayerAction::Action1:   changeKey(player1Bindings.action1); break;
        case PlayerAction::Action2:   changeKey(player1Bindings.action2); break;
        case PlayerAction::Action3:   changeKey(player1Bindings.action3); break;
    }
    waitingForKey=false;
}

// Change key for Player 2
void KeyBinding::changePlayer2Key(PlayerAction action,bool& waitingForKey) {
    switch (action) {
        case PlayerAction::MoveUp:    changeKey(player2Bindings.moveUp); break;
        case PlayerAction::MoveDown:  changeKey(player2Bindings.moveDown); break;
        case PlayerAction::MoveLeft:  changeKey(player2Bindings.moveLeft); break;
        case PlayerAction::MoveRight: changeKey(player2Bindings.moveRight); break;
        case PlayerAction::Action1:   changeKey(player2Bindings.action1); break;
        case PlayerAction::Action2:   changeKey(player2Bindings.action2); break;
        case PlayerAction::Action3:   changeKey(player2Bindings.action3); break;
    }
    waitingForKey=false;

}

// Change key by capturing user input
void KeyBinding::changeKey(SDL_Keycode& key) {
    SDL_Event event;
    bool waitingForKey = true;

    while (waitingForKey) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_KEYDOWN) {
                key = event.key.keysym.sym;  // Update key binding
                printf("Key pressed: %s\n", SDL_GetKeyName(key));
                waitingForKey = false;       // Exit the loop
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
bool KeyBinding::isKeyInUse(SDL_Keycode key, PlayerAction action) const {
    // Check Player 1 bindings
    if (key == getPlayer1Key(PlayerAction::MoveUp) && action != PlayerAction::MoveUp) return true;
    if (key == getPlayer1Key(PlayerAction::MoveDown) && action != PlayerAction::MoveDown) return true;
    if (key == getPlayer1Key(PlayerAction::MoveLeft) && action != PlayerAction::MoveLeft) return true;
    if (key == getPlayer1Key(PlayerAction::MoveRight) && action != PlayerAction::MoveRight) return true;
    if (key == getPlayer1Key(PlayerAction::Action1) && action != PlayerAction::Action1) return true;
    if (key == getPlayer1Key(PlayerAction::Action2) && action != PlayerAction::Action2) return true;
    if (key == getPlayer1Key(PlayerAction::Action3) && action != PlayerAction::Action3) return true;

    // Check Player 2 bindings
    if (key == getPlayer2Key(PlayerAction::MoveUp) && action != PlayerAction::MoveUp) return true;
    if (key == getPlayer2Key(PlayerAction::MoveDown) && action != PlayerAction::MoveDown) return true;
    if (key == getPlayer2Key(PlayerAction::MoveLeft) && action != PlayerAction::MoveLeft) return true;
    if (key == getPlayer2Key(PlayerAction::MoveRight) && action != PlayerAction::MoveRight) return true;
    if (key == getPlayer2Key(PlayerAction::Action1) && action != PlayerAction::Action1) return true;
    if (key == getPlayer2Key(PlayerAction::Action2) && action != PlayerAction::Action2) return true;
    if (key == getPlayer2Key(PlayerAction::Action3) && action != PlayerAction::Action3) return true;

    return false; // Key is not in use
}