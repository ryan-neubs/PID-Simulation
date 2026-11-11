from dataclasses import dataclass
from typing import ClassVar
from servo import Servo
import math
import json

class Ball:
    """
    Represents the physical state of the 5/8" steel ball
    bearing as it rolls along the linear soft potentiometer.
    """
    with open("setup.json", "r", encoding="utf-8") as file:
        rail_properies: int = json.load(file)["Rail"]
        rail_length_mm = rail_properies["Rail Length (mm)"]

    BALL_MASS_GRAMS: ClassVar[float] = 16.0
    BALL_SIZE_MM: ClassVar[float] = 15.875
    LATERAL_OFFSET_LIMIT_MM: ClassVar[float] = rail_length_mm / 2
    HEIGHT_OFFSET_LIMIT_MM: ClassVar[float] = LATERAL_OFFSET_LIMIT_MM * math.sin(
        math.radians(Servo.ANGLE_LIMIT)
    )

    _ball_lateral_offset_mm: float = 0.0
    _ball_height_mm: float = 0.0
    ball_velocity: float = 0.0

    def __init__(self, lateral_offset) -> None:
        self.ball_lateral_offset_mm = lateral_offset

    @property
    def ball_height_mm(self) -> float:
        """Height offset from level position in mm."""
        return self._ball_height_mm

    @ball_height_mm.setter
    def ball_height_mm(self, value: float) -> None:
        limit = self.HEIGHT_OFFSET_LIMIT_MM
        self._ball_height_mm = max(-limit, min(value, limit))

    @property
    def ball_lateral_offset_mm(self) -> float:
        """Position offset from centered position in mm."""
        return self._ball_lateral_offset_mm

    @ball_lateral_offset_mm.setter
    def ball_lateral_offset_mm(self, value: float) -> None:
        limit = self.LATERAL_OFFSET_LIMIT_MM
        self._ball_lateral_offset_mm = max(-limit, min(value, limit))