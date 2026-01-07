def ft_achievement_tracker():
    print("=== Achievement Tracker System ===\n")
    ach_alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    ach_bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    ach_charlie = {
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist',
    }
    print(f"Player alice achievements: {ach_alice}")
    print(f"Player bob achievements: {ach_bob}")
    print(f"Player charlie achievements: {ach_charlie}\n")

    print("=== Achievement Analytics ===")
    all_ach = ach_alice.union(ach_charlie, ach_bob)
    print(f"All unique achievements: {all_ach}")
    print(f"Total unique achievements: {len(all_ach)}\n")

    common_ach = ach_alice.intersection(ach_charlie, ach_bob)
    unique_ali = ach_alice.difference(ach_bob)
    unique_bob = ach_bob.difference(ach_alice)
    print(f"Common to all players: {common_ach}")
    rare_ach = (
        ach_alice.difference(ach_bob.union(ach_charlie))
        .union(ach_bob.difference(ach_alice.union(ach_charlie)))
        .union(ach_charlie.difference(ach_alice.union(ach_bob)))
    )
    print(f"Rare achievements (1 player): {rare_ach}\n")

    diff_ali_bob = ach_alice.intersection(ach_bob)
    print(f"Alice vs Bob common: {diff_ali_bob}")
    print(f"Alice unique: {unique_ali}")
    print(f"Bob unique: {unique_bob}")


if __name__ == "__main__":
    ft_achievement_tracker()
