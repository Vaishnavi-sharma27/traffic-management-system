class EmergencyController:

    def __init__(self):

        self.emergency_active = False

        self.emergency_lane = None

    def activate_emergency(
        self,
        lane
    ):

        self.emergency_active = True

        self.emergency_lane = lane

    def deactivate_emergency(self):

        self.emergency_active = False

        self.emergency_lane = None

    def get_priority_lane(self):

        if self.emergency_active:

            return self.emergency_lane

        return None