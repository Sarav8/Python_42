# SpellCard (Concrete Implementation)
def __init__(self, name: str, cost: int, rarity: str, effect_type: str)
def play(self, game_state: dict) -> dict
def resolve_effect(self, targets: list) -> dict
