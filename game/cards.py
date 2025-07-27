class Card:
    def __init__(self, name, cost, card_type, tags=None):
        self.name = name
        self.cost = cost
        self.card_type = card_type  # 'automated', 'active', or 'event'
        self.tags = tags if tags is not None else []
        self.requirements = {}
        self.effect_description = ""

    def play(self, player, game_state):
        raise NotImplementedError

class AsteroidCard(Card):
    def __init__(self):
        super().__init__("Asteroid", 14, "event", tags=['space', 'event'])
        self.effect_description = "Increase temperature 1 step."

    def play(self, player, game_state):
        game_state.board.temperature += 2
        player.terraform_rating += 1

class PowerPlantCard(Card):
    def __init__(self):
        super().__init__("Power Plant", 11, "automated", tags=['building'])
        self.effect_description = "Increase your energy production 1 step."

    def play(self, player, game_state):
        player.production['energy'] += 1

class CityCard(Card):
    def __init__(self):
        super().__init__("City", 25, "automated", tags=['city', 'building'])
        self.effect_description = "Place a city tile and increase your M€ production 1 step."

    def play(self, player, game_state):
        # TODO: Implement city placement logic
        player.production['megacredits'] += 1 