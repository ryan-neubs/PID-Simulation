This directory represents the components in the setup that react to, and influence the physics of the simulation.

#### control_loop.py
This file houses the PID control loop. These are the commands that will be calculated and sent out by the microcontroller to influence the physical system. Each step it:
1. Calculates the current error as the setpoint minus the ball's lateral offset.
2. Combines the proportional, integral, and derivative terms (using the gains from `setup.json`) into a single command.
3. Converts that command into a servo angle adjustment, limited by the servo's speed and angle limit, and passes it to the servo.

#### servo.py
This represents the servo that controls the tilt of our rail the ball is on. It holds the properties of our servo (currently setup for an SG90 microservo), such as its angle limit and speed, along with its current angle. It has a singular method called "tilt" that adjusts the servo tilt from the command output by the PID step.