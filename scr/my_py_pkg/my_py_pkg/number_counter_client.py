#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial

from example_interfaces.srv import AddTwoInts
from example_interfaces.srv import SetBool


class AddTwoIntsClientNode(Node):
    def __init__(self):
        super().__init__("number_counter_client")
        self.call_add_two_ints_server(True)
       # self.call_add_two_ints_server(5 , 9)
        #self.call_add_two_ints_server(9 , 8)
        
    def call_add_two_ints_server(self, data):
        client =self.create_client(SetBool,"reset_number_count")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Add Two Ints...")

        request=SetBool.Request()
        request.data = data

        future=client.call_async(request)
        future.add_done_callback(partial(self.callback_call_add_two_ints, data=data))

    def callback_call_add_two_ints(self, future, request,response):
        response =future.result()
        if request.data:
          self.counter_=0 
          response.success=True
          response.message="Counter has been reset"
        else:
          response.success=False
          response.message="Counter has not beem reset"
        



def main(args=None):
    rclpy.init(args=args)
    node=AddTwoIntsClientNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__== "__main__":
        main()