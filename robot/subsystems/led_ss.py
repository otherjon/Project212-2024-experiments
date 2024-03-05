import logging
logger = logging.getLogger('LED-subsystem')

import wpilib
import commands2

from commands.led_commands import (
    IncrementLEDCommand, DecrementLEDCommand, BigIncrementLEDCommand,
    BigDecrementLEDCommand)


class Blinkin(wpilib.Spark):
    """
    The Blinkin class is exactly the same as the wpilib.Spark class, but with
    a more appropriate name for this purpose.  Otherwise, it works exactly like
    an old Spark (not SparkMAX) motor controller that uses PWM (pulse width
    modulation) to control the motor speed.

    See the Blinkin manual for more information:
      https://www.revrobotics.com/content/docs/REV-11-1105-UM.pdf
    """
    pass


class LEDSubsystem(commands2.Subsystem):
    def __init__(self, pwm_port) -> None:
        super().__init__()
        self.led_controller = Blinkin(pwm_port)
        self.setting = -0.99
        wpilib.SmartDashboard.putNumber("Blinkin value", self.setting)

        wpilib.SmartDashboard.putData("LED+1", IncrementLEDCommand(self))
        wpilib.SmartDashboard.putData("LED-1", DecrementLEDCommand(self))
        wpilib.SmartDashboard.putData("LED+10", BigIncrementLEDCommand(self))
        wpilib.SmartDashboard.putData("LED-10", BigDecrementLEDCommand(self))

    def periodic(self):
        self.led_controller.set(self.setting)
        wpilib.SmartDashboard.putNumber("Blinkin value", self.setting)
