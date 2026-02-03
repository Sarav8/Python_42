from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory
from ex3.FantasyCardFactory import FantasyCardFactory
class GameEngine():
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        deck = self.factory.create_themed_deck(8)
        hand = [f"{card.name} ({card.cost})" for card_list in deck.values() for card in card_list]
        print(f"Hand: {hand}")
        battlefield = []
        turn_result = self.strategy.execute_turn(hand, battlefield)
        self.turns_simulated += 1
        self.total_damage = turn_result['damage_dealt'] 
        self.cards_created = len(turn_result['cards_played'])
        return turn_result

        
    def get_engine_status(self) -> dict:
         return {
        'turns_simulated': self.turns_simulated,
        'strategy_used': self.strategy.get_strategy_name(),
        'total_damage': self.total_damage,
        'cards_created': self.cards_created
    }