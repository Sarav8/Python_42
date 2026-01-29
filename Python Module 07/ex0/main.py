from ex0.CreatureCard import CreatureCard
from ex0.Card import Card


print("=== DataDeck Card Foundation ===\n")
print("Testing Abstract Base Class Design:\n")

print("CreatureCard Info:")
fire_dragon = CreatureCard('Fire Dragon', 5, 'Legendary',  7,  5)
playable = fire_dragon.is_playable(6)
print(fire_dragon.get_card_info())

print(f"\nPlaying {fire_dragon.name} with 6 mana available:")
if playable:
    result = fire_dragon.play({})
    print(f"Playable: {fire_dragon.is_playable(6)}")
    print(f"Play result: {result}")


goblin = CreatureCard('Goblin Warrior', 2, 'Common', 2, 2)
attack1 = fire_dragon.attack_target(goblin)
print(f"\n{fire_dragon.name} attacks {goblin.name}:")
print(f"Attack result: {attack1}")

print("\nTesting insufficient mana (3 available):")
print(f"Playable: {fire_dragon.is_playable(3)}")
print("Abstract pattern successfully demonstrated!")

