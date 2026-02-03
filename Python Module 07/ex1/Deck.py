from ex0.Card import Card
import random
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard


class Deck():
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards == []:
            return None
        draw = self.cards[0]
        self.cards = self.cards[1:]
        return draw
        

    def get_deck_stats(self) -> dict:
        artifact = 0
        spell = 0
        creature = 0
        cost = 0
        total = len(self.cards)
        for card in self.cards:
            if isinstance(card, SpellCard):
                spell += 1
                cost += card.cost
            elif isinstance(card, ArtifactCard):
                artifact += 1
                cost += card.cost
            elif isinstance(card, CreatureCard):
                creature += 1
                cost += card.cost
        avg_cost = cost / total if total > 0 else 0
        result = {
                'total_cards': total,
                'spells': spell,
                'artifacts': artifact,
                'creatures': creature,
                'avg_cost': avg_cost
                }
        return result

                
