#include "Spritesheet.h"
#include <iostream>
#include <GL/gl.h>
#include <GL/glu.h> // Include GL and GLU headers

Spritesheet::Spritesheet(const char* path, int row, int column)
    : m_texture(0), m_row(row), m_column(column)
{
    // Load the image into a surface
    SDL_Surface* tempSurface = IMG_Load(path);
    if (!tempSurface) {
        std::cerr << "Failed to load sprite sheet: " << IMG_GetError() << std::endl;
        return;
    }

    
    // Create a texture from the loaded surface
    glGenTextures(1, &m_texture);

    

    if (glGetError() != GL_NO_ERROR || m_texture == 0) {
        std::cerr << "Failed to generate OpenGL texture." << std::endl;
        SDL_FreeSurface(tempSurface);
        return;
    }

    glBindTexture(GL_TEXTURE_2D, m_texture);

    // Set texture parameters (texture filtering)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

    // Set texture wrapping mode (optional, adjust if needed)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);

    // Load the texture into OpenGL
    int mode = tempSurface->format->BytesPerPixel == 4 ? GL_RGBA : GL_RGB;
    glTexImage2D(GL_TEXTURE_2D, 0, mode, tempSurface->w, tempSurface->h, 0, mode, GL_UNSIGNED_BYTE, tempSurface->pixels);

    // Set up the clipping rectangle based on the sprite sheet layout
    m_clip.w = tempSurface->w / column;
    m_clip.h = tempSurface->h / row;

    // Free the SDL surface after loading it to OpenGL
    SDL_FreeSurface(tempSurface);

    std::cout << "Sprite sheet loaded successfully." << std::endl;
}

Spritesheet::~Spritesheet() {
    // Delete OpenGL texture if it was created
    if (m_texture) {
        glDeleteTextures(1, &m_texture);
        m_texture = 0;
    }
}

// Select the sprite at row `x` and column `y`
void Spritesheet::select_sprite(int x, int y) {
    if (x >= m_row || y >= m_column) {
        std::cerr << "Sprite selection out of bounds: (" << x << ", " << y << ")" << std::endl;
        return;
    }

    // Calculate the position of the selected sprite in the sheet
    m_clip.x = x * m_clip.w;
    m_clip.y = y * m_clip.h;
}

// Draw the selected sprite at position `x`, `y` with size `width`, `height`
void Spritesheet::draw(float x, float y, float width, float height) {
    if (m_texture == 0) {
        std::cerr << "No texture to draw." << std::endl;
        return;
    }

    glEnable(GL_TEXTURE_2D);
    glBindTexture(GL_TEXTURE_2D, m_texture); // Make sure this texture is valid

    // Calculate texture coordinates
    float texLeft = static_cast<float>(m_clip.x) / (m_clip.w * m_column);
    float texRight = static_cast<float>(m_clip.x + m_clip.w) / (m_clip.w * m_column);
    float texTop = static_cast<float>(m_clip.y) / (m_clip.h * m_row);
    float texBottom = static_cast<float>(m_clip.y + m_clip.h) / (m_clip.h * m_row);
    
    float temp = texTop;
    texTop = texBottom;
    texBottom = temp;

    // Draw the sprite using textured quads
    glBegin(GL_QUADS);
        // Specify the vertices and texture coordinates
        glTexCoord2f(texLeft, texTop); glVertex2f(x, y);                    // Top-left
        glTexCoord2f(texRight, texTop); glVertex2f(x + width, y);           // Top-right
        glTexCoord2f(texRight, texBottom); glVertex2f(x + width, y + height); // Bottom-right
        glTexCoord2f(texLeft, texBottom); glVertex2f(x, y + height);        // Bottom-left
    glEnd();

    glBindTexture(GL_TEXTURE_2D, 0);
    glDisable(GL_TEXTURE_2D);
}
