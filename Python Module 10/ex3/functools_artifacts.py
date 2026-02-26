from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    """Combine spell powers using a specified operation."""
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    func_choose = operations[operation]
    return reduce(func_choose, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """Create enchantment functions with fixed power and element."""
    return {
        'fire_enchant': partial(base_enchantment, power=50, element="fire"),
        'ice_enchant': partial(base_enchantment, power=50, element="ice"),
        'lightning_enchant': partial(base_enchantment,
                                     power=50,
                                     element="lightning")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number using memoization."""
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    """Create a dispatcher that handles different spell input types."""
    @singledispatch
    def dispatcher(spell):
        return f"Generic effect: {spell}"

    @dispatcher.register(int)
    def _(spell):
        return f"Damage spell dealt {spell} points"

    @dispatcher.register(str)
    def _(spell):
        return f"Applied enchantment: {spell}"

    @dispatcher.register(list)
    def _(spell):
        return f"Multi-cast: {', '.join(map(str, spell))}"

    return dispatcher


if __name__ == "__main__":
    powers = [10, 20, 30, 40]
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(100))
    print(cast("Shield"))

    def base_enchantment(item, power, element):
        """Base function to create enchantments."""
        return f"{item} enchanted with {element} power {power}"

    print("\nTesting partial_enchanter...")
    enchants = partial_enchanter(base_enchantment)
    print(enchants['fire_enchant']("Sword"))
    print(enchants['ice_enchant']("Shield"))
    print(enchants['lightning_enchant']("Helmet"))
