#include "Spritesheet.h"
#include <iostream> 

Spritesheet::Spritesheet(char const *path, int row, int column) 
    : m_spritesheet_image(nullptr) {  // Initialize m_spritesheet_image to nullptr
    // Load the image from file
    m_spritesheet_image = IMG_Load(path);
    
    // Error handling for failed image load
    if (!m_spritesheet_image) {
        std::cerr << "Failed to load sprite sheet: " << IMG_GetError() << std::endl;
        return;  // Return early if the image failed to load
    }

    // Ensure no division by zero
    if (row == 0 || column == 0) {
        std::cerr << "Invalid row/column values (must be non-zero)" << std::endl;
        return;
    }

    // Set up the clipping rectangle dimensions
    m_clip.w = m_spritesheet_image->w / column;
    m_clip.h = m_spritesheet_image->h / row;

    
}

Spritesheet::~Spritesheet() {
    // Free the image surface only if it was loaded successfully
    if (m_spritesheet_image) {
        SDL_FreeSurface(m_spritesheet_image);
    }
}

// Get sprite in row x and col y
void Spritesheet::select_sprite(int x, int y) {
    // Calculate the position of the selected sprite in the sheet
    m_clip.x = x * m_clip.w;
    m_clip.y = y * m_clip.h;
}

// Draw the selected sprite onto the window surface
void Spritesheet::draw(SDL_Surface *window_surface, SDL_Rect *position) {
    if (m_spritesheet_image) {
        
       // SDL_BlitSurface(m_spritesheet_image, &m_clip, window_surface, position);
       SDL_BlitSurface(m_spritesheet_image, NULL, window_surface, NULL);
    }
}
