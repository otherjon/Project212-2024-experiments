import wpilib
import wpimath.controller

import commands2
import commands2.cmd
import commands2.button

import constants
import subsystems.ir_sensor_ss
import commands.turntoangle
import commands.turntoangleprofiled


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
        # The robot's subsystems
        self.ir_sensor = subsystems.ir_sensor_ss.InfraredSensorSubsystem()

        # The driver's controller.  See:
        # https://robotpy.readthedocs.io/projects/commands-v2/en/latest/commands2.button/CommandXboxController.html#commands2.button.CommandXboxController
        self.stick = commands2.button.CommandXboxController(
            constants.OIConstants.kDriverControllerPort
        )

        # Configure the button bindings
        self.configureButtonBindings()


    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings.  Buttons can
        be created via the button factories on
        commands2.button.CommandGenericHID or one of its subclasses
        (commands2.button.CommandJoystick or
        command2.button.CommandXboxController).
        """
        # Drive at half speed when the right bumper is held
        self.stick.rightBumper().onTrue(
            commands2.InstantCommand(
                (lambda: self.ir_sensor.do_something()), [self.ir_sensor]
            )
        ).onFalse(
            commands2.InstantCommand(
                (lambda: self.ir_sensor.do_something()), [self.ir_sensor]
            )
        )

        # Stabilize robot to drive straight with gyro when left bumper is held
        self.stick.A().whileTrue(
            commands2.InstantCommand(
                (lambda: self.ir_sensor.do_something()), [self.ir_sensor]
            )
        )


    def getAutonomousCommand(self) -> commands2.Command:
        """
        Use this to pass the autonomous command to the main :class:`.Robot`
        class.

        :returns: the command to run in autonomous mode
        """
        return commands2.InstantCommand()
