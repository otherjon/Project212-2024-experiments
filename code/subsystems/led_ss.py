import logging
logger = logging.getLogger('LED-subsystem')

import wpilib
import commands2

class LED_5v_Subsystem(commands2.Subsystem):
    """
    This class represents a subsystem of individually addressable LEDs.

    The following are all equivalent:
     * addressable LED strip
     * individually addressable LED strip
     * 5-volt LED strip
     * three-wire LED strip
     * different LEDs can be set to different colors at the same time

    THE OPPOSITE can be described with the following equivalent terms:
     * 12-volt LED strip
     * four-wire LED strip
     * LED strip that *requires* a Blinkin-style controller
     * all LEDs must be the same color (which can change, but all LEDs change)
    """
    def __init__(self, pwm_port, speed=1.0, length=20) -> None:
        super().__init__()
        self.length = length
        self.port = pwm_port
        self.data = self.rainbow(self.length)
        self.leds = wpilib.AddressableLED(self.port)
        self.speed = speed
        self.timer = wpilib.Timer()
        self.timer.start()
        
        self.leds.setLength(self.length)
        self.leds.setData(self.data)
        self.leds.start()
        logger.info("Initialized LED subsystem")

    @classmethod
    def rainbow(cls, length):
        colors = ((255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0),
                  (0, 0, 255), (102, 0, 255), (255, 0, 255))

        result = []
        for i in range(length):
            color = colors[i % len(colors)]
            result.append(wpilib.AddressableLED.LEDData(*color))

        return result

    @classmethod
    def off(cls, length):
        result = []
        for i in range(length):
            result.append(wpilib.AddressableLED.LEDData(0, 0, 0))
        return result

        #wpilib.SmartDashboard.putData("LED+1", IncrementLEDCommand(self))
        #wpilib.SmartDashboard.putData("LED-1", DecrementLEDCommand(self))
        #wpilib.SmartDashboard.putData("LED+10", BigIncrementLEDCommand(self))
        #wpilib.SmartDashboard.putData("LED-10", BigDecrementLEDCommand(self))

    def teleopInit(self):
        self.data = self.rainbow(self.length)

    def disabledInit(self):
        self.data = self.off(self.length)

    def periodic(self):
        if self.timer.advanceIfElapsed(self.speed):
            logger.info("Updating LED pattern")
            self.data = self.data[1:] + [self.data[0]]
            self.leds.setData(self.data)
