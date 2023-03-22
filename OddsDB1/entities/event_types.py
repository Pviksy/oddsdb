class Generic:
    def __init__(self, id, event_type):
        self.id = id
        self.event_type = event_type


class GC(Generic):
    def __init__(self, id, event_type, num_stages):
        super().__init__(id, event_type)
        self.num_stages = num_stages


class RaceDay(Generic):
    def __init__(self, id, event_type, distance, elevation):
        super().__init__(id, event_type)
        self.distance = distance
        self.elevation = elevation
