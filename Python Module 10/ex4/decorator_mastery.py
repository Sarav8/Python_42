import functools
import time


def spell_timer(func: callable) -> callable:
    """Decorator that measures function execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    """Decorator factory that validates power levels."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get('power')
            if power is None:
                power = args[-1] if args else 0
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    """Decorator that retries failed spells upon exception."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Name is valid if >= 3 chars and contains only letters/spaces."""
        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Successfully casts the spell if power validation passes."""
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    print("Testing spell timer...")
    print(f"Result: {fireball()}")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Albus"))
    print(guild.validate_mage_name("A1"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))

    @retry_spell(max_attempts=3)
    def unstable_spell():
        raise Exception("Boom!")

    print("\nTesting retry spell...")
    print(unstable_spell())
