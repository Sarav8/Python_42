import random
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """Card that implements Combat and Ranking interfaces."""

    def __init__(self, name: str, cost: int, rarity: str, id: str):
        """Initialize card with tournament and combat stats."""
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self)
        self.id = id
        self.wins = 0
        self.losses = 0
        self.rating = 1000
        self.health = 10
        self.damage = 5

    def play(self, game_state: dict) -> dict:
        """Return basic card play information."""
        return {'name': self.name, 'id': self.id, 'rating': self.rating}

    def attack(self, target: 'TournamentCard') -> dict:
        """Simulate a match and update wins/losses."""
        if random.choice([True, False]):
            winner, loser = self, target
        else:
            winner, loser = target, self

        winner.update_wins(1)
        loser.update_losses(1)

        return {
            'winner': winner.id,
            'loser': loser.id,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating
        }

    def defend(self, incoming_damage: int) -> dict:
        """Handle damage taken during combat."""
        self.health -= incoming_damage
        return {'defender': self.name, 'health_left': self.health}

    def get_combat_stats(self) -> dict:
        """Return health and damage stats."""
        return {'health': self.health, 'damage': self.damage}

    def calculate_rating(self) -> int:
        """Return current ELO rating."""
        return self.rating

    def update_wins(self, wins: int) -> None:
        """Add wins and increase rating."""
        self.wins += wins
        self.rating += 16

    def update_losses(self, losses: int) -> None:
        """Add losses and decrease rating."""
        self.losses += losses
        self.rating -= 16

    def get_rank_info(self) -> dict:
        """Return tournament record and rating."""
        return {
            'wins': self.wins,
            'losses': self.losses,
            'rating': self.rating
        }

    def get_tournament_stats(self) -> dict:
        """Helper for tournament reporting."""
        return self.get_rank_info()
