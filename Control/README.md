This directory represents the components in the setup that react to, and influence the physics of the simulation.

#### control_loop.py
This file houses the PID control loop. These are the commands that will be calculated and sent out by the microcontroller to influence the physical system. It calculates our current error based on the ball's position and the servo tilt and outputs the updated servo tilt.

#### servo.py
This represents the servo that controls the tilt of our rail the ball is on. It holds the properties of our servo (currently setup for an SG90 microservo) and a singular method called "tilt" that adjusts the servo tilt from the command output by the PID step.