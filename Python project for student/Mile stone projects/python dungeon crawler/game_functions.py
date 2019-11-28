class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def level_up():
    from player import ME
    from random import randint
    print("\n YOU'VE LEVELED UP TO LEVEL", ME["lvl"] + 1)

    # change level and exp
    ME["exp"] = abs(ME["exp"] - ME["exp_goal"])
    print("my exp>", ME["exp"])
    ME["lvl"] += 1
    ME["exp_goal"] = ME['exp_goal'] * 2

    # generate random numbers
    n1 = randint(1, 5)
    n2 = randint(1, 5)
    n3 = randint(1, 5)
    n4 = randint(1, 5)

    # show
    print("=====Stats=====")
    print("Hp:", ME["max_hp"], color.OKGREEN + "  +", n1, color.ENDC)
    print("Atk:", ME["atk"], color.OKGREEN + "  +", n2, color.ENDC)
    print("Def:", ME["def"], color.OKGREEN + "  +", n3, color.ENDC)
    print("magic:", ME["magic"], color.OKGREEN + "  +", n4, color.ENDC)
    print("\n")

    # increase stats
    ME["max_hp"] += n1
    ME["atk"] += n2
    ME["def"] += n3
    ME["magic"] += n4


def get_item():
    from items import LOOT
    from random import randint
    return LOOT.pop(randint(0, len(LOOT) - 1))


def increase_stats(item_name):
    """
      This function increases the stats of the player once they get an item
      - input: name of item (str)
      - return : None
    """
    from player import ME
    from items import ITEM_DATABASE

    print("increase stats for", item_name)

    for stat in ITEM_DATABASE[item_name].keys():
        if stat == "hp":
            ME["max_hp"] += ITEM_DATABASE[item_name][stat]
        elif stat != "name" and stat != "cost":
            ME[stat] += ITEM_DATABASE[item_name][stat]


def calculate_reward(t1=55, t2=40, t3=5):
    from random import choices, randint

    x = choices([1, 2, 3], [t1, t2, t3])

    if x == "1":
        return randint(0, 400)
    elif x == "2":
        return randint(400, 700)
    else:
        return randint(700, 1000)


def magic(target=None):
    from player import ME
    from random import randint
    if ME["spells"] == []:
        print("seems like you don't know any spells")
        return

    # list a bunch of spells you can use
    print(ME["spells"])

    spell = input("Casting.....(type in the name of spell):")
    if spell in ME["spells"]:

        # make sure its a valid number
        try:
            guess = int(input("guess a number between 1-100:"))
        except TypeError:
            print("YOUR SPELL MISCASTED")
            return

        # make sure its within range
        if guess > 100 or guess < 1:
            print("YOUR SPELL MISCASTED")
            return

        x = randint(1, 100)

        if x == guess:
            e = 10
        else:
            e = 10 / abs(guess - x)

        # look up the spell functions and pass target as paramenter
        from spells import SPELL_DATABASE
        SPELL_DATABASE[spell](e, target)

        return


def run():
    from random import randint

    if randint(1, 3) == 3:
        return True

    return False


def ruin():
    from puzzles import QUESTIONS
    from random import randint
    from player import ME

    x = randint(1, len(QUESTIONS))
    print(QUESTIONS[x]["question"])

    answer = input(">>")

    if answer == QUESTIONS[x]["answer"]:
        reward = get_item()
        print("You've solved the puzzle ")
        print("You found a", reward)
        ME['bag'].append(reward)
        increase_stats(reward)



