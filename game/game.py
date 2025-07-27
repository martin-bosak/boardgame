import random
from .player import Player
from .corp import BeginnerCorporation, Credicor, TharsisRepublic
from .cards import AsteroidCard, PowerPlantCard, CityCard
from .board import Board

class Game:
    def __init__(self):
        self.players = []
        self.board = Board()
        self.current_player_index = 0
        self.project_cards = self._initialize_deck()
        self.corporations = self._initialize_corporations()

    def _initialize_deck(self):
        # For now, just a few cards for testing
        deck = [AsteroidCard() for _ in range(20)] + \
               [PowerPlantCard() for _ in range(20)] + \
               [CityCard() for _ in range(20)]
        random.shuffle(deck)
        return deck

    def _initialize_corporations(self):
        return [BeginnerCorporation(), Credicor(), TharsisRepublic()]

    def add_player(self, name):
        if len(self.players) < 5:
            player = Player(name)
            self.players.append(player)
            return player
        return None

    def start_game(self):
        if not self.players:
            raise ValueError("No players in the game.")

        # Assign corporations
        available_corps = self.corporations[:]
        random.shuffle(available_corps)
        for player in self.players:
            player.corporation = available_corps.pop()
            player.resources['megacredits'] = player.corporation.starting_megacredits

        # Deal initial cards
        for player in self.players:
            if player.corporation.name == "Beginner Corporation":
                player.cards = [self.project_cards.pop() for _ in range(10)]
            else:
                # In the full game, players would choose from a hand of 10
                player.cards = [self.project_cards.pop() for _ in range(10)]

    @property
    def current_player(self):
        return self.players[self.current_player_index] 