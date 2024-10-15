#include "imgui.h"
#include "imgui_impl_sdl2.h"
#include "imgui_impl_opengl3.h"
#include <SDL.h>
#include <SDL_opengl.h>
#include <stdio.h>

// Game state variables
bool game_running = true;
float square_x = 0.0f;  // Square's X position
float square_y = 0.0f;  // Square's Y position
float square_size = 0.1f;  // Size of the square

// Function to update the game logic
void UpdateGame() {
    const Uint8* state = SDL_GetKeyboardState(NULL);
    if (state[SDL_SCANCODE_UP])
        square_y += 0.01f;  // Move up
    if (state[SDL_SCANCODE_DOWN])
        square_y -= 0.01f;  // Move down
    if (state[SDL_SCANCODE_LEFT])
        square_x -= 0.01f;  // Move left
    if (state[SDL_SCANCODE_RIGHT])
        square_x += 0.01f;  // Move right
}

// Function to render a simple square
void RenderSquare() {
    glBegin(GL_QUADS);  // Start drawing a quad (square)
    glColor3f(0.0f, 1.0f, 0.0f);  // Green color
    glVertex2f(square_x - square_size, square_y - square_size);  // Bottom-left
    glVertex2f(square_x + square_size, square_y - square_size);  // Bottom-right
    glVertex2f(square_x + square_size, square_y + square_size);  // Top-right
    glVertex2f(square_x - square_size, square_y + square_size);  // Top-left
    glEnd();
}

int main(int, char**) {
    // Initialize SDL
    if (SDL_Init(SDL_INIT_VIDEO | SDL_INIT_TIMER | SDL_INIT_GAMECONTROLLER) != 0) {
        printf("Error: %s\n", SDL_GetError());
        return -1;
    }

    // Set up OpenGL context and SDL window
    const char* glsl_version = "#version 130";
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_FLAGS, 0);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 3);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 0);

    SDL_Window* window = SDL_CreateWindow("Simple Game with ImGui", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 1280, 720, SDL_WINDOW_OPENGL | SDL_WINDOW_RESIZABLE);
    SDL_GLContext gl_context = SDL_GL_CreateContext(window);
    SDL_GL_MakeCurrent(window, gl_context);
    SDL_GL_SetSwapInterval(1);  // Enable vsync

    // Initialize Dear ImGui context
    IMGUI_CHECKVERSION();
    ImGui::CreateContext();
    ImGuiIO& io = ImGui::GetIO(); (void)io;
    ImGui::StyleColorsDark();

    // Set up ImGui for SDL and OpenGL
    ImGui_ImplSDL2_InitForOpenGL(window, gl_context);
    ImGui_ImplOpenGL3_Init(glsl_version);

    // Main loop
    SDL_Event event;
    while (game_running) {
        // Poll and handle SDL events
        while (SDL_PollEvent(&event)) {
            ImGui_ImplSDL2_ProcessEvent(&event);
            if (event.type == SDL_QUIT)
                game_running = false;
        }

        // Update game logic
        UpdateGame();

        // Start ImGui frame
        ImGui_ImplOpenGL3_NewFrame();
        ImGui_ImplSDL2_NewFrame();
        ImGui::NewFrame();

        // ImGui interface
        {
            ImGui::Begin("Game Controls");
            ImGui::Text("Use arrow keys to move the square.");
            ImGui::Text("Press 'ESC' to exit.");
            if (ImGui::Button("Exit"))
                game_running = false;
            ImGui::End();
        }

        // Render game objects
        glClear(GL_COLOR_BUFFER_BIT);
        RenderSquare();

        // Render ImGui
        ImGui::Render();
        ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());

        SDL_GL_SwapWindow(window);
    }

    // Cleanup
    ImGui_ImplOpenGL3_Shutdown();
    ImGui_ImplSDL2_Shutdown();
    ImGui::DestroyContext();

    SDL_GL_DeleteContext(gl_context);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
