from ex3.CardFactory import CardFactory
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class FantasyCardFactory(CardFactory):
    """Factory that creates fantasy-themed cards like Goblins and Dragons."""

    def create_creature(self, name_or_power: str) -> Card:
        """Create a creature card based on the given name."""
        if name_or_power == "Goblin":
            return CreatureCard("Goblin Warrior", 2, "Common", 2, 2)
        elif name_or_power == "Dragon":
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 6)
        return None

    def create_spell(self, name_or_power: str) -> Card:
        """Create a spell card based on the given name."""
        if name_or_power == "Fireball":
            return SpellCard("Fireball", 4, "Rare", "damage")
        elif name_or_power == "Lightning Bolt":
            return SpellCard("Lightning Bolt", 3, "Common", "damage")
        return None

    def create_artifact(self, name_or_power: str) -> Card:
        """Create an artifact card based on the given name."""
        if name_or_power == "Mana Ring":
            return ArtifactCard("Mana Ring", 2, "Rare", 5, "+1 mana per turn")
        elif name_or_power == "Magic Staff":
            return ArtifactCard("Magic Staff", 3, "Epic", 4, "+2 spell damage")
        return None

    def create_themed_deck(self, size: int) -> dict:
        """Create a dictionary of cards to form a themed deck."""
        total = size // 3
        list_art = []
        list_spell = []
        list_crea = []

        types = self.get_supported_types()
        creatures = types['creatures']
        spells = types['spells']
        artifacts = types['artifacts']

        for i in range(total):
            name = creatures[i % 2]
            list_crea.append(self.create_creature(name))

        for i in range(total):
            name = spells[i % 2]
            list_spell.append(self.create_spell(name))

        for i in range(total):
            name = artifacts[i % 2]
            list_art.append(self.create_artifact(name))

        return {
            'creatures': list_crea,
            'spells': list_spell,
            'artifacts': list_art
        }

    def get_supported_types(self) -> dict:
        """Return a dictionary of all card types supported by this factory."""
        return {
            'creatures': ['Goblin', 'Dragon'],
            'spells': ['Fireball', 'Lightning Bolt'],
            'artifacts': ['Mana Ring', 'Magic Staff']
        }
