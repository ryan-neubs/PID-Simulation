import json
import time
from GUI.Graphing.graphing import RealTimeGraph
from Sim.Control.servo import Servo
from Sim.Control.control_loop import ControlLoop
from Sim.Physics.ball import Ball
from Sim.Physics.physics import PhysicsLoop

with open("setup.json", "r", encoding="utf-8") as file:
    SETUP_PROPERTIES: dict = json.load(file)
    
SIM_DURATION: float = SETUP_PROPERTIES["Time"]["Simulator Runtime (s)"]
SIMULATOR_STEP: float = 0.02

ball: Ball = Ball()
servo: Servo = Servo()
control_loop: ControlLoop = ControlLoop(ball, servo)
physics_loop: PhysicsLoop = PhysicsLoop(ball, servo)
graph: RealTimeGraph = RealTimeGraph(SIM_DURATION, SIMULATOR_STEP)

seconds: float = 0.0

while seconds < SIM_DURATION:
    graph.add_point(ball.lateral_offset_mm)
    physics_loop.step()
    control_loop.step()
    print(f'[ball offset|ball height|servo angle] [{ball.lateral_offset_mm:.2f}|{ball.height_mm:.2f}|{servo.current_angle:.2f}]')
    seconds += 0.02
    time.sleep(SIMULATOR_STEP)