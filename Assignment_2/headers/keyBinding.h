#ifndef KEYBINDING_H
#define KEYBINDING_H

#include <SDL2/SDL.h>

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
class KeyBinding {
public:
    

    KeyBinding();  // Constructor to initialize key bindings

    void changePlayer1Key(PlayerAction action, bool &waitingForKey);
    void changePlayer2Key(PlayerAction action, bool &waitingForKey);
    void resetKeyBindings();

    SDL_Keycode getPlayer1Key(PlayerAction action) const;
    SDL_Keycode getPlayer2Key(PlayerAction action) const;
    bool isKeyInUse(SDL_Keycode key, PlayerAction action) const;

private:
    PlayerKeyBindings player1Bindings;
    PlayerKeyBindings player2Bindings;

    void initializeDefaultKeyBindings();
    void changeKey(SDL_Keycode &key);
};

// Global instance of KeyBinding
extern KeyBinding keyBindingsInstance;

#endif
