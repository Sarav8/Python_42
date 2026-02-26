def mage_counter() -> callable:
    """Create a simple counter that increments on each call."""
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    """Create an accumulator that adds a value to a running total."""
    current_power = initial_power

    def accumulator(amount: int):
        nonlocal current_power
        current_power += amount
        return current_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    """Return a function that applies a specific enchantment to an item."""
    def enchantment(item_name: str):
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, callable]:
    """
    Create a private dictionary and return interface functions to manage it.
    """
    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key: str):
        return memory.get(key, "Memory not found")

    return {
        'store': store,
        'recall': recall
    }


if __name__ == "__main__":
    print("Testing mage counter...")
    mage_count = mage_counter()
    print(f"Call 1: {mage_count()}")
    print(f"Call 2: {mage_count()}")
    print(f"Call 3: {mage_count()}")

    print("\nTesting enchantment factory...")
    flaming_factory = enchantment_factory("Flaming")
    frozen_factory = enchantment_factory("Frozen")
    print(flaming_factory("Sword"))
    print(frozen_factory("Shield"))

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(10)
    print(f"Initial 10, adding 5: {acc(5)}")
    print(f"Current 15, adding 10: {acc(10)}")

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']("secret_word", "Abracadabra")
    print(f"Recall secret: {vault['recall']('secret_word')}")
    print(f"Recall missing: {vault['recall']('non_existent')}")
