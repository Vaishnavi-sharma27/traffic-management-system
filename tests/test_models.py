import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from models.vehicle import Vehicle
from models.lane import Lane
from models.signal import Signal

print("Smart Traffic Management System")
from models.vehicle import Vehicle
from models.lane import Lane
from models.signal import Signal

vehicle1 = Vehicle(
    "HR02AB1234",
    "Car",
    "A"
)

laneA = Lane("A")

laneA.add_vehicle()

signalA = Signal("A")

print(vehicle1.display())

print("Vehicle Count:", laneA.get_count())

print("Green Time:", signalA.green_time)
