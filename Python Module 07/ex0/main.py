from ex0.CreatureCard import CreatureCard


def main():
    """Demonstrate the base functionality of the Card system."""
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    print("CreatureCard Info:")
    fire_dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    print(fire_dragon.get_card_info())

    print(f"\nPlaying {fire_dragon.name} with 6 mana available:")
    print(f"Playable: {fire_dragon.is_playable(6)}")

    if fire_dragon.is_playable(6):
        result = fire_dragon.play({})
        print(f"Play result: {result}")

    goblin = CreatureCard('Goblin Warrior', 2, 'Common', 2, 2)
    attack1 = fire_dragon.attack_target(goblin)
    print(f"\n{fire_dragon.name} attacks {goblin.name}:")
    print(f"Attack result: {attack1}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {fire_dragon.is_playable(3)}")
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
