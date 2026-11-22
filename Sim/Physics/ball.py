import json
import math
from typing import Final, Any

with open("setup.json", "r", encoding="utf-8") as file:
    SIM_PROPERTIES: dict[str, Any] = json.load(file)
    RAIL_PROPERTIES: dict[str, Any] = SIM_PROPERTIES["Rail"]
    BALL_PROPERTIES: dict[str, Any] = SIM_PROPERTIES["Ball"]
    SERVO_PROPERTIES: dict[str, Any] = SIM_PROPERTIES["Servo"]

class Ball:
    """
    Represents the physical state and position of the 5/8" steel ball bearing.
    """

    # Rail constants
    RAIL_LENGTH_MM: Final[float] = RAIL_PROPERTIES["Length (mm)"]

    # Servo constants
    SERVO_ANGLE_LIMIT: Final[float] = SERVO_PROPERTIES["Angle Limit (deg)"]

    # Ball position limits
    LATERAL_OFFSET_LIMIT_MM: Final[float] = RAIL_LENGTH_MM / 2
    HEIGHT_OFFSET_LIMIT_MM: Final[float] = LATERAL_OFFSET_LIMIT_MM * math.sin(
        math.radians(SERVO_ANGLE_LIMIT)
    )

    # Ball initial position
    BALL_INITIAL_POSITION: Final[float] = BALL_PROPERTIES["Initial Offset (mm)"]

    # Ball physical properties
    MASS_GRAMS: Final[float] = BALL_PROPERTIES["Mass (g)"]
    DIAMETER_MM: Final[float] = BALL_PROPERTIES["Diameter (mm)"]
    RADIUS_MM: Final[float] = DIAMETER_MM / 2
    ROTATIONAL_INERTIA: Final[float] = 0.4 * (MASS_GRAMS / 1000) * (RADIUS_MM ** 2)

    """Current lateral offset from centered position in mm."""
    _lateral_offset_mm: float = BALL_INITIAL_POSITION

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