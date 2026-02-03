from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Magical, Combatable):
    def __init__(self, name, cost, rarity, health, attack, mana):
        super().__init__(name, cost, rarity)
        Combatable.__init__(self)
        Magical.__init__(self)
        self.damage = attack
        self.combat_type = 'melee'
        self.health = health
        self.damage_blocked = 3
        self.mana = mana
        

    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.damage,
            'combat_type': self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = incoming_damage - self.damage_blocked
        if damage_taken < 0:
            damage_taken = 0
        self.health -= damage_taken
        still_alive = self.health > 0
        return {
                'defender': self.name,
                'damage_taken': 2,
                'damage_blocked': self.damage_blocked,
                'still_alive': still_alive
            }

    def get_combat_stats(self) -> dict:
        return {
            'health': self.health,
            'damage': self.damage,
            'combat_type': self.combat_type
        }
    
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': self.mana
            }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount        
        return {                   
            'channeled': amount,
            'total_mana': self.mana
        }

    def get_magic_stats(self) -> dict:    
        return {                   
            'total_mana': self.mana
        }

    def play(self) -> dict:
        def play(self) -> dict:
            combat_result = self.attack("Enemy")
            defense_result = self.defend(5) 
            magic_result = self.cast_spell("Fireball", ["Enemy1", "Enemy2"])
            mana_result = self.channel_mana(3)
            return {
                'combat': combat_result,
                'defense': defense_result,
                'magic': magic_result,
                'mana': mana_result
            }

    def get_capabilities(self) -> dict:
        capabilities = {
            'Card': ['play', 'get_card_info', 'is_playable'],
            'Combatable': ['attack', 'defend', 'get_combat_stats'],
            'Magical': ['cast_spell', 'channel_mana', 'get_magic_stats']
        }
        capabilities_str = "EliteCard capabilities:\n"
        for interface, methods in capabilities.items():
            capabilities_str += f"- {interface}: {methods}\n"
        return capabilities_str