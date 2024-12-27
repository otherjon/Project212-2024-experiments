import logging
logger = logging.getLogger("LED commands")

import commands2
from commands2.cmd import runOnce

class ChangeLEDCommand(commands2.Command):
    delta = 0  # change this in subclasses

    def __init__(self, led_ss):
      self.led_ss = led_ss

    def initialize(self):
        proposed_setting = self.led_ss.setting + self.delta
        if proposed_setting >= -1 and proposed_setting <= 1:
            self.led_ss.setting = proposed_setting
            logger.info(f"{self.delta:+}, new setting = {proposed_setting}")
        else:
            logger.info(f"Setting out of range, staying at {self.led_ss.setting}")
            self.cancel()

    def execute(self):
        pass

    def isFinished(self):
        return True


class IncrementLEDCommand(ChangeLEDCommand):
    delta = 1

class DecrementLEDCommand(ChangeLEDCommand):
    delta = -1

class BigIncrementLEDCommand(ChangeLEDCommand):
    delta = 10

class BigDecrementLEDCommand(ChangeLEDCommand):
    delta = -10
