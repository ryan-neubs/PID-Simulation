import json

with open("Gains.json", "r", encoding="utf-8") as file:
    gains = json.load(file)

PROPORTIONAL_GAIN: float = gains["Kp"]
INTEGRAL_GAIN: float = gains["Ki"]
DERIVATIVE_GAIN: float = gains["Kd"]
CONTROLLER_STEP: int = 100 # Milliseconds per controller step

file.close()

class ControlLoop:

    previous_error: float = 0
    integral: float = 0