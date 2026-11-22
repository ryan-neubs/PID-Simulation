The files within the Sim directory represent all of the components needed to simulate the PID control loop of a ball balancing on a rail.

The simulation is split into two halves that run in lockstep, one step every 0.02 seconds (see `sim.py` in the project root):

- **[Physics](Physics/README.md)** - the physical world: the ball and how it moves as the rail tilts.
- **[Control](Control/README.md)** - the parts that sense and react: the PID controller and the servo that tilts the rail.

#### How the halves interact
1. The physics step reads the servo's current tilt and updates the ball's acceleration, position, velocity, and height.
2. The control step reads the ball's new position, calculates a PID command, and tells the servo to tilt toward it.
3. Repeat until the simulator runtime set in `setup.json` is reached.

Both halves share the same `Ball` and `Servo` objects, and all tunable values (gains, rail length, ball and servo properties) are read from `setup.json`.