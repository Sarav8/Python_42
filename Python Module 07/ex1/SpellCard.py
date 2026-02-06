from ex0.Card import Card


class SpellCard(Card):
    """Concrete card for instant magic effects."""

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        """Initialize spell with an effect type."""
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        """Resolve the spell effect and return play info."""
        result = self.resolve_effect(targets=[])
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': result['effect']
        }

    def resolve_effect(self, targets: list) -> dict:
        """Define specific behavior based on effect_type."""
        effect = self.effect_type
        if effect == "damage":
            return {'effect': 'Deal 3 damage to target'}
        elif effect == "heal":
            return {'effect': 'Heals the target'}
        elif effect == "buff":
            return {'effect': 'Applies a buff'}
        elif effect == "debuff":
            return {'effect': 'Weakens the enemy'}
        return {'effect': 'No effect'}
