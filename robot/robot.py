import wpilib
import commands2
import commands2.cmd

import container

class MyRobot(commands2.TimedCommandRobot):
    """
    Our default robot class, pass it to wpilib.run
    Command v2 robots are encouraged to inherit from TimedCommandRobot, which
    has an implementation of robotPeriodic which runs the scheduler for you
    """

    def robotInit(self) -> None:
        """
        This function is run when the robot is first started up and should
        be used for any initialization code.
        """
        self.autonomousCommand: typing.Optional[commands2.Command] = None

        # Instantiate our RobotContainer.  This will perform all our button
        # bindings, and put our autonomous chooser on the dashboard.
        #
        self.container = container.RobotContainer()

    def disabledInit(self) -> None:
        """
        This function is called once each time the robot enters Disabled mode.
        """
        pass

    def disabledPeriodic(self) -> None:
        """This function is called periodically when disabled"""
        pass

    def autonomousInit(self) -> None:
        """
        This autonomous runs the autonomous command selected by your
        RobotContainer class.
        """
        self.autonomousCommand = self.container.getAutonomousCommand()

        # schedule the autonomous command (example)
        if self.autonomousCommand is not None:
            self.autonomousCommand.schedule()
        else:
            wpilib.reportWarning("No autonomous command")

    def autonomousPeriodic(self) -> None:
        """This function is called periodically during autonomous"""

    def teleopInit(self) -> None:
        # This makes sure that the autonomous stops running when
        # teleop starts running. If you want the autonomous to
        # continue until interrupted by another command, remove
        # this line or comment it out.
        if self.autonomousCommand is not None:
            self.autonomousCommand.cancel()

    def teleopPeriodic(self) -> None:
        """This function is called periodically during operator control"""

    def testInit(self) -> None:
        # Cancels all running commands at the start of test mode
        commands2.CommandScheduler.getInstance().cancelAll()


if __name__ == "__main__":
    wpilib.run(MyRobot)
