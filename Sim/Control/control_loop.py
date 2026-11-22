from Sim.Control.servo import Servo
import json
from Sim.Physics.ball import Ball
from typing import Any

with open("setup.json", "r", encoding="utf-8") as file:
    SETUP_PROPERTIES: dict[str, Any] = json.load(file)
    GAINS: dict[str, float] = SETUP_PROPERTIES["Gains"]

# PID gains
PROPORTIONAL_GAIN: float = GAINS["Kp"]
INTEGRAL_GAIN: float = GAINS["Ki"]
DERIVATIVE_GAIN: float = GAINS["Kd"]

# Desired target offset
SETPOINT: float = SETUP_PROPERTIES["Variables"]["Setpoint"]

# Seconds between each step in the simulator
SIMULATOR_STEP: float = 0.02

class ControlLoop:
    """
    Represents the calculations done in each step of the PID controller
    """
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