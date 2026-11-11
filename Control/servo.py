import json
from typing import ClassVar
class Servo:
    with open("setup.json", "r", encoding="utf-8") as file:
        servo_properties: dict = json.load(file)["Servo"]

    DEGREES_PER_SECOND: ClassVar[float] = servo_properties["Degrees Per Second"]
    ANGLE_LIMIT: ClassVar[float] = servo_properties["Angle Limit (deg)"]

    current_angle: float = 0.0

    def tilt(self, degrees) -> None:
        pass
