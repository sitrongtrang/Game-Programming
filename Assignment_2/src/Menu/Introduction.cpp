#include "../headers/menu/Introduction.h"

bool fade_in = true;
float fade_speed = 0.01f;
float splash_alpha = 0.0f;

void renderIntroduction(SDL_Renderer *renderer, const char *imagePath, int displayTimeMs)
{
    SDL_Surface *icon_surface = IMG_Load(imagePath);
    if (!icon_surface)
    {
        printf("Error: %s\n", IMG_GetError());
        return;
    }

    SDL_Texture *texture = SDL_CreateTextureFromSurface(renderer, icon_surface);
    SDL_FreeSurface(icon_surface);
    if (!texture)
    {
        printf("Error: %s\n", SDL_GetError());
        return;
    }

    SDL_SetTextureBlendMode(texture, SDL_BLENDMODE_BLEND);

    int totalTimeMs = 0;
    Uint32 lastTime = SDL_GetTicks();

    while (totalTimeMs <= displayTimeMs)
    {
        Uint32 currentTime = SDL_GetTicks();
        Uint32 deltaTime = currentTime - lastTime;
        lastTime = currentTime;
        totalTimeMs += deltaTime;

        if (fade_in)
        {
            splash_alpha += fade_speed;
            if (splash_alpha >= 1.0f)
            {
                splash_alpha = 1.0f;
                fade_in = false;
            }
        }

        else
        {
            splash_alpha -= fade_speed;
            if (splash_alpha <= 0.0f)
            {
                splash_alpha = 0.0f;
                break;
            }
        }

        // Clear the screen
        SDL_RenderClear(renderer);

        // Set the texture alpha
        SDL_SetTextureAlphaMod(texture, (Uint8)(splash_alpha * 255));

        // Get the window size
        int window_width, window_height;
        SDL_GetRendererOutputSize(renderer, &window_width, &window_height);

        // Define the destination rectangle for the texture
        SDL_Rect destRect = {0, 0, window_width, window_height};

        // Render the texture to the screen
        SDL_RenderCopy(renderer, texture, NULL, &destRect);
        SDL_RenderPresent(renderer);

        // Small delay for smooth fade effect
        SDL_Delay(16); // Roughly 60 FPS
    }

    // Destroy the texture
    SDL_DestroyTexture(texture);
}
