#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from threading import Thread
import itertools as it

# =================
print(">> Task 1")


class Colors:
    """ Colors Enum """
    RED = 1
    YELLOW = 2
    GREEN = 3

    to_str = {RED: "Red", YELLOW: "Yellow", GREEN: "Green"}


class TrafficLight(Thread):
    init_color_order_list = [Colors.RED, Colors.YELLOW, Colors.GREEN]

    lighting_pause = {Colors.RED: 7,
                      Colors.YELLOW: 2,
                      Colors.GREEN: 4
                      }

    def __init__(self, color=Colors.RED):
        Thread.__init__(self)
        self.__color = color
        self.__color_order = list(
            it.islice(it.dropwhile(lambda x: x != color, it.cycle(TrafficLight.init_color_order_list)), Colors.GREEN))
        print(f"Order of traffic light is {self.__color_order}")

    def run(self):
        print("Now the traffic light is running...")
        count = 0
        for light in it.cycle(self.__color_order):
            if count > 3:
                break
            print(f"Light now is:{Colors.to_str[light]}")
            time.sleep(TrafficLight.lighting_pause[light])
            count += 1

    def running(self):
        self.start()


trafficLight = TrafficLight(Colors.YELLOW)
trafficLight.running()

# Waiting for completion
trafficLight.join(10)

print("It's all done")