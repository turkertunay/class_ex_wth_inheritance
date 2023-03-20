class Footballer:
    def __init__(self, name, nation, age, team, position, is_active):
        self.name = name
        self.nation = nation
        self.age = age
        self.team = team
        self.position = position
        self.is_active = is_active

    def young(self):
        if self.age <= 21:
            return True
        else:
            return False

