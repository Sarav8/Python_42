from abc import ABC, abstractmethod


class Combatable(ABC):
    """Interface for cards that can engage in combat."""

    @abstractmethod
    def attack(self, target) -> dict:
        """Abstract method to perform an attack."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Abstract method to handle incoming damage."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Abstract method to get combat-related data."""
        pass
