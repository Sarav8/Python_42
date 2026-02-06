from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Magical, Combatable):
    """A powerful card that combines combat and magic abilities."""

    def __init__(self, name: str, cost: int, rarity: str,
                 health: int, attack: int, mana: int):
        """Initialize EliteCard with all required attributes."""
        Card.__init__(self, name, cost, rarity)
        self.health = health
        self.damage = attack
        self.mana = mana
        self.combat_type = 'melee'
        self.damage_blocked = 3

    def attack(self, target) -> dict:
        """Implement attack from Combatable interface."""
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.damage,
            'combat_type': self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        """Implement defense from Combatable interface."""
        damage_taken = max(0, incoming_damage - self.damage_blocked)
        self.health -= damage_taken
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': self.damage_blocked,
            'still_alive': self.health > 0
        }

    def get_combat_stats(self) -> dict:
        """Return combat statistics."""
        return {'health': self.health, 'damage': self.damage}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Implement spell casting from Magical interface."""
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': self.mana
        }

    def channel_mana(self, amount: int) -> dict:
        """Implement mana channeling."""
        self.mana += amount
        return {'channeled': amount, 'total_mana': self.mana}

    def get_magic_stats(self) -> dict:
        """Return magic statistics."""
        return {'total_mana': self.mana}

    def play(self, game_state: dict) -> dict:
        """Execute a full turn action for the elite card."""
        return {
            'combat': self.attack("Enemy"),
            'magic': self.cast_spell("Fireball", ["Enemy1"])
        }

    def get_capabilities(self) -> str:
        """Return a string listing all card capabilities."""
        return (
            "EliteCard capabilities:\n"
            "- Card: ['play', 'get_card_info', 'is_playable']\n"
            "- Combatable: ['attack', 'defend', 'get_combat_stats']\n"
            "- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']"
        )
