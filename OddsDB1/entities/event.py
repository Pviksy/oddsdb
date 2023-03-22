class Event:
    def __init__(self, id, race_id, type, name, date):
        """
        Event constructor

        :param id: PK in event table.
        :param race_id: Relates the individual event or betting market to the race it is part of.
        :param type: Makes it possible to add additional information to specific types of events, when it is not necessary to store it for all types.
        :param name:
        :param date:
        """
        self.id = id
        self.race_id = race_id
        self.type = type
        self.name = name
        self.date = date
