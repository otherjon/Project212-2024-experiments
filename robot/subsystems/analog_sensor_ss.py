import wpilib
import commands2
import constants
from wpiutil import SendableBuilder

class AnalogSensorSS(commands2.Subsystem):
    """
    This class represents a subsystem consisting of a simple analog sensor,
    plugged into one of the RoboRIO's Analog I/O (AIO) ports.  The sensor
    has no external inputs (just what's onboard the sensor), and produces a
    single continuous-voltage output.  Examples of these simple analog sensors
    include:
      * ultrasonic sensors
    """
    def __init__(self, aio_port, name, max_in=1.0, low=0.0, high=1.0,
                 scale=True) -> None:
        """Create a new AnalogSensorSS"""
        super().__init__()
        self.aio_port = aio_port
        self.sensor = wpilib.AnalogInput(aio_port)
        self.name = name
        self.max_in = max_in
        self.low = low
        self.high = high
        self.addChild(f"{name} sensor", self.sensor)
        wpilib.SmartDashboard.putData(f"{name} (#{aio_port})", self.sensor)

    def initSendable(self, builder: SendableBuilder) -> None:
        builder.setSmartDashboardType("Subsystem")
        builder.addDoubleProperty(".value", lambda: self.value(), lambda: None)

    def raw_unscaled_value(self):
        return self.sensor.get()

    def battery_adjusted_value(self):
        v_batt = wpilib.RobotController.getVoltage5V()
        return self.raw_unscaled_value * v_batt / 5.0

    def value(self):
      return self.low + (
        self.battery_adjusted_value() / self.max_in * (self.high - self.low))
