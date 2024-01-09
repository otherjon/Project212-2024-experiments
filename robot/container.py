import wpilib
import wpilib.deployinfo
from wpiutil import SendableBuilder
from constants import Constants


class Sensor:
    """
    This class represents a simple digital or analog sensor, plugged into one
    of the RoboRIO's DIO or AIO ports respectively.
    """
    # SENSOR_CLASS must be a Sendable, since we call SmartDashboard.putData()
    # with it.
    #
    SENSOR_CLASS = None

    def __init__(self, io_port, name) -> None:
        """Create a new Sensor"""
        super().__init__()
        self.io_port = io_port
        self.sensor = self.SENSOR_CLASS(io_port)
        self.name = name
        #self.sensor.addChild("P212 Value", self.value())
        #wpilib.SmartDashboard.putData(f"{name} (#{io_port})", self.sensor)

    def initSendable(self, builder: SendableBuilder) -> None:
        builder.setSmartDashboardType("Subsystem")
        builder.addDoubleProperty(".value", lambda: self.value(), lambda: None)

    def value(self):
        pass


class DigitalSensor(Sensor):
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
    SENSOR_CLASS = wpilib.DigitalInput

    def __init__(self, dio_port, name, invert=False) -> None:
        """Create a new DigitalSensor"""
        super().__init__(dio_port, name)
        self.invert = invert

    def value(self):
        return not self.sensor.get() if self.invert else self.sensor.get()


class AnalogSensor(Sensor):
    """
    This class represents a simple analog sensor,
    plugged into one of the RoboRIO's Analog I/O (AIO) ports.  The sensor
    has no external inputs (just what's onboard the sensor), and produces a
    single continuous-voltage output.  Examples of these simple analog sensors
    include:
      * ultrasonic sensors
    """
    SENSOR_CLASS = wpilib.AnalogInput
    def __init__(self, aio_port, name, low=0.0, high=1.0, round=None,
                 scale=True) -> None:
        """Create a new AnalogSensor"""
        super().__init__(aio_port, name)
        self.low = low
        self.high = high
        self.round = round

    def raw_unscaled_value(self):
        return self.sensor.getVoltage()

    def battery_adjusted_value(self):
        v_batt = wpilib.RobotController.getVoltage5V()
        return self.raw_unscaled_value() / v_batt

    def value(self):
        tempval = self.low + (
            self.battery_adjusted_value() * (self.high - self.low))
        if self.round:
            tempval = int(tempval * 10**self.round) / 10**self.round
        return tempval


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
        self.limit_sw = DigitalSensor(Constants.LIMIT_SW_DIO, "Limit Switch")
        self.ir = DigitalSensor(Constants.IR_DIO, "IR Proximity", invert=True)
        self.breakbeam = DigitalSensor(Constants.BREAK_BEAM_DIO, "Break-Beam")
        self.hall = DigitalSensor(Constants.HALL_EFFECT_DIO, "Hall Effect", invert=True)
        conversion_to_inches = 512.0 / 2.54
        self.ultrasonic = AnalogSensor(
            Constants.ULTRASONIC_AIO, "Ultrasonic",
            low=0.0, high=conversion_to_inches, round=1)

    def updateSensorData(self):
        wpilib.SmartDashboard.putBoolean(
            "ASensorDemo.LimitSwitch", self.limit_sw.value())
        wpilib.SmartDashboard.putBoolean(
            "ASensorDemo.IRSensor", self.ir.value())
        wpilib.SmartDashboard.putBoolean(
            "ASensorDemo.HallEffectSensor", self.hall.value())
        wpilib.SmartDashboard.putBoolean(
            "ASensorDemo.BreakBeamSensor", self.breakbeam.value())
        wpilib.SmartDashboard.putNumber(
            "ASensorDemo.UltrasonicRangefinder", self.ultrasonic.value())
