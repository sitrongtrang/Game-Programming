#ifndef SPRITESHEET_H
#define SPRITESHEET_H

#include "Constant.h"


class Spritesheet{
    private:
        SDL_Rect m_clip;
        SDL_Texture *m_texture;
        SDL_Renderer *m_renderer;

    public:
        Spritesheet(char const *path, SDL_Renderer *m_renderer, int row, int column);
        ~Spritesheet();

        void select_sprite(int x, int y);
        void draw(SDL_Rect* position);

};

#endif //SPRITESHEET_H