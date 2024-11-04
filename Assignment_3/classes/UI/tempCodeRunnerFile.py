def playBackgroundMusic(self):
        if self.background_music_is_on:
            SoundPlayer.get_instance().set_music_volume(1.0)
        else:
            SoundPlayer.get_instance().set_music_volume(0.0)