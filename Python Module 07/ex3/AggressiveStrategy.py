from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Strategy that focuses on high damage and low-cost creatures."""

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Play offensive cards and target the enemy player."""
        cards_played = []
        mana_used = 0
        limit = 8

        for card_str in hand:
            name, cost_str = card_str.split("(")
            name = name.strip()
            cost = int(cost_str.strip(")"))

            if mana_used + cost <= limit:
                cards_played.append(name)
                mana_used += cost

        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': ['Enemy Player'],
            'damage_dealt': mana_used + 3
        }

    def get_strategy_name(self) -> str:
        """Return the name of the strategy."""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """Return prioritized list of targets."""
        return available_targets
