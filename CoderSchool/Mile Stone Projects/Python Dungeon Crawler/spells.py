def heal(e, target="player"):
    from player import ME

    ME['hp'] += int(ME["magic"] * e)
    if ME['hp'] > ME["max_hp"]:
        ME["hp"] = ME["max_hp"]

    print("\n")
    print("You've healed for", int(ME["magic"] * e))
    return


def fireball(e, target="monster"):
    from player import ME
    target["hp"] -= int(ME["magic"] * e)

    print("Fireball hits the monster for", int(ME['magic'] * e))


SPELL_DATABASE = {
    "heal": heal,
    "fireball": fireball,
}


