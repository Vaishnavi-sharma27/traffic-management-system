from controllers.signal_controller import SignalController
from controllers.emergency_controller import EmergencyController


class SmartController:

    def __init__(self):

        self.signal_controller = SignalController()

        self.emergency_controller = EmergencyController()

    def update_lane(
        self,
        lane,
        vehicles
    ):

        self.signal_controller.update_lane(
            lane,
            vehicles
        )

    def activate_ambulance(
        self,
        lane
    ):

        self.emergency_controller.activate_emergency(
            lane
        )

    def get_active_lane(self):

         emergency_lane = self.emergency_controller.get_priority_lane()

         if emergency_lane:
            return emergency_lane

         lane = self.signal_controller.get_priority_lane()

         print("DEBUG LANE:", lane)

         return lane
    

    # def get_active_lane(self):

    #     emergency_lane = self.emergency_controller.get_priority_lane()

    #     if emergency_lane:
    #         return emergency_lane

    #     normal_lane = self.signal_controller.get_priority_lane()

    #     if normal_lane is None:
    #        return "None"

    #     return normal_lane