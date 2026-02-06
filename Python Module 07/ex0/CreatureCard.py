from ex0.Card import Card


class CreatureCard(Card):
    """Concrete implementation of a card representing a creature."""

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        """Initialize creature with attack and health validation."""
        super().__init__(name, cost, rarity)

        if health <= 0 or attack <= 0:
            raise ValueError("Attack and Health must be positive integers")

        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        """Implement play method for a creature card."""
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def get_card_info(self) -> dict:
        """Return dictionary with creature-specific information."""
        info = super().get_card_info()
        info.update({
            'type': 'Creature',
            'attack': self.attack,
            'health': self.health
        })
        return info

    def attack_target(self, target: 'CreatureCard') -> dict:
        """Resolve combat between this creature and a target."""
        return {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }
