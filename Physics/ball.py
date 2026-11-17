from Control.servo import Servo
from dataclasses import dataclass
import json
import math
from typing import ClassVar, Any

class Ball:
    """
    Represents the physical state of the 5/8" steel ball bearing.
    """
    with open("setup.json", "r", encoding="utf-8") as file:
        sim_properties: dict[str, Any] = json.load(file)
        rail_length_mm: float = sim_properties["Rail"]["Length (mm)"]
        ball_properties: float = sim_properties["Ball"]

    LATERAL_OFFSET_LIMIT_MM: ClassVar[float] = rail_length_mm / 2
    HEIGHT_OFFSET_LIMIT_MM: ClassVar[float] = LATERAL_OFFSET_LIMIT_MM * math.sin(
        math.radians(Servo.ANGLE_LIMIT)
    )
    MASS_GRAMS: ClassVar[float] = ball_properties["Mass (g)"]
    DIAMETER_MM: ClassVar[float] = ball_properties["Diameter (mm)"]
    RADIUS_MM: ClassVar[float] = DIAMETER_MM / 2
    ROTATIONAL_INERTIA: ClassVar[float] = 0.4 * (MASS_GRAMS / 1000) * (RADIUS_MM ** 2)

    """Current lateral offset from centered position in mm."""
    _lateral_offset_mm: float = ball_properties["Initial Offset (mm)"]
    """Current height offset from level position in mm."""
    _height_mm: float = 0.0
    """Current velocity of the ball"""
    velocity: float = 0.0
    """Current acceleration of the ball"""
    acceleration: float = 0.0

    @property
    def height_mm(self) -> float:
        return self._height_mm

    @height_mm.setter
    def height_mm(self, value: float) -> None:
        limit: float = self.HEIGHT_OFFSET_LIMIT_MM
        self._height_mm = max(-limit, min(value, limit))

    @property
    def lateral_offset_mm(self) -> float:
        return self._lateral_offset_mm

    @lateral_offset_mm.setter
    def lateral_offset_mm(self, value: float) -> None:
        limit = self.LATERAL_OFFSET_LIMIT_MM
        self._lateral_offset_mm = max(-limit, min(value, limit))