#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math
import serial
import time

class SerialBridgeNode(Node):
    def __init__(self):
        super().__init__('serial_bridge_node')
        self.port = self.declare_parameter('port', '/dev/ttyUSB0').value
        self.baudrate = self.declare_parameter('baudrate', 9600).value
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
            time.sleep(2)
            self.get_logger().info(f"Connected to Arduino on {self.port}")
        except Exception as e:
            self.get_logger().error(f"Failed to connect to Serial Port: {e}")
            self.ser = None

        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_state_callback,
            10
        )

    def rad_to_deg(self, rad):
        deg = math.degrees(rad) + 90
        return max(0, min(180, int(deg)))

    def joint_state_callback(self, msg):
        if self.ser and self.ser.is_open:
            if len(msg.position) >= 5:
                j1 = self.rad_to_deg(msg.position[0])
                j2 = self.rad_to_deg(msg.position[1])
                j3 = self.rad_to_deg(msg.position[2])
                j4 = self.rad_to_deg(msg.position[3])
                j5 = self.rad_to_deg(msg.position[4])

                data_str = f"{j1},{j2},{j3},{j4},{j5}\n"
                self.ser.write(data_str.encode('utf-8'))
                self.get_logger().info(f"Sent to Arduino: {data_str.strip()}")

def main(args=None):
    rclpy.init(args=args)
    node = SerialBridgeNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if node.ser:
            node.ser.close()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
