#include "../headers/menu/Game_over_menu.h"
void renderGameOver(GameState &state, int &score1, int &score2)
{
    ImGui::Begin("GAME OVER", NULL, ImGuiWindowFlags_NoResize | ImGuiWindowFlags_NoMove | ImGuiWindowFlags_NoCollapse | ImGuiWindowFlags_NoTitleBar);
    ImGui::SetWindowSize(ImVec2(400, 400));
    ImGui::SetWindowPos(ImVec2(440, 210));

    // "Game Over"
    ImGui::SetWindowFontScale(1.0f);
    ImVec2 windowSize = ImGui::GetWindowSize();
    ImVec2 textSize = ImGui::CalcTextSize("GAME OVER");
    ImGui::SetCursorPosX((windowSize.x - textSize.x) * 0.5f);
    ImGui::SetCursorPosY(45.0f);
    ImGui::Text("GAME OVER");
    ImGui::SetWindowFontScale(0.75f);
    ImGui::SetCursorPosY(120.0f);

    // Display the winner
    if (score1 > score2)
    {
        textSize = ImGui::CalcTextSize("TEAM A WINS");
        ImGui::SetCursorPosX((windowSize.x - textSize.x) * 0.5f);
        ImGui::Text("TEAM A WINS");
    }
    else if (score1 < score2)
    {
        textSize = ImGui::CalcTextSize("TEAM B WINS");
        ImGui::SetCursorPosX((windowSize.x - textSize.x) * 0.5f);
        ImGui::Text("TEAM B WINS");
    }
    else
    {
        textSize = ImGui::CalcTextSize("DRAW");
        ImGui::SetCursorPosX((windowSize.x - textSize.x) * 0.5f);
        ImGui::Text("DRAW");
    }

    // Show the score
    char buffer[50];
    sprintf(buffer, "TEAM A %d - %d TEAM B", score1, score2);
    textSize = ImGui::CalcTextSize(buffer);
    ImGui::SetCursorPosX((windowSize.x - textSize.x) * 0.5f);
    ImGui::SetCursorPosY(180.0f);
    ImGui::Text("TEAM A %d - %d TEAM B", score1, score2);

    // Retry button
    ImGui::SetCursorPosX((windowSize.x - 200) * 0.5f);
    ImGui::SetCursorPosY(210.0f);
    if (ImGui::Button("RETRY", ImVec2(200, 50)))
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
