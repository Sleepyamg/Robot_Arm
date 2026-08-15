# 5-DOF Robot Arm - ROS 2 & Gazebo Simulation with Arduino Bridge

This repository contains the ROS 2 packages for simulating a 5-DOF robotic arm in Gazebo Sim, controlled via `ros2_control`, along with a Serial Bridge node to map joint state trajectories directly to physical servo motors via Arduino.

---

## **Features**
* **URDF & Xacro Modeling**: Complete 5-DOF robotic arm model with visual, collision, and custom inertial elements.
* **Gazebo Integration**: Simulation support powered by Gazebo Sim (`ros2_control` hardware interface plugin).
* **Trajectory Control**: Configured `joint_state_broadcaster` and `JointTrajectoryController` (`arm_controller`).
* **Serial Bridge (`serial_bridge.py`)**: ROS 2 node subscribing to `/joint_states`, converting radians to degrees ($0^\circ - 180^\circ$), and publishing CSV data over Serial to Arduino.

---

## **Package Structure**
```text
my_robot_arm/
├── config/
│   └── controllers.yaml
├── launch/
│   └── robot.launch.py
├── my_robot_arm/
│   ├── __init__.py
│   ├── serial_bridge.py
│   └── trajectory_controller.py
├── urdf/
│   ├── my_robot_arm.ros2_control.xacro
│   └── my_robot_arm.urdf.xacro
├── package.xml
├── setup.py
└── README.md
