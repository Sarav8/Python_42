import random
from typing import Optional
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck:
    """Class to manage a collection of different card types."""

    def __init__(self):
        """Initialize an empty list of cards."""
        self.cards = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck list."""
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card by name and return True if found."""
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Randomly shuffle the deck in-place."""
        random.shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        """Remove and return the top card, or None if empty."""
        if not self.cards:
            return None
        draw = self.cards[0]
        self.cards = self.cards[1:]
        return draw

    def get_deck_stats(self) -> dict:
        """Return statistics and average cost of the deck."""
        artifact = 0
        spell = 0
        creature = 0
        cost = 0
        total = len(self.cards)

        for card in self.cards:
            cost += card.cost
            if isinstance(card, SpellCard):
                spell += 1
            elif isinstance(card, ArtifactCard):
                artifact += 1
            elif isinstance(card, CreatureCard):
                creature += 1

        avg_cost = cost / total if total > 0 else 0.0
        return {
            'total_cards': total,
            'spells': spell,
            'artifacts': artifact,
            'creatures': creature,
            'avg_cost': avg_cost
        }
