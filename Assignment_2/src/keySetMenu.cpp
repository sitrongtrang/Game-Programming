#include "../headers/keySetMenu.h"
#include "../headers/keyBinding.h"
#include "../headers/utils.h"
#include <iostream>

// Constructor
KeySetMenu::KeySetMenu(KeyBinding &keyBindings)
    : keyBindingsInstance(keyBindings), isPlayer1Selected(true) {}

// Function to render the Key Set Menu
void KeySetMenu::Render(GameState &state, bool &game_paused)
{

    ImVec2 displaySize = ImGui::GetIO().DisplaySize;

    // Calculate the center position based on the display size
    ImVec2 mainPos;
    mainPos.x = (displaySize.x - KeySetMenu::WIDTH) / 2.0f;  // Center horizontally
    mainPos.y = (displaySize.y - KeySetMenu::HEIGHT) / 2.0f; // Center vertically

    // Set the window size
    ImGui::SetNextWindowSize(ImVec2(KeySetMenu::WIDTH, KeySetMenu::HEIGHT), ImGuiCond_Once);

    // Set the next window position to the calculated center position
    ImGui::SetNextWindowPos(mainPos, ImGuiCond_Once);
    ImGui::Begin("Key Set Menu", NULL, ImGuiWindowFlags_NoResize | ImGuiWindowFlags_NoTitleBar);

    ImGui::Text("Controls:");
    ImGui::Separator();

    // Toggle between Player 1 and Player 2
    if (ImGui::Button(isPlayer1Selected ? "Switch to Player 2" : "Switch to Player 1"))
    {
        isPlayer1Selected = !isPlayer1Selected; // Toggle player selection
    }

    // Render key buttons for the selected player
    renderKeyBindings();

    // Create a horizontal layout for the buttons
    ImGui::Separator(); // Separate action buttons from other options
    ImGui::Spacing();

    if (waitingForKey == KeySetState::WaitingForAnyKey)
    {
        ImGui::Text("Waiting for key press...");
    }
    else if (waitingForKey == KeySetState::DupplicateKey)
    {
        ImGui::Text("Duplicated key, please try another");
    }

    else
    {
        // Calculate the total width of both buttons
        float buttonWidth = 150.0f;                                                 // Width of each button
        float totalButtonWidth = 4 * buttonWidth + ImGui::GetStyle().ItemSpacing.x; // Adding spacing between buttons

        // Center the buttons
        ImGui::SetCursorPosX((ImGui::GetWindowWidth() - totalButtonWidth) * 0.5f);

        // Render the Resume Game button
        if (ImGui::Button("Resume Game", ImVec2(buttonWidth, 40)))
        {
            game_paused = false; // Resume the game
            pausedDuration += std::chrono::duration_cast<std::chrono::seconds>(std::chrono::steady_clock::now() - pauseTime).count();
        }

        // Keep the Reset button on the same line
        ImGui::SameLine();

        // Render the Reset to Default button
        if (ImGui::Button("Reset to Default", ImVec2(buttonWidth, 40)))
        {
            keyBindingsInstance.resetKeyBindings(); // Reset key bindings to defaults
        }
        ImGui::SameLine();
        if (ImGui::Button("Main menu", ImVec2(2 * buttonWidth, 40)))
        {
            game_paused = false;
            state = GameState::MAIN_MENU;
            pausedDuration = 0;
        }
    }

    ImGui::End();
}

// Function to render key buttons for the selected player
void KeySetMenu::renderKeyBindings()
{
    const char *playerName = isPlayer1Selected ? "Player 1" : "Player 2";

    ImGui::Text("%s Movement:", playerName);
    renderMovementKeys();

    ImGui::Separator(); // Separate movement keys from action keys

    ImGui::Text("%s Actions:", playerName);
    renderActionKeys();
}

void KeySetMenu::renderMovementKeys()
{
    const float buttonWidth = 50.0f;  // Width of each button
    const float buttonHeight = 50.0f; // Width of each button

    const float spacing = 10.0f; // Space between buttons

    // First row - Up button
    ImGui::BeginGroup();
    // Center the Up button
    ImGui::SetCursorPosX(ImGui::GetCursorPosX() + buttonWidth + spacing);
    renderKeyButton(PlayerAction::MoveUp, "↑", buttonWidth, buttonHeight); // Use renderKeyButton for movement
    ImGui::EndGroup();

    // Second row - Left, Down, Right buttons
    ImGui::BeginGroup();
    renderKeyButton(PlayerAction::MoveLeft, "←", buttonWidth, buttonHeight);  // Use renderKeyButton for left
    ImGui::SameLine(0, spacing);                                              // Keep the left arrow button on the same line
    renderKeyButton(PlayerAction::MoveDown, "↓", buttonWidth, buttonHeight);  // Use renderKeyButton for down
    ImGui::SameLine(0, spacing);                                              // Keep the down arrow button on the same line
    renderKeyButton(PlayerAction::MoveRight, "→", buttonWidth, buttonHeight); // Use renderKeyButton for right
    ImGui::EndGroup();
}

// Render action keys
void KeySetMenu::renderActionKeys()
{
    renderKeyButton(PlayerAction::Action1, "Action 1");
    renderKeyButton(PlayerAction::Action2, "Action 2");
    renderKeyButton(PlayerAction::Action3, "Action 3");
}

// Function to render a single key button
void KeySetMenu::renderKeyButton(PlayerAction action, const char *label, float width, float height)
{
    SDL_Keycode currentKey = isPlayer1Selected ? keyBindingsInstance.getPlayer1Key(action) : keyBindingsInstance.getPlayer2Key(action);
    if (waitingForKey != KeySetState::NotWaiting && selectedAction == action)
    {
        ImGui::Button("Press a new key", ImVec2(width, height));
        if (isPlayer1Selected)
        {
            keyBindingsInstance.changePlayer1Key(action, waitingForKey);
        }
        else
        {
            keyBindingsInstance.changePlayer2Key(action, waitingForKey);
        }
    }
    else
    {
        if (ImGui::Button(SDL_GetKeyName(currentKey), ImVec2(width, height)))
        {
            selectedAction = action;
            waitingForKey = KeySetState::WaitingForAnyKey;
        }
    }
}

// Render the Resume Game button
void KeySetMenu::renderResumeButton(bool &game_paused)
{
    ImGui::Separator(); // Separate action buttons from other options
    ImGui::Spacing();

    if (waitingForKey != KeySetState::NotWaiting)
    {
        ImGui::Text("Waiting for key press...");
    }
    else
    {
        ImGui::SetCursorPosX((ImGui::GetWindowWidth() - 150) * 0.5f); // Center the button
        if (ImGui::Button("Resume Game", ImVec2(150, 40)))
        {
            game_paused = false;
        }
    }
}
