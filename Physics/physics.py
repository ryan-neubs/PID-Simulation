from Physics.ball import Ball
from Control.servo import Servo
import math
class PhysicsLoop:
    GRAVITY: float = 9810
    SIMULATOR_STEP: float = 0.02 # Seconds per simulator step

    def __init__(self, ball: Ball, servo: Servo):
        self.ball = ball
        self.servo = servo

    def calculate_ball_acceleration(self):
        self.ball.acceleration = (5/7) * self.GRAVITY * math.sin(math.radians(self.servo.current_angle))

    def calculate_ball_velocity(self):
        if (abs(self.ball.lateral_offset_mm) == 100):
            self.ball.velocity = 0
        else:
            prev_velocity: float = self.ball.velocity
            self.ball.velocity = prev_velocity + self.ball.acceleration * self.SIMULATOR_STEP

    def calculate_ball_position(self):
        prev_position: float = self.ball.lateral_offset_mm
        self.ball.lateral_offset_mm = prev_position + (self.ball.velocity * self.SIMULATOR_STEP) + (0.5 * self.ball.acceleration * (self.SIMULATOR_STEP**2)) 

    def calculate_ball_height(self):
        self.ball.height_mm = -self.ball.lateral_offset_mm * math.sin(math.radians(self.servo.current_angle))

    def step(self):
        self.calculate_ball_acceleration()
        self.calculate_ball_position()
        self.calculate_ball_velocity()
        self.calculate_ball_height()