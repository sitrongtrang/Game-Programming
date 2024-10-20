#include "utils.h"
#include <cstdlib> 

float randRange(float min, float max) {
    // Generate a random float between min and max
    float scale = static_cast<float>(rand()) / RAND_MAX; // Scale to 0-1
    return min + scale * (max - min); // Scale to [min, max]
}

void RenderRectangle(float rect_x, float rect_y, float width, float height) {
    glBegin(GL_QUADS);                               // Start drawing a quad (rectangle)
    glColor3f(0.0f, 1.0f, 0.0f);                     // Green color
    glVertex2f(rect_x - width/2, rect_y - height/2); // Bottom-left
    glVertex2f(rect_x + width/2, rect_y - height/2); // Bottom-right
    glVertex2f(rect_x + width/2, rect_y + height/2); // Top-right
    glVertex2f(rect_x - width/2, rect_y + height/2); // Top-left
    glEnd();
}

void RenderCircle(float circ_x, float circ_y, float radius, int num_segments) {
    glBegin(GL_TRIANGLE_FAN); // Using a triangle fan to create a filled circle
    glVertex2f(circ_x, circ_y);        // Center of the circle

    for (int i = 0; i <= num_segments; i++) {
        float theta = 2.0f * 3.14159265358979323846 * float(i) / float(num_segments); // Current angle
        float x = radius * cosf(theta);                             // X coordinate
        float y = radius * sinf(theta);                             // Y coordinate
        glVertex2f(circ_x + x, circ_y + y);                         // Define the vertex
    }

    glEnd();
}

SDL_FPoint* getFootballerInitPos(float charX, float charY, float radius) {

    SDL_FPoint* footballers = new SDL_FPoint[NUM_FOOTBALLER];

    float angleIncrement = 2 * PI / NUM_FOOTBALLER; 

    for (int i = 0; i < NUM_FOOTBALLER; ++i) {
        float angle = i * angleIncrement;

        footballers[i].x = charX + radius * cos(angle);
        footballers[i].y = charY + radius * sin(angle);
    }

    return footballers;
}

bool sphere_sphereCollision(SDL_FPoint center1, float radius1, SDL_FPoint center2, float radius2) {
    float center_dist_squared = (center1.x - center2.x) * (center1.x - center2.x) + (center1.y - center2.y) * (center1.y - center2.y);
    float sum_rad = radius1 + radius2;
    return center_dist_squared <= sum_rad * sum_rad;
}

bool sphere_rectCollision(SDL_FPoint center1, float radius, SDL_FPoint center2, float width, float height) {
    float half_width = width / 2;
    float half_height = height / 2;

    float closest_x = std::max(center2.x - half_width, std::min(center1.x, center2.x + half_width));
    float closest_y = std::max(center2.y - half_height, std::min(center1.y, center2.y + half_height));

    float distance_x = center1.x - closest_x;
    float distance_y = center1.y - closest_y;

    if ((distance_x * distance_x + distance_y * distance_y) < (radius * radius))
        return true;
    return false;
}


bool rect_rectCollision(SDL_FPoint center1, float width1, float height1, SDL_FPoint center2, float width2, float height2) {
    float half_width1 = width1 / 2;
    float half_height1 = height1 / 2;
    float half_width2 = width2 / 2;
    float half_height2 = height2 / 2;
    
    if (std::abs(center1.x - center2.x) < half_width1 + half_width2 
        && std::abs(center1.y - center2.y) < half_height1 + half_height2)
        return true;
    return false;
}