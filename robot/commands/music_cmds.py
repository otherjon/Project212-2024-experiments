import wpilib
import phoenix5
import commands2
from subsystems.music_ss import MusicSubsystem
import constants

class PlaySong (commands2.Command):
    def __init__(self, music_ss: MusicSubsystem, chrp_file: str) -> None:
        super().__init__()
        self.music_ss = music_ss
        self.addRequirements(music_ss)
        self.chrp_file = chrp_file

    def execute(self):
      if not self.music_ss.is_playing():
        self.music_ss.play_chrp_file(self.chrp_file)

    def isFinished(self):
        return self.music_ss.is_playing()

    def end(self, interrupted: bool):
        self.music_ss.stop_music()

