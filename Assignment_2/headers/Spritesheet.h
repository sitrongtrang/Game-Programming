#ifndef SPRITESHEET_H
#define SPRITESHEET_H

#include "Constant.h"


class Spritesheet{
    private:
        SDL_Rect m_clip;
        SDL_Surface *m_spritesheet_image;

    public:
        Spritesheet(char const *path, int row, int column);
        ~Spritesheet();

        void select_sprite(int x, int y);
        void draw(SDL_Surface *window_surface, SDL_Rect* position);

};

#endif //SPRITESHEET_H