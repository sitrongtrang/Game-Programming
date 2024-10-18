#include "Spritesheet.h"
#include <iostream> 

Spritesheet::Spritesheet(char const *path, SDL_Renderer *renderer, int row, int column) 
    : m_texture(nullptr), m_renderer(renderer){  // Initialize m_spritesheet_image to nullptr
   
    // Load the image into a texture
    SDL_Surface* tempSurface = IMG_Load(path);
    if (!tempSurface) {
        std::cerr << "Failed to load sprite sheet: " << IMG_GetError() << std::endl;
        return;
    }

    // Create a texture from the loaded surface
    m_texture = SDL_CreateTextureFromSurface(renderer, tempSurface);
    SDL_FreeSurface(tempSurface);  // We don't need the surface anymore, free it

    if (!m_texture) {
        std::cerr << "Failed to create texture from surface: " << SDL_GetError() << std::endl;
        return;
    }

    // Set up the clipping rectangle
    m_clip.w = tempSurface->w / column;
    m_clip.h = tempSurface->h / row;

    
}

Spritesheet::~Spritesheet() {

    if (m_texture) {
        SDL_DestroyTexture(m_texture);
    }
}

// Get sprite in row x and col y
void Spritesheet::select_sprite(int x, int y) {
    // Calculate the position of the selected sprite in the sheet
    m_clip.x = x * m_clip.w;
    m_clip.y = y * m_clip.h;
    
}

// Draw the selected sprite onto the window surface
void Spritesheet::draw(SDL_Rect *position) {
    SDL_RenderCopy(m_renderer, m_texture, &m_clip, position);    
}
