class Team:
    def __init__(self, id, name, category, country):
        self.id = id
        self.name = name
        self.category = category
        self.country = country

    def toString(self):
        print("id: ", self.id)
        print("name: ", self.name)
        print("category: ", self.category)
        print("country: ", self.country)