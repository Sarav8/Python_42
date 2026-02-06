from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main():
    """Demonstrate the Abstract Factory and Strategy patterns."""
    print("=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    aggressive_strategy = AggressiveStrategy()

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {aggressive_strategy.__class__.__name__}")

    types = factory.get_supported_types()
    print(f"Available types: {types}")

    engine = GameEngine()
    engine.configure_engine(factory, aggressive_strategy)

    print("\nSimulating aggressive turn...")
    turn_result = engine.simulate_turn()

    print("\nTurn execution:")
    print(f"Strategy: {aggressive_strategy.get_strategy_name()}")
    print(f"Actions: {turn_result}")

    game_report = engine.get_engine_status()
    print("\nGame Report:")
    print(game_report)
    message = "Abstract Factory + Strategy Pattern: Maximum flexibility!"
    print(f"\n{message}")


if __name__ == "__main__":
    main()
