from Control.servo import Servo
import json
from Physics.ball import Ball

with open("setup.json", "r", encoding="utf-8") as file:
    setup_properties = json.load(file)
    gains = setup_properties["Gains"]

PROPORTIONAL_GAIN: float = gains["Kp"]
INTEGRAL_GAIN: float = gains["Ki"]
DERIVATIVE_GAIN: float = gains["Kd"]
SETPOINT: float = 25
SIMULATOR_STEP: float = 0.02 # Seconds per simulator step
class ControlLoop:
    prev_error: float = 0
    error_sum: float = 0

    def __init__(self, ball: Ball, servo: Servo):
        self.ball = ball
        self.servo = servo

    def step(self):
        curr_error = SETPOINT - self.ball.lateral_offset_mm
        self.error_sum += (curr_error * SIMULATOR_STEP)
        proportion: float = PROPORTIONAL_GAIN * curr_error
        integral: float = INTEGRAL_GAIN * self.error_sum
        derivative: float = DERIVATIVE_GAIN * ((curr_error - self.prev_error) / SIMULATOR_STEP)
        self.prev_error = curr_error
        self.servo.tilt(proportion + integral + derivative)