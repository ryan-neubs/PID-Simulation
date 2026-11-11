from Control.servo import Servo
from Control.control_loop import ControlLoop
import json
from Physics.ball import Ball
from Physics.physics import PhysicsLoop
import time

with open("setup.json", "r", encoding="utf-8") as file:
    setup_properties: dict = json.load(file)
    sim_duration: int = setup_properties["Time"]["Simulator Runtime (s)"]

ball = Ball()
servo = Servo()
control_loop = ControlLoop(ball, servo)
physics_loop = PhysicsLoop(ball, servo)

seconds = 0

while seconds < sim_duration:
    physics_loop.step()
    control_loop.step()
    print(f'Ball [offset|height] [{ball.lateral_offset_mm:.2f}|{ball.height_mm:.2f}]')
    seconds += 0.02
    time.sleep(0.02)