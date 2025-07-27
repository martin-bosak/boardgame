class Corporation:
    def __init__(self, name, starting_megacredits, effect_description=""):
        self.name = name
        self.starting_megacredits = starting_megacredits
        self.starting_resources = {}
        self.starting_production = {}
        self.tags = []
        self.effect_description = effect_description

    def apply_effect(self, player, game_state):
        pass

class BeginnerCorporation(Corporation):
    def __init__(self):
        super().__init__("Beginner Corporation", 42, "Starts with 10 project cards.")

    def apply_effect(self, player, game_state):
        # The 10 project cards are handled during setup
        pass

class Credicor(Corporation):
    def __init__(self):
        super().__init__("Credicor", 57, "When you play a card with a cost of 20 M€ or more (including the card's cost), you get a 4 M€ discount.")
        self.tags = ['earth']

    def apply_effect(self, player, game_state):
        # This effect is passive and will be checked when playing a card.
        pass

class TharsisRepublic(Corporation):
    def __init__(self):
        super().__init__("Tharsis Republic", 40, "As your first action, place a city tile. When anyone places a city, increase your M€ production 1 step. When you place a city, gain 3 M€.")
        self.tags = ['building']

    def apply_effect(self, player, game_state):
        # TODO: Implement the first action to place a city
        # The other effects are passive and will be handled by event listeners in the game logic
        pass 