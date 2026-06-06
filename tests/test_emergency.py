import sys
import os

project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(project_root)

from controllers.emergency_controller import EmergencyController

controller = EmergencyController()

controller.activate_emergency("B")

print(
    "Priority Lane:",
    controller.get_priority_lane()
)

controller.deactivate_emergency()

print(
    "Emergency Status:",
    controller.emergency_active
)