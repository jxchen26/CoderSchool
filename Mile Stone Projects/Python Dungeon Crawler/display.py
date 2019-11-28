class color:
    HEADER = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    FAIL = '\033[91m'
    end = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


c = color()


def show_status():
    from player import ME
    from items import ITEM_DATABASE

    stat_from_item = {
        'hp': 0,
        'atk': 0,
        'def': 0,
        "magic": 0
    }

    for item in ME["bag"]:
        for stat in ITEM_DATABASE[item].keys():
            if stat != "name" and stat != "cost":
                stat_from_item[stat] += ITEM_DATABASE[item][stat]

    print("=====Stats=====")
    print("LVL:", ME['lvl'])
    print("Hp:", ME["hp"], '|', ME['max_hp'], c.yellow + '+', str(stat_from_item['hp']) + c.end)
    print("Atk:", ME["atk"], c.yellow + '+', str(stat_from_item['atk']) + c.end)
    print("Def:", ME["def"], c.yellow + '+', str(stat_from_item['def']) + c.end)
    print("magic:", ME["magic"], c.yellow + '+', str(stat_from_item['magic']) + c.end)
    print("exp goal:", ME["exp_goal"])
    print("current exp:", ME["exp"])
    print("Gold:", ME["money"])

    print("\n")

    print("====equipment====")
    print(ME['bag'])
    print("\n")
    input("press enter to exit")


def show_welcome_message():
    print("\n~Welcome to the dungeon adventurer~")


def show_menu():
    from game_system import GAMESYS
    print("==========Day:", GAMESYS["day"], "============")
    print("1. Explore dungeon")
    print("2. Shop")
    print("3. view inventory")

