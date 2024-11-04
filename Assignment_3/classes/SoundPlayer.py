
import pygame
import os

class SoundPlayer:
    _instance = None

    @staticmethod
    def get_instance():
      
        if SoundPlayer._instance is None:
            SoundPlayer()
        return SoundPlayer._instance

    def __init__(self):
       
        if SoundPlayer._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            SoundPlayer._instance = self
            pygame.mixer.init()
            self.sounds = {}
            self.music_volume = 0.5
            self.sound_volume = 0.5

    def load_sound(self, sound_name, file_path):
        """Loads a sound file for future playback."""
        if os.path.exists(file_path):
            self.sounds[sound_name] = pygame.mixer.Sound(file_path)
            self.sounds[sound_name].set_volume(self.sound_volume)
        else:
            raise FileNotFoundError(f"Sound file not found: {file_path}")

    def play_sound(self, sound_name, loops=0):
        """Plays a loaded sound effect."""
        if sound_name in self.sounds:
            self.sounds[sound_name].play(loops=loops)
        else:
            print(f"Sound '{sound_name}' not loaded.")

    def stop_sound(self, sound_name):
        """Stops a specific sound effect."""
        if sound_name in self.sounds:
            self.sounds[sound_name].stop()
        else:
            print(f"Sound '{sound_name}' not loaded.")

    def play_music(self, file_path, loops=-1):
        """Plays background music."""
        if os.path.exists(file_path):
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.set_volume(self.music_volume)
            pygame.mixer.music.play(loops=loops)
        else:
            raise FileNotFoundError(f"Music file not found: {file_path}")

    def stop_music(self):
        """Stops the background music."""
        pygame.mixer.music.stop()

    def set_music_volume(self, volume):
        """Sets the volume for background music."""
        self.music_volume = volume
        pygame.mixer.music.set_volume(volume)

    def set_sound_volume(self, volume):
        """Sets the volume for all sound effects."""
        self.sound_volume = volume
        for sound in self.sounds.values():
            sound.set_volume(volume)
