import wpilib
import constants
import commands2
import phoenix5

class MusicSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        self.instrument1 = phoenix5.TalonFX(constants.ELEC.motor1_CAN_ID)
        self.orch = phoenix5.Orchestra()
        self.orch.addInstrument(self.instrument1)

    def is_playing(self):
      return self.orch.isPlaying()

    def play_chrp_file(self, filename):
      self.orch.loadMusic(filename)
      self.orch.play()

    def stop_music(self):
      if self.orch.isPlaying():
        self.orch.stop()
