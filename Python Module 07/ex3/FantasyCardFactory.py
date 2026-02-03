from ex3.CardFactory import CardFactory
from ex1 import SpellCard, ArtifactCard
from ex0 import Card, CreatureCard

class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power) -> Card:
        if name_or_power == "Goblin":
            return CreatureCard("Goblin Warrior", 2, "Common", 2, 2)
        elif name_or_power == "Dragon":
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 6)

    def create_spell(self, name_or_power) -> Card:
        if name_or_power == "Fireball":
            return SpellCard("Fireball", 4, "Rare", "damage")
        elif name_or_power == "Lightning Bolt":
            return SpellCard("Lightning Bolt", 3, "Common", "damage")

    def create_artifact(self, name_or_power) -> Card:
        if name_or_power == "Mana Ring":
            return ArtifactCard("Mana Ring", 2, "Rare", 5, "+1 mana per turn")
        elif name_or_power == "Magic Staff":
            return ArtifactCard("Magic Staff", 3, "Epic", 4, "+2 spell damage")

    def create_themed_deck(self, size: int) -> dict:
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
        result = {
            'creatures': ['Goblin', 'Dragon'],
            'spells': ['Fireball', 'Lightning Bolt'],
            'artifacts': ['Mana Ring', 'Magic Staff']
        }
        return result
