class Signal:

    def __init__(self, lane):

        self.lane = lane

        self.green_time = 30

    def update_green_time(self, time):

        self.green_time = time