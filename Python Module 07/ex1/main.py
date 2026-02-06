from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard


def main():
    """Demonstrate deck builder and polymorphism."""
    print("=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    deck = Deck()
    spell = SpellCard("Lightning Bolt", 3, "epic", "damage")
    artifact = ArtifactCard("Mana Crystal", 2, "rare", 3,
                            "Permanent: +1 mana per turn")
    creature = CreatureCard("Fire Dragon", 5, "legendary", 5, 8)

    deck.add_card(spell)
    deck.add_card(artifact)
    deck.add_card(creature)

    analysis = deck.get_deck_stats()
    print(f"Deck stats: {analysis}")

    print("\nDrawing and playing cards:")
    card = deck.draw_card()
    while card:
        result = card.play(game_state={})
        card_type = type(card).__name__
        print(f"\nDrew: {card.name} ({card_type})")
        print(f"Play result: {result}")
        card = deck.draw_card()

    print("\nPolymorphism in action: Same interface, different behaviors!")


if __name__ == "__main__":
    main()
