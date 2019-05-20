"""
The simulate_underwater_yawbot script starts a simulator with the Underwater Yawbot.
"""
import time

from demo.underwater_yawbot.underwater_yawbot import UnderwaterYawbot
from src.simulation.simulator import Simulator

SIMULATOR = Simulator()
SIMULATOR.spawn_robot(UnderwaterYawbot())

time.sleep(10)

SIMULATOR.stop()
