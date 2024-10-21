#ifndef SOUNDPLAYER_H
#define SOUNDPLAYER_H

#include <SDL2/SDL.h>
#include <string>
#include <map>
#include <vector>

struct Sound {
    SDL_AudioSpec spec;
    Uint8* buffer;
    Uint32 length;
    Uint32 position; // Tracks the current play position
};

class SoundPlayer {
public:
    static SoundPlayer* getInstance();

    bool init();
    void loadSound(const std::string& soundName, const std::string& filePath);
    void playSound(const std::string& soundName);
    void loadBackgroundMusic(const std::string& filePath);
    void playBackgroundMusic();
    void stopBackgroundMusic();
    void cleanup();

private:
    SoundPlayer();
    ~SoundPlayer();

    // Singleton enforcement
    SoundPlayer(const SoundPlayer&) = delete;
    SoundPlayer& operator=(const SoundPlayer&) = delete;

    static void audioCallback(void* userdata, Uint8* stream, int len);

    static SoundPlayer* instance;

    std::map<std::string, Sound> sounds;
    std::vector<Sound*> playingSounds; // Tracks all currently playing sounds
    Sound* backgroundMusic;
    SDL_AudioDeviceID audioDevice;
};

#endif // SOUNDPLAYER_H
