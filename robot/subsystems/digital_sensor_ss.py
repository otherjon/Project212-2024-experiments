import wpilib
import commands2
import constants


class DigitalSensorSS(commands2.Subsystem):
    """
    This class represents a subsystem consisting of a simple digital sensor,
    plugged into one of the RoboRIO's Digital I/O (DIO) ports.  The sensor
    has no external inputs (just what's onboard the sensor), and produces a
    single binary output.  Examples of these simple digital sensors include:
      * limit switches
      * IR proximity sensors
      * Hall Effect sensors
      * break-beam sensors
    """
    def __init__(self, dio_port, name) -> None:
        """Create a new DigitalSensorSS"""
        super().__init__()
        self.dio_port = dio_port
        self.sensor = wpilib.DigitalInput(dio_port)
        self.name = name
        self.addChild(f"{name} sensor", self.sensor)
        wpilib.SmartDashboard.putData(f"{name} (#{dio_port})", self.sensor)

    def value(self):
        return self.sensor.get()
