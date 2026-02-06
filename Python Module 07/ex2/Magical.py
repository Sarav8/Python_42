from abc import ABC, abstractmethod


class Magical(ABC):
    """Interface for cards that possess magical abilities."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Abstract method to cast a magical spell."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Abstract method to increase mana pool."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Abstract method to get magic-related data."""
        pass
