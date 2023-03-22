class Rider:
    def __init__(self, id, team_id, firstname, lastname, country, date_of_birth):
        self.id = id
        self.team_id = team_id
        self.firstname = firstname
        self.lastname = lastname
        self.country = country
        self.date_of_birth = date_of_birth

    def print(self):
        print('           id:', self.id)
        print('      team_id:', self.team_id)
        print('         name:', self.firstname, self.lastname)
        print('      country:', self.country)
        print('date_of_birth:', self.date_of_birth)
        print('               -')