class Odds:
    def __init__(self, id, bookmaker_id, event_id, team_id, rider_id, size, type, timestamp):
        self.id = id
        self.bookmaker_id = bookmaker_id
        self.event_id = event_id
        self.team_id = team_id
        self.rider_id = rider_id
        self.size = size
        self.type = type
        self.timestamp = timestamp
