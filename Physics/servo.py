from typing import ClassVar

class Servo:
    DEGREES_PER_SECOND: ClassVar[float] = 600.0
    ANGLE_LIMIT: ClassVar[float] = 15.0

    current_angle: float = 0.0

    def tilt(self, degrees) -> None:
        pass
