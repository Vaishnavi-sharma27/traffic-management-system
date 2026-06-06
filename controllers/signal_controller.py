class SignalController:

    def __init__(self):

        self.lanes = {}

    def update_lane(
        self,
        lane_name,
        vehicle_count
    ):

        self.lanes[lane_name] = vehicle_count

    def get_priority_lane(self):

        highest_lane = max(
            self.lanes,
            key=self.lanes.get
        )

        return highest_lane
    
    def get_all_lanes(self):
        return self.lanes