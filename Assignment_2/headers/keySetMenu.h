#ifndef KEYSETMENU_H
#define KEYSETMENU_H

#include "keyBinding.h"
#include "utils.h"
#include <imgui.h>


class KeySetMenu {
public:
    // Constructor
    KeySetMenu(KeyBinding& keyBindings);

    // Function to render the Key Set Menu
    void Render(bool& game_paused);

private:
    // Function to render key buttons for the selected player
    void renderKeyBindings();
    
    // Function to render movement keys
    void renderMovementKeys();

    // Function to render action keys
    void renderActionKeys();

    // Function to render a single key button
    void renderKeyButton(PlayerAction action, const char* label,float width = 150.0f,float height = 0.0f);

    // Function to render the Resume Game button
    void renderResumeButton(bool& game_paused);

    KeyBinding& keyBindingsInstance; // Reference to key bindings instance
    bool isPlayer1Selected;           // Track which player is selected
    KeySetState waitingForKey = KeySetState::NotWaiting;       // Indicates if waiting for key input
    PlayerAction selectedAction;      // Currently selected action to change key
    const int HEIGHT=SCREEN_HEIGHT*70/100;
    const int WIDTH=SCREEN_WIDTH*70/100;
};

#endif
