#include "../headers/menu/Main_menu.h"
void renderBackground(GLuint background_texture)
{
    ImGui::SetNextWindowBgAlpha(0.0f);
    ImGui::SetWindowSize(ImVec2(1280, 720));
    ImGui::SetWindowPos(ImVec2(0, 0));
    ImGui::GetStyle().WindowPadding = ImVec2(0, 0);

    ImGui::Begin("Background", NULL, ImGuiWindowFlags_NoResize | ImGuiWindowFlags_NoMove | ImGuiWindowFlags_NoCollapse | ImGuiWindowFlags_NoTitleBar | ImGuiWindowFlags_NoBringToFrontOnFocus);

    ImGui::Image((ImTextureID)(intptr_t)background_texture, ImVec2(1280, 720), ImVec2(0, 0), ImVec2(1, 1));

    ImGui::End();
}
void renderMainMenu(GameState &state, bool &game_running)
{
    ImGui::SetNextWindowBgAlpha(0.0f);
    ImGui::Begin("Main Menu", NULL, ImGuiWindowFlags_NoDecoration | ImGuiWindowFlags_NoTitleBar | ImGuiWindowFlags_NoResize | ImGuiWindowFlags_NoMove | ImGuiWindowFlags_NoCollapse | ImGuiWindowFlags_NoBackground);
    ImGui::SetWindowSize(ImVec2(800, 400));
    ImGui::SetWindowPos(ImVec2(240, 210));

    // Title
    ImGui::SetWindowFontScale(2.0f);
    ImVec2 windowSize = ImGui::GetWindowSize();
    ImVec2 textSize = ImGui::CalcTextSize("TINY FOOTBALL");
    ImGui::SetCursorPosX((windowSize.x - textSize.x) * 0.5f);
    ImGui::SetCursorPosY(45.0f);
    ImGui::TextColored(ImVec4(1.0f, 1.0f, 1.0f, 1.0f), "TINY FOOTBALL");

    // Start button
    ImGui::SetWindowFontScale(1.5f);
    ImVec2 buttonSize = ImVec2(400, 75);
    ImGui::SetCursorPosX((windowSize.x - buttonSize.x) * 0.5f);
    ImGui::SetCursorPosY(150.0f);
    ImGui::PushStyleColor(ImGuiCol_ButtonHovered, ImVec4(0.8f, 0.8f, 0.8f, 1.0f));
    if (ImGui::Button("START", buttonSize))
    {
        state = GameState::NEW_GAME;
        startTime = std::chrono::steady_clock::now();
    }

    // Quit button
    ImGui::SetWindowFontScale(1.0f);
    buttonSize = ImVec2(300, 50);
    ImGui::SetCursorPosX((windowSize.x - buttonSize.x) * 0.5f);
    ImGui::SetCursorPosY(240.0f);
    if (ImGui::Button("QUIT", buttonSize))
    {
        state = GameState::QUIT;
        game_running = false;
    }

    ImGui::PopStyleColor();

    ImGui::End();
}
