import json
from typing import ClassVar, Any

class Servo:
    with open("setup.json", "r", encoding="utf-8") as file:
        servo_properties: dict[str, Any] = json.load(file)["Servo"]

    DEGREES_PER_SECOND: float = servo_properties["Degrees Per Second"]
    ANGLE_LIMIT: float = servo_properties["Angle Limit (deg)"]
    SERVO_RESPONSE_TIME_CONSTANT: float = (2 * ANGLE_LIMIT) / DEGREES_PER_SECOND

    current_angle: float = 0.0

    def tilt(self, angle: float) -> None:
        self.current_angle += angle