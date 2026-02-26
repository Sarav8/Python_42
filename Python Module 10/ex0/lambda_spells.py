def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort a list of artifacts by power in descending order."""
    list_ord = sorted(artifacts, key=lambda art: art['power'], reverse=True)
    return list_ord


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filter mages who have a power level greater than or equal to min"""
    max_power = list(filter(lambda p: p['power'] >= min_power, mages))
    return max_power


def spell_transformer(spells: list[str]) -> list[str]:
    """Transform spell names by wrapping them in asterisks."""
    l_transf = list(map(lambda name_t: f"* {name_t} *", spells))
    return l_transf


def mage_stats(mages: list[dict]) -> dict:
    """Calculate the maximum, minimum, and average power of a list of mages."""
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    powers = list(map(lambda p: p['power'], mages))
    max_p = max(powers)
    min_p = min(powers)
    avg = sum(powers) / len(powers)
    avg_red = round(avg, 2)
    return {
        'max_power': max_p,
        'min_power': min_p,
        'avg_power': avg_red
    }


if __name__ == "__main__":
    spells = ["fireball", "heal", "shield"]
    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'}
    ]

    mages = [
        {'name': 'Ember', 'power': 92, 'element': 'fire'},
        {'name': 'Storm', 'power': 55, 'element': 'lightning'},
        {'name': 'Nova', 'power': 78, 'element': 'light'},
        {'name': 'Sage', 'power': 95, 'element': 'wind'},
        {'name': 'Kai', 'power': 61, 'element': 'water'}
    ]

    print("Testing artifact sorter...")
    print(artifact_sorter(artifacts))

    print("\nTesting spell transformer...")
    print(spell_transformer(spells))

    print("\nTesting power filter...")
    print(power_filter(mages, 80))

    print("\nTesting mage stats...")
    print(mage_stats(mages))
