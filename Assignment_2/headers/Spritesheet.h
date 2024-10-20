#ifndef SPRITESHEET_H
#define SPRITESHEET_H

#include "Constant.h"
#include <GL/gl.h> // Include OpenGL headers

class Spritesheet {
private:
    SDL_Rect m_clip;     // Clipping rectangle for sprites
    GLuint m_texture;    // OpenGL texture ID
    int m_row;           // Number of rows in the sprite sheet
    int m_column;        // Number of columns in the sprite sheet
    
    int frame;           // Current frame index
    int MAX_FRAME ; // Total number of frames in the spritesheet
    float frameDuration; // Duration for each frame
    float animationTime; // Time accumulator for animation
public:
    // Constructor
    Spritesheet(const char* path, int row, int column, int max_frame, float frameDuration);
    // Destructor
    ~Spritesheet();

    // Select a specific sprite
    void select_sprite(int x, int y);
    // Draw the selected sprite at the specified position
    void draw(float x, float y, float width, float height);

    void update(float deltaTime);
};

#endif // SPRITESHEET_H
