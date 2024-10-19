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
    glBindTexture(GL_TEXTURE_2D, m_texture);

    // Set texture parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

    // Load the texture into OpenGL
    int mode = tempSurface->format->BytesPerPixel == 4 ? GL_RGBA : GL_RGB;
    glTexImage2D(GL_TEXTURE_2D, 0, mode, tempSurface->w, tempSurface->h, 0, mode, GL_UNSIGNED_BYTE, tempSurface->pixels);

    // Free the SDL surface
    SDL_FreeSurface(tempSurface);

    // Set up the clipping rectangle
    m_clip.w = tempSurface->w / column;
    m_clip.h = tempSurface->h / row;
}

Spritesheet::~Spritesheet() {
    if (m_texture) {
        glDeleteTextures(1, &m_texture);
    }
}

// Get sprite in row x and col y
void Spritesheet::select_sprite(int x, int y) {
    // Calculate the position of the selected sprite in the sheet
    m_clip.x = x * m_clip.w;
    m_clip.y = y * m_clip.h;
}

// Draw the selected sprite onto the window surface using OpenGL
void Spritesheet::draw(float x, float y, float width, float height) {
    glEnable(GL_TEXTURE_2D);
    glBindTexture(GL_TEXTURE_2D, m_texture);

    // Calculate texture coordinates
    float texLeft = static_cast<float>(m_clip.x) / (m_clip.w * m_column);
    float texRight = static_cast<float>(m_clip.x + m_clip.w) / (m_clip.w * m_column);
    float texTop = static_cast<float>(m_clip.y) / (m_clip.h * m_row);
    float texBottom = static_cast<float>(m_clip.y + m_clip.h) / (m_clip.h * m_row);

    glBegin(GL_QUADS);
        // Specify the vertices and texture coordinates
        glTexCoord2f(texLeft, texTop); glVertex2f(x, y);                    // Top-left
        glTexCoord2f(texRight, texTop); glVertex2f(x + width, y);          // Top-right
        glTexCoord2f(texRight, texBottom); glVertex2f(x + width, y + height); // Bottom-right
        glTexCoord2f(texLeft, texBottom); glVertex2f(x, y + height);       // Bottom-left
    glEnd();

    glBindTexture(GL_TEXTURE_2D, 0);
    glDisable(GL_TEXTURE_2D);
}
