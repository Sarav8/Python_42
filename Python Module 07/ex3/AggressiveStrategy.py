from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        creatures_played = 0

     
        for c in hand:
            nam, cost_str = c.split("(")
            nam = nam.strip()
            cost = int(cost_str.strip(")"))

            if "Goblin" in nam or "Dragon" in nam: 
                if mana_used + cost <= 8: 
                    cards_played.append(nam)
                    mana_used += cost
                    creatures_played += 1

        for c in hand:
            nam, cost_str = c.split("(")
            nam = nam.strip()
            cost = int(cost_str.strip(")"))

            if "Fireball" in nam or "Lightning Bolt" in nam:
                if mana_used + cost <= 8:  
                    cards_played.append(nam)
                    mana_used += cost

        result = {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': ['Enemy Player'],
            'damage_dealt': mana_used
        }

        return result

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets
