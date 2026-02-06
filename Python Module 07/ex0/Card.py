from abc import ABC, abstractmethod


class Card(ABC):
    """Abstract class representing a generic game card."""

    def __init__(self, name: str, cost: int, rarity: str):
        """Initialize card with name, cost, and rarity."""
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Abstract method to define card behavior when played."""
        pass

    def get_card_info(self) -> dict:
        """Return a dictionary with basic card information."""
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """Check if the card can be played with current mana."""
        return available_mana >= self.cost
