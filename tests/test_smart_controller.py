import sys
import os

project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(project_root)

from controllers.smart_controller import SmartController

controller = SmartController()

controller.update_lane("A",10)

controller.update_lane("B",30)

controller.update_lane("C",20)

controller.update_lane("D",60)

print(
    "Normal Mode:",
    controller.get_active_lane()
)

controller.activate_ambulance("B")

print(
    "Emergency Mode:",
    controller.get_active_lane()
)