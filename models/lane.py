class Lane:

    def __init__(self, lane_name):

        self.lane_name = lane_name

        self.vehicle_count = 0

    def add_vehicle(self):

        self.vehicle_count += 1

    def remove_vehicle(self):

        if self.vehicle_count > 0:

            self.vehicle_count -= 1

    def get_count(self):

        return self.vehicle_count