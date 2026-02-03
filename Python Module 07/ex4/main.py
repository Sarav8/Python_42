from ex4.Rankable import Rankable
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform

def main():
    print("=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()
    print("Registering Tournament Cards...")

    fire_dragon = TournamentCard(name="Fire Dragon", cost=5, rarity="Legendary", id="dragon_001")
    ice_wizard = TournamentCard(name="Ice Wizard", cost=4, rarity="Epic", id="wizard_001")

    print(f"{fire_dragon.name} (ID: {fire_dragon.id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {fire_dragon.rating}")
    print(f"- Record: {fire_dragon.wins}-{fire_dragon.losses}")
    platform.register_card(fire_dragon)

    print(f"{ice_wizard.name} (ID: {ice_wizard.id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {ice_wizard.rating}")
    print(f"- Record: {ice_wizard.wins}-{ice_wizard.losses}")
    platform.register_card(ice_wizard)

    print("Creating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print("Match result:", match_result)

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for line in leaderboard:
        print(line)

    print("Platform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")

if __name__ == "__main__":
    main()
