import random

def simulateBattle(p1, p2) -> None:
    """Run a turn‑based fight until one character's HP reaches 0."""
    # Resets hp
    p1.reset()
    p2.reset()

    print("\nBattle start!")
    round_no = 1
    while p1.is_alive() and p2.is_alive():
        print(f"\nRound {round_no}:")
        # Randomly decide who attacks first each round (adds variety)
        attacker, defender = (p1, p2) if random.random() < 0.5 else (p2, p1)

        # 
        attacker.attack()
        defender.receive_damage(attacker.damage)
        print(f"{type(defender).__name__} takes {attacker.damage} damage") # {type(defender).__name__} = show character class
        print(f"(HP left {defender.hp})")
        if not defender.is_alive():
            break # if hp < 0 breaks
        
        print()
        defender.attack()
        attacker.receive_damage(defender.damage)
        print(f"{type(attacker).__name__} takes {defender.damage} damage")
        print(f"(HP left: {attacker.hp})")
        if not attacker.is_alive():
            break # if hp < 0 breaks
        
        try:
            input("\nPress enter to continue")
        except Exception:
            pass

        round_no += 1

    # Announce winner
    winner = p1 if p1.is_alive() else p2
    loser  = p2 if winner is p1 else p1
    print(f"\n*** {type(winner).__name__} wins! ***")
    print(f"{type(loser).__name__} is defeated with 0 HP.")
    print("*** End of simulation ***")



    return None