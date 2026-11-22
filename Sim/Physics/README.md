This directory represents the physical side of the simulation: the ball on the rail and the physics that move it as the servo tilts the rail. Distances are in millimeters and masses are in grams.

#### ball.py
This represents the 5/8" steel ball bearing. It holds the ball's physical properties (mass, diameter, rotational inertia), the rail and servo limits it must stay within, and its current state (lateral offset, height, velocity, and acceleration). Setting the ball's lateral offset or height clamps it to the rail's limits so it can't leave the rail.

#### physics.py
This file houses the physics loop, which updates the ball's state between each step of the PID controller. Each step it calculates the ball's acceleration from the servo's current tilt (including the effect of the ball rolling instead of sliding), then updates the ball's position, velocity, and height.
