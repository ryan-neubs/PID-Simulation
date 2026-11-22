import json
from typing import Any, Final

with open("setup.json", "r", encoding="utf-8") as file:
    SERVO_PROPERTIES: dict[str, Any] = json.load(file)["Servo"]

class Servo:
    """Represents the physical limits and tilting of the servo in the control loop"""
    
    # Physical constraints of the servo
    DEGREES_PER_SECOND: Final[float] = SERVO_PROPERTIES["Degrees Per Second"]
    ANGLE_LIMIT: Final[float] = SERVO_PROPERTIES["Angle Limit (deg)"]
    SERVO_RESPONSE_TIME_CONSTANT: Final[float] = (2 * ANGLE_LIMIT) / DEGREES_PER_SECOND

    current_angle: float = 0.0

    def tilt(self, angle: float) -> None:
        self.current_angle += angle