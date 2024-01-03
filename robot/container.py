import wpilib
import wpilib.deployinfo

import commands2
import commands2.cmd
import commands2.button

from constants import Constants
from subsystems.digital_sensor_ss import DigitalSensorSS


class RobotContainer:
    """
    This class is where the bulk of the robot should be declared.

    Since Command-based is a "declarative" paradigm, very little robot logic
    should actually be handled in the :class:`.Robot` periodic methods (other
    than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self):
        """
        The container for the robot.  Contains subsystems, OI devices, and
        commands.
        """
        self.deploy_data = wpilib.deployinfo.getDeployData()

        # The robot's subsystems
        self.limit_sw = DigitalSensorSS(Constants.LIMIT_SW_DIO, "Limit Switch")
        self.ir = DigitalSensorSS(Constants.IR_DIO, "IR Proximity")
        self.breakbeam = DigitalSensorSS(Constants.BREAK_BEAM_DIO, "Break-Beam")
        self.hall = DigitalSensorSS(Constants.HALL_EFFECT_DIO, "Hall Effect")


    def getAutonomousCommand(self) -> commands2.Command:
        """
        Use this to pass the autonomous command to the main :class:`.Robot`
        class.

        :returns: the command to run in autonomous mode
        """
        return commands2.InstantCommand()
