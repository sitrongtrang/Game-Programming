#include "../headers/menu/Game_menu.h"
void renderGameMenu(GameState &state, bool &game_paused, int &score1, int &score2)
{
    ImGui::Begin("Game Menu", NULL, ImGuiWindowFlags_NoDecoration | ImGuiWindowFlags_NoTitleBar | ImGuiWindowFlags_NoResize | ImGuiWindowFlags_NoMove | ImGuiWindowFlags_NoCollapse | ImGuiWindowFlags_NoBackground);
    ImGui::SetWindowSize(ImVec2(1280, 720));
    ImGui::SetWindowPos(ImVec2(0, 0));

    // Display score
    ImGui::SetCursorPosY(15.0f);
    ImGui::Text("TEAM A %d - %d TEAM B ", score1, score2);
    ImGui::SameLine();

    // Calculate remaining time
    ImGui::SetCursorPosX((1280 - 200) * 0.5f);
    ImGui::SetCursorPosY(0.0f);
    auto currentTime = std::chrono::steady_clock::now();
    int elapsedTime = std::chrono::duration_cast<std::chrono::seconds>(currentTime - startTime).count() - pausedDuration;
    int remainingTime = countdownDuration - elapsedTime;
    if (remainingTime < 0)
    {
        remainingTime = 0;
        state = GameState::GAME_OVER;
    }

    // make the button show time
    char remainingTimeLabel[100];
    sprintf(remainingTimeLabel, "%d : %d", remainingTime / 60, remainingTime % 60);
    if (ImGui::Button(remainingTimeLabel, ImVec2(200, 50)))
    {
        game_paused = !game_paused;
        if (game_paused)
        {
            pauseTime = std::chrono::steady_clock::now();
        }
        else
        {
            pausedDuration += std::chrono::duration_cast<std::chrono::seconds>(std::chrono::steady_clock::now() - pauseTime).count();
        }
    }
    ImGui::End();
}
