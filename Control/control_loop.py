from Control.servo import Servo
import json
from Physics.ball import Ball
from typing import Any

with open("setup.json", "r", encoding="utf-8") as file:
    setup_properties: dict[str, Any] = json.load(file)
    gains: dict[str, float] = setup_properties["Gains"]

PROPORTIONAL_GAIN: float = gains["Kp"]
INTEGRAL_GAIN: float = gains["Ki"]
DERIVATIVE_GAIN: float = gains["Kd"]
SETPOINT: float = setup_properties["Variables"]["Setpoint"]
SIMULATOR_STEP: float = 0.02 # Seconds per simulator step

class ControlLoop:
    prev_error: float = 0.0
    error_sum: float = 0.0

    def __init__(self, ball: Ball, servo: Servo) -> None:
        self.ball: Ball = ball
        self.servo: Servo = servo

    def step(self) -> None:
        command: float = self.calculate_PID_command()
        angle_adjustment: float = self.calculate_angle_update(command)
        self.servo.tilt(angle_adjustment)

    def calculate_PID_command(self) -> float:
        curr_error: float = SETPOINT - self.ball.lateral_offset_mm
        self.error_sum += (curr_error * SIMULATOR_STEP)

        proportion: float = PROPORTIONAL_GAIN * curr_error
        integral: float = INTEGRAL_GAIN * self.error_sum
        derivative: float = DERIVATIVE_GAIN * ((curr_error - self.prev_error) / SIMULATOR_STEP)

        self.prev_error = curr_error

        return proportion + integral + derivative

    def calculate_angle_update(self, command: float) -> float:
        current: float = self.servo.current_angle
        requested_delta: float = (command - current) * SIMULATOR_STEP / self.servo.SERVO_RESPONSE_TIME_CONSTANT
        target: float = max(-self.servo.ANGLE_LIMIT, min(current + requested_delta, self.servo.ANGLE_LIMIT))
        
        return target - current