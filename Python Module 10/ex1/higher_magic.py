def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """Returns a function that calls two spells and returns a tuple."""
    def combiner(*args, **kwargs):
        res1 = spell1(*args, **kwargs)
        res2 = spell2(*args, **kwargs)
        return res1, res2
    return combiner


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """Returns a function that multiplies the base spell result."""
    def amplified_spell(*args, **kwargs):
        result = base_spell(*args, **kwargs)
        return result * multiplier
    return amplified_spell


def conditional_caster(condition: callable, spell: callable) -> callable:
    """Returns a function that only casts if condition is True."""
    def condition_verify(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return condition_verify


def spell_sequence(spells: list[callable]) -> callable:
    """Returns a function that executes a list of spells in order."""
    def sequence(*args, **kwargs):
        results = []
        for s in spells:
            res = s(*args, **kwargs)
            results.append(res)
        return results
    return sequence


if __name__ == "__main__":
    def heal(target):
        return f"Heals {target}"

    def fireball(target):
        return f"Fireball hits {target}"

    def damage_base(target):
        return 10

    def tiene_mana(puntos):
        return puntos >= 50

    print("Testing spell combiner...")
    combiner = spell_combiner(fireball, heal)
    resul_comb = combiner("Dragon")
    print(f"Combined spell result: {resul_comb[0]}, {resul_comb[1]}")

    print("\nTesting power amplifier...")
    multipli = power_amplifier(damage_base, 3)
    val_amplifi = multipli("Dragon")
    val_orig = damage_base("Dragon")
    print(f"Original: {val_orig}, Amplified: {val_amplifi}")

    print("\nTesting conditional caster...")
    cond_cast = conditional_caster(tiene_mana, fireball)
    print(f"With mana (80): {cond_cast(80)}")
    print(f"Without mana (20): {cond_cast(20)}")

    print("\nTesting spell sequence...")
    seq = spell_sequence([fireball, heal])
    results = seq("Knight")
    print(f"Sequence result: {results}")
