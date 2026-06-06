import sys
import os

project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(project_root)

from controllers.traffic_controller import TrafficController

controller = TrafficController()

vehicles = 55

density = controller.calculate_density(
    vehicles
)

green_time = controller.calculate_green_time(
    density
)

print("Vehicles:", vehicles)

print("Density:", density)

print("Green Time:", green_time)