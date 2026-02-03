from ex0 import Card
from ex2 import Combatable
from ex4 import Rankable


class TournamentCard (Card, Combatable, Rankable):
    def __init__(self, name, cost, rarity, id):
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self)
        self.wins= 0 
        self.losses =0
        self.rating = 1000
        self.id = id


    def play(self, game_state: dict) -> dict:
        result = {
            'name': self.name,
            'id': self.id,
            'rating': self.rating, 
            'record': f"{self.wins} - {self.losses}"
        }
        return result

    def attack(self, target) -> dict:
        import random

        if random.choice([True, False]):
            winner = self
            loser = target
        else:
            winner = target
            loser = self

        winner.update_wins(1)
        loser.update_losses(1)

        return {
            'winner': winner.id,
            'loser': loser.id,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating
        }

        

    def calculate_rating(self) -> int:
        return self.rating

    def get_tournament_stats(self) -> dict:
        result = {
            'name': self.name,
            'rating': self.rating,
            'record': f"{self.wins} - {self.losses}"
        }
        return result

    
    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16 
    

  
    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16

   
    def get_rank_info(self) -> dict:
        result = {
    "wins": self.wins,
    "losses": self.losses,
    "rating": self.rating
        }
        return result