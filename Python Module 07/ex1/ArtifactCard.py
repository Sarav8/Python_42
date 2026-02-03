from ex0.Card import Card

class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect


    def play(self, game_state: dict) -> dict:
        result = self.activate_ability()
        info_artifact = {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': result['effect']
        }
        return info_artifact

    def activate_ability(self) -> dict:
        return {f'effect': self.effect}

