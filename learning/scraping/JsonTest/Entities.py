class Odds:
    def __init__(self, race_name, rider_name, size):
        self.race_name = race_name
        self.rider_name = rider_name
        self.size = size

    def toString(self):
        print(self.race_name + " - " + self.rider_name + " - " + self.size)