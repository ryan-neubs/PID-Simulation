import json
from typing import ClassVar
class Servo:
    with open("setup.json", "r", encoding="utf-8") as file:
        servo_properties: dict = json.load(file)["Servo"]

    DEGREES_PER_SECOND: ClassVar[float] = servo_properties["Degrees Per Second"]
    ANGLE_LIMIT: ClassVar[float] = servo_properties["Angle Limit (deg)"]
    SIMULATOR_STEP: float = 0.02
    SERVO_TAU: float = 0.04

    current_angle: float = 0.0

    def tilt(self, controller_output) -> None:
        new_angle = self.current_angle + ((controller_output - self.current_angle) * self.SIMULATOR_STEP / self.SERVO_TAU)
        limit = self.ANGLE_LIMIT
        self.current_angle = max(-limit, min(new_angle, limit))