#include "utils.h"
#include <cstdlib> 

float randRange(float min, float max) {
    // Generate a random float between min and max
    float scale = static_cast<float>(rand()) / RAND_MAX; // Scale to 0-1
    return min + scale * (max - min); // Scale to [min, max]
}
