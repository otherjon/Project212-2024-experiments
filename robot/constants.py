from collections import namedtuple

data = {
  "LIMIT_SW_DIO": 0,
  "IR_DIO": 1,
  "BREAK_BEAM_DIO": 2,
  "HALL_EFFECT_DIO": 3,

  "ULTRASONIC_AIO": 0,

  "JOYSTICK_PORT": 0,
}

_ConstantsClass = namedtuple("ConstantsClass", data.keys())
Constants = _ConstantsClass(**data)
