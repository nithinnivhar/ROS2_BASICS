#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class BatteryNode(Node):
    def __init__(self):
        super().__init__("battery")
        self.battery_state_= "full"
        self.last_time_battery_state_changed_=self.get_current_time_seconds()
        self.battery_timer_=self.create_timer(0.1,self.check_battery_states())
    
    def get_current_time_seconds(self):
         secs, nsecs = self.get_clock.now().seconds_nanoseconds()
         return secs + nsecs / 1000000000.0


    def check_battery_states(self):
         timer_now=self.get_current_time_seconds()
         if self.battery_state_=="full":
              if timer_now - self.last_time_battery_state_changed_>4.0:
                   self.battery_state_="empty"
                   self.get_logger().info("Battery is empty! Charging battery...")
                   self.last_time_battery_state_changed_=timer_now
         else:
              if timer_now - self.last_time_battery_state_changed_>6.0:
                   self.battery_state_="full"
                   self.get_logger().info("Battery is now full again.")
                   self.last_time_battery_state_changed_=timer_now


def main(args=None):
    rclpy.init(args=args)
    node=BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__== "__main__":
        main()