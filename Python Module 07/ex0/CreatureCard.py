from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        if health <= 0:
            raise ValueError ("Health must be positive integer")
        self.health = health
        if attack <= 0:
            raise ValueError ("Attack must be a positive integer")
        self.attack = attack
        

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def get_card_info(self):
        info_card = super().get_card_info()
        info_card['type'] = 'Creature'
        info_card['attack'] = self.attack
        info_card['health'] = self.health
        return info_card

    def attack_target(self, target) -> dict:
        info_attack = {
            'attacker': self.name,
            'target': target.name, 
            'damage_dealt': self.attack,
            'combat_resolved': True
        }
        return info_attack

