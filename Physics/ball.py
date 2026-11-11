from Control.servo import Servo
from dataclasses import dataclass
import json
import math
from typing import ClassVar

class Ball:
    """
    Represents the physical state of the 5/8" steel ball
    bearing as it rolls along the linear soft potentiometer.
    """
    with open("setup.json", "r", encoding="utf-8") as file:
        sim_properties: dict = json.load(file)
        rail_length_mm: float = sim_properties["Rail"]["Length (mm)"]
        ball_initial_offset: float = sim_properties["Ball"]["Initial Offset (mm)"]

    LATERAL_OFFSET_LIMIT_MM: ClassVar[float] = rail_length_mm / 2
    HEIGHT_OFFSET_LIMIT_MM: ClassVar[float] = LATERAL_OFFSET_LIMIT_MM * math.sin(
        math.radians(Servo.ANGLE_LIMIT)
    )

    _lateral_offset_mm: float = ball_initial_offset
    _height_mm: float = 0.0
    velocity: float = 0.0
    acceleration: float = 0.0

    @property
    def height_mm(self) -> float:
        """Height offset from level position in mm."""
        return self._height_mm

    @height_mm.setter
    def height_mm(self, value: float) -> None:
        limit = self.HEIGHT_OFFSET_LIMIT_MM
        self._height_mm = max(-limit, min(value, limit))

    @property
    def lateral_offset_mm(self) -> float:
        """Position offset from centered position in mm."""
        return self._lateral_offset_mm

    @lateral_offset_mm.setter
    def lateral_offset_mm(self, value: float) -> None:
        limit = self.LATERAL_OFFSET_LIMIT_MM
        self._lateral_offset_mm = max(-limit, min(value, limit))