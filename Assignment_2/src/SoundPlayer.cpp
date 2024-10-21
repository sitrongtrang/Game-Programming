#include "SoundPlayer.h"
#include <iostream>
#include <algorithm>

SoundPlayer* SoundPlayer::instance = nullptr;

SoundPlayer* SoundPlayer::getInstance() {
    if (instance == nullptr) {
        instance = new SoundPlayer();
    }
    return instance;
}

SoundPlayer::SoundPlayer() : backgroundMusic(nullptr), audioDevice(0) {}

SoundPlayer::~SoundPlayer() {
    cleanup();
}

bool SoundPlayer::init() {
    if (SDL_Init(SDL_INIT_AUDIO) < 0) {
        std::cerr << "Failed to initialize SDL audio: " << SDL_GetError() << std::endl;
        return false;
    }

    SDL_AudioSpec desiredSpec;
    SDL_zero(desiredSpec);
    desiredSpec.freq = 44100;
    desiredSpec.format = AUDIO_S16; 
    desiredSpec.channels = 2;
    desiredSpec.samples = 4096;
    desiredSpec.callback = audioCallback;
    desiredSpec.userdata = this;

    audioDevice = SDL_OpenAudioDevice(NULL, 0, &desiredSpec, NULL, 0);
    if (!audioDevice) {
        std::cerr << "Failed to open audio device: " << SDL_GetError() << std::endl;
        return false;
    }

    SDL_PauseAudioDevice(audioDevice, 0); // Start playing audio
    return true;
}

void SoundPlayer::loadSound(const std::string& soundName, const std::string& filePath) {
    Sound sound;

    if (SDL_LoadWAV(filePath.c_str(), &sound.spec, &sound.buffer, &sound.length) == NULL) {
        std::cerr << "Failed to load sound: " << filePath << " SDL Error: " << SDL_GetError() << std::endl;
        return;
    }

    sound.position = 0;
    sounds[soundName] = sound;
    std::cout << "Loaded sound: " << soundName << std::endl; 
}

void SoundPlayer::playSound(const std::string& soundName) {
    if (sounds.find(soundName) != sounds.end()) {
        Sound* sound = &sounds[soundName];
        sound->position = 0; // Start from the beginning
        playingSounds.push_back(sound);
        //std::cout << "Playing sound: " << soundName << std::endl; 
    } else {
        std::cerr << "Sound not found: " << soundName << std::endl;
    }
}

void SoundPlayer::loadBackgroundMusic(const std::string& filePath) {
    Sound sound;
    if (SDL_LoadWAV(filePath.c_str(), &sound.spec, &sound.buffer, &sound.length) == NULL) {
        std::cerr << "Failed to load background music: " << filePath << " SDL Error: " << SDL_GetError() << std::endl;
        return;
    }
    sound.position = 0;
    backgroundMusic = new Sound(sound); 
}

void SoundPlayer::playBackgroundMusic() {
    if (backgroundMusic) {
        playingSounds.push_back(backgroundMusic); // Add background music to playing sounds
        std::cout << "Playing background music." << std::endl; 
    }
}

void SoundPlayer::stopBackgroundMusic() {
    playingSounds.erase(std::remove(playingSounds.begin(), playingSounds.end(), backgroundMusic), playingSounds.end());
}

void SoundPlayer::audioCallback(void* userdata, Uint8* stream, int len) {
    SoundPlayer* player = reinterpret_cast<SoundPlayer*>(userdata);

    SDL_memset(stream, 0, len); // Clear the stream

    // Loop through all playing sounds
    for (auto it = player->playingSounds.begin(); it != player->playingSounds.end(); ) {
        Sound* sound = *it;
        Uint32 remaining = sound->length - sound->position;
        Uint32 bytesToWrite = (remaining < (Uint32)len) ? remaining : (Uint32)len;

        SDL_MixAudioFormat(stream, sound->buffer + sound->position, AUDIO_S16, bytesToWrite, SDL_MIX_MAXVOLUME);

        sound->position += bytesToWrite;

        if (sound->position >= sound->length) {
            if (sound == player->backgroundMusic) {
                // Loop background music
                sound->position = 0;
            } else {
                // Stop non-background sounds
                it = player->playingSounds.erase(it);
                continue;
            }
        }

        ++it;
    }
}

void SoundPlayer::cleanup() {
    for (auto& pair : sounds) {
        SDL_FreeWAV(pair.second.buffer);
    }
    sounds.clear();

    if (backgroundMusic) {
        SDL_FreeWAV(backgroundMusic->buffer);
        delete backgroundMusic;
        backgroundMusic = nullptr;
    }

    if (audioDevice) {
        SDL_CloseAudioDevice(audioDevice);
    }
}
