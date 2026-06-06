class Vehicle:

    def __init__(self, vehicle_id, vehicle_type, lane):

        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.lane = lane

    def display(self):

        return f"{self.vehicle_id} | {self.vehicle_type} | Lane {self.lane}"