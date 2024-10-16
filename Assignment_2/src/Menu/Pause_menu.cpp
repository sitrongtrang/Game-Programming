#include "../headers/menu/Pause_menu.h"
void renderPauseMenu(GameState &state, int &score1, int &score2)
{
    ImGui::Begin("GAME PAUSED", NULL, ImGuiWindowFlags_NoResize | ImGuiWindowFlags_NoMove | ImGuiWindowFlags_NoCollapse | ImGuiWindowFlags_NoTitleBar);
    ImGui::SetWindowSize(ImVec2(320, 400));
    ImGui::SetWindowPos(ImVec2(440, 210));

    // Title
    ImGui::SetWindowFontScale(1.0f);
    ImVec2 windowSize = ImGui::GetWindowSize();
    ImVec2 textSize = ImGui::CalcTextSize("GAME PAUSED");
    ImGui::SetCursorPosX((windowSize.x - textSize.x) * 0.5f);
    ImGui::SetCursorPosY(45.0f);
    ImGui::Text("GAME PAUSED");

    // Resume button
    ImGui::SetWindowFontScale(0.75f);
    ImGui::SetCursorPosX((windowSize.x - 200) * 0.5f);
    ImGui::SetCursorPosY(120.0f);
    if (ImGui::Button("RESUME", ImVec2(200, 50)))
    {
        state = GameState::PLAYING;
        pausedDuration += std::chrono::duration_cast<std::chrono::seconds>(std::chrono::steady_clock::now() - pauseTime).count();
    }

    // Restart button
    ImGui::SetCursorPosX((windowSize.x - 200) * 0.5f);
    ImGui::SetCursorPosY(210.0f);
    if (ImGui::Button("RESTART", ImVec2(200, 50)))
    {
        state = GameState::PLAYING;
        startTime = std::chrono::steady_clock::now();
        score1 = 0;
        score2 = 0;
        pausedDuration = 0;
    }

    // Main menu button
    ImGui::SetCursorPosX((windowSize.x - 200) * 0.5f);
    ImGui::SetCursorPosY(300.0f);
    if (ImGui::Button("MAIN MENU", ImVec2(200, 50)))
    {
        state = GameState::MAIN_MENU;
        pausedDuration = 0;
    }
    ImGui::End();
}
