import sys
import os

project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(project_root)

from controllers.signal_controller import SignalController

controller = SignalController()

controller.update_lane("A",15)

controller.update_lane("B",50)

controller.update_lane("C",30)

controller.update_lane("D",80)

priority_lane = controller.get_priority_lane()

print(
    "Priority Lane:",
    priority_lane
)