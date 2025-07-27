class Player:
    def __init__(self, name):
        self.name = name
        self.corporation = None
        self.resources = {
            'megacredits': 0,
            'steel': 0,
            'titanium': 0,
            'plants': 0,
            'energy': 0,
            'heat': 0,
        }
        self.production = {
            'megacredits': 1,
            'steel': 1,
            'titanium': 1,
            'plants': 1,
            'energy': 1,
            'heat': 1,
        }
        self.cards = []
        self.terraform_rating = 20

    def __repr__(self):
        return self.name 