from abc import ABC, abstractmethod


class Rankable(ABC):
    """Interface for objects that can be ranked in a tournament."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate and return the current rating."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update the win count and adjust rating."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update the loss count and adjust rating."""
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Return a dictionary with ranking statistics."""
        pass
