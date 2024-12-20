#ifndef KEYBINDING_H
#define KEYBINDING_H

#include <SDL2/SDL.h>
#include <stdio.h>

enum class KeySetState {
    NotWaiting,
    WaitingForAnyKey,
    DupplicateKey,
};
// Structure for player key bindings
struct PlayerKeyBindings {
    SDL_Keycode moveUp;
    SDL_Keycode moveDown;
    SDL_Keycode moveLeft;
    SDL_Keycode moveRight;
    SDL_Keycode action1;
    SDL_Keycode action2;
    SDL_Keycode action3;
};
enum class PlayerAction {
    MoveUp,
    MoveDown,
    MoveLeft,
    MoveRight,
    Action1,
    Action2,
    Action3,
    None
};

struct Actions {
    int character_num;
    PlayerAction action;
};
class KeyBinding {
public:
    

    KeyBinding();  // Constructor to initialize key bindings

    void changePlayer1Key(PlayerAction action, KeySetState &waitingForKey);
    void changePlayer2Key(PlayerAction action, KeySetState &waitingForKey);
    void resetKeyBindings();

    SDL_Keycode getPlayer1Key(PlayerAction action) const;
    SDL_Keycode getPlayer2Key(PlayerAction action) const;
    Actions getAction(SDL_Keycode key) const;
    bool hasSingleDuplicateKey() const;

private:
    PlayerKeyBindings player1Bindings;
    PlayerKeyBindings player2Bindings;

    void initializeDefaultKeyBindings();
    void changeKey(SDL_Keycode &key, KeySetState &waitingForKey);
};

// Global instance of KeyBinding
extern KeyBinding keyBindingsInstance;

#endif
