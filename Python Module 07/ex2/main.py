from ex2.EliteCard import EliteCard


def main():
    """Demonstrate the power of multiple inheritance and interfaces."""
    print("=== DataDeck Ability System ===\n")
    elite = EliteCard("Arcane Warrior", 5, "rare", 5, 3, 10)
    print(elite.get_capabilities())

    print("\nPlaying Arcane Warrior (Elite Card):")
    print("\nCombat phase:")
    print(f"Attack result: {elite.attack('Enemy')}")
    print(f"Defense result: {elite.defend(5)}")

    print("\nMagic phase:")
    targets = ['Enemy1', 'Enemy2']
    print(f"Spell cast: {elite.cast_spell('Fireball', targets)}")
    print(f"Mana channel: {elite.channel_mana(3)}")
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
