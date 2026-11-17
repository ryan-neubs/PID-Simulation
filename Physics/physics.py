from Physics.ball import Ball
from Control.servo import Servo
import math

GRAVITY: float = 9810 # 9810mm/s^2 - Multiply the gravity acceleration constant (9.81m/s^2) by 1000 since we have our measurements in mm
SIMULATOR_STEP: float = 0.02 # Seconds per simulator step

class PhysicsLoop:
    """Represents the physical state of the system between each step of the simulator"""

    def __init__(self, ball: Ball, servo: Servo) -> None:
        self.ball: Ball = ball
        self.servo: Servo = servo

    def calculate_ball_acceleration(self) -> None:
        self.ball.acceleration = (
            (5/7) * GRAVITY * math.sin(math.radians(self.servo.current_angle)) / (
                self.ball.MASS_GRAMS + self.ball.ROTATIONAL_INERTIA / self.ball.RADIUS_MM ** 2
            )
        )

    def calculate_ball_velocity(self) -> None:
        if (abs(self.ball.lateral_offset_mm) == 100):
            self.ball.velocity = 0
        else:
            prev_velocity: float = self.ball.velocity
            self.ball.velocity = prev_velocity + self.ball.acceleration * SIMULATOR_STEP

    def calculate_ball_position(self) -> None:
        prev_position: float = self.ball.lateral_offset_mm
        self.ball.lateral_offset_mm = prev_position + (self.ball.velocity * SIMULATOR_STEP) + (0.5 * self.ball.acceleration * (SIMULATOR_STEP**2)) 

    def calculate_ball_height(self) -> None:
        self.ball.height_mm = -self.ball.lateral_offset_mm * math.sin(math.radians(self.servo.current_angle))

    def step(self) -> None:
        self.calculate_ball_acceleration()
        self.calculate_ball_position()
        self.calculate_ball_velocity()
        self.calculate_ball_height()