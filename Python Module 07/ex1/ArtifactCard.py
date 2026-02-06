from ex0.Card import Card


class ArtifactCard(Card):
    """Concrete card for permanent game items."""

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        """Initialize artifact with durability and effect."""
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        """Activate the artifact ability and return play info."""
        result = self.activate_ability()
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': result['effect']
        }

    def activate_ability(self) -> dict:
        """Return the artifact's permanent effect info."""
        return {'effect': self.effect}
