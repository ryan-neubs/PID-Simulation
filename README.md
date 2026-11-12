# PID-Simulation
This repo is for learning the PID control loop for robotics. This simulates the PID control loop for a ball balancing on a rail with a servo controlling the tilt. The end goal is to use this simulation to segue into a physical setup with an ESP32, linear soft potentiometer, servo, and steel ball bearing.

# To run
The entire simulation runs out of sim.py. You can tweak the simualtion length in setup.json.

From the CLI: 'python3 sim.py' or 'python sim.py'


# Plans
- Add a graph of the error, outout command, servo tilt, ball speed, ball positon, etc over time for a better UX of what is happening.
- Add a gui for tweaking the Kp, Ki, and Kd gains in real time. 
- Add gui for tweaking the physical components/variables of the system.
- Unit testing
- 3D Simulation?