class TrafficController:

    def __init__(self):

        self.max_capacity = 100

    def calculate_density(
        self,
        vehicle_count
    ):

        density = (
            vehicle_count /
            self.max_capacity
        ) * 100

        return density

    def calculate_green_time(
        self,
        density
    ):

        if density >= 80:
            return 90

        elif density >= 60:
            return 60

        elif density >= 40:
            return 40

        elif density >= 20:
            return 30

        else:
            return 20