import wpilib
import container

class MyRobot(wpilib.TimedRobot):
    """
    Our default robot class, pass it to wpilib.run
    """

    def robotInit(self) -> None:
        """
        This function is run when the robot is first started up and should
        be used for any initialization code.
        """

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
        wpilib.reportWarning("No autonomous command")

    def autonomousPeriodic(self) -> None:
        """This function is called periodically during autonomous"""
        pass

    def teleopInit(self) -> None:
        pass

    def teleopPeriodic(self) -> None:
        """This function is called periodically during operator control"""
        self.container.updateSensorData()

    def testInit(self) -> None:
        pass

if __name__ == "__main__":
    wpilib.run(MyRobot)
