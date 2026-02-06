from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory


class GameEngine:
    """Orchestrator that combines a CardFactory and a GameStrategy."""

    def __init__(self):
        """Initialize the engine with default values."""
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """Assign a factory and a strategy to the engine."""
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        """Execute a turn using the factory to draw and strategy to play."""
        deck = self.factory.create_themed_deck(8)
        hand = [
            f"{card.name} ({card.cost})"
            for card_list in deck.values()
            for card in card_list
        ]
        print(f"Hand: {hand}")
        battlefield = []
        turn_result = self.strategy.execute_turn(hand, battlefield)
        self.turns_simulated += 1
        self.total_damage = turn_result['damage_dealt']
        self.cards_created = len(turn_result['cards_played'])
        return turn_result

    def get_engine_status(self) -> dict:
        """Return cumulative statistics of the engine."""
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
