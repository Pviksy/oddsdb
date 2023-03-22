class Race:
    def __init__(self, id, org_id, name, country, category, year):
        self.id = id
        self.org_id = org_id
        self.name = name
        self.country = country
        self.category = category
        self.year = year

    def print(self):
        print('      id:', self.id)
        print('  org_id:', self.org_id)
        print('    name:', self.name)
        print(' country:', self.country)
        print('category:', self.category)
        print('    year:', self.year)
        print('          -')