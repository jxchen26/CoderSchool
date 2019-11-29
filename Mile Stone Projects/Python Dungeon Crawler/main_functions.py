def shop():
    from items import SHOP, ITEM_DATABASE
    from player import ME
    from game_functions import increase_stats
    from os import system

    while True:
        system("cls")
        print("=======Shop======= \n")

        if SHOP == []:
            print("Looks like we've sold out everything")
            return

        for item in SHOP:
            print("~", item, "~")
            for i in ITEM_DATABASE[item].keys():
                if i != "name":
                    print(i, ITEM_DATABASE[item][i])

            print("========== \n")

        print("your gold", ME["money"])
        order = input("\n What you want yo buy(type in name of item or press enter to exit)\n>")

        if order == "exit":
            break
        else:

            # if the order is found
            if order in SHOP:

                if ME["money"] >= ITEM_DATABASE[order]["cost"]:
                    ME["money"] -= ITEM_DATABASE[order]["cost"]
                    SHOP.remove(order)
                    ME["bag"].append(order)
                    increase_stats(order)
                    print("your bag:", ME["bag"])
                else:
                    print("hmm seems like you don't have enough")

            # if the order is not found
            else:
                print("we don't have", order, "for sale")

        input("press enter to continue")


def battle():
    from game_functions import run, magic, level_up
    from os import system
    from player import ME
    from monsters import MONSTER_DATABASE, l1, l2, l1b, l2b
    from random import uniform, choice
    from game_system import GAMESYS

    # get monster
    if GAMESYS["difficulty"] == 1 and GAMESYS["day"] < 10:
        m_name = choice(l1)
    elif GAMESYS["difficulty"] == 2 and 10 < GAMESYS["day"] < 20:
        m_name = choice(l2)
    elif GAMESYS["difficulty"] == 3 and 20 < GAMESYS["day"] < 30:
        m_name = choice(l3)

    # check boss date
    if GAMESYS["day"] == 10:
        m_name = l1b
        GAMESYS["difficulty"] += 1
    elif GAMESYS["day"] == 20:
        GAMESYS["difficulty"] += 1
        m_name = l2b
    # elif GAMESYS["day"]==30:
    #   m_name = l3b
    elif GAMESYS["difficulty"] == 3:
        print("GAME BEATEN")
        quit()

    # get a copy of the monster data
    m = MONSTER_DATABASE[m_name].copy()
    m_hp = m["hp"]

    # begin battle
    while True:
        system("cls")

        # display
        print("! Your were attacked by a", m_name, '! \n')
        print("your health:", "\033[92m" + "█" * int(10 * (ME["hp"] / ME["max_hp"])), ME["hp"], '\033[0m')
        print(m_name, "health:", "\033[92m" + "█" * int(10 * (m["hp"] / m_hp)), m["hp"], '\033[0m')
        print("")

        # player turn
        action = input("1.attack ({}-{}), 2.magic, 3.run >".format(int(ME["atk"] * 0.5), int(ME["atk"] * 1)))
        if action == "1":
            dmg = int(ME["atk"] * uniform(.5, 1))
            print("you hit", m_name, "for", dmg)
            m["hp"] -= dmg

            # check if you've defeated the monster
            if m["hp"] <= 0:
                print("The monster has been slain, well done.")
                ME["exp"] += m["exp"]

                # check if you leved!
                while ME["exp"] >= ME["exp_goal"]:
                    level_up()

                break

        # magic
        elif action == "2":
            magic(m)
            if m["hp"] <= 0:
                print("the monster has been slain. well done.")

                if ME["exp"] >= ME["exp_goal"]:
                    level_up()

                break



        # run
        elif action == "3":
            if run():
                print("You've ESCAPED!")
                break
            else:
                print("THE MONSTER CAUGHT UP TO YOU, your attempt at escaping failed.")

        else:
            print("There is no", action, "command")

        # monster turn
        m_dmg = int(m["atk"] * uniform(0, 1) - ME["def"] * uniform(0, 1))
        if m_dmg < 0:
            m_dmg = 0
        print("the monster hit you for", m_dmg)
        ME["hp"] -= m_dmg
        if ME["hp"] <= 0:
            print("You've been slained by", m_name, "game over.")

            # print summary of run
            # update high score
            GAMESYS["state"] = "Over"
            return

        input("enter to continue")


def explore():
    from player import ME
    from game_functions import calculate_reward, ruin
    from random import choices, randint
    from game_system import GAMESYS

    event = choices(["nothing happens", "encounter monster", "discover ruin", "encounter trap", "discover secret"],
                    [20, 55, 5, 15, 5])

    if event == ["nothing happens"]:
        print("It seems you made it through the day without encountering any monster")

        reward = calculate_reward()
        print("You've found", reward, "gold")

        ME['money'] += reward


    elif event == ["encounter monster"]:
        battle()

    elif event == ["discover ruin"]:
        ruin()

    elif event == ["encounter trap"]:
        x = randint(1, 3)

        print("You've encountered a trap!")
        print("1. RUN ")
        print("2. STAY STILL")
        print("3. CALL FOR HELP")

        answer = input("choose 1,2 or 3 \n >>")

        if answer == x:
            print("You've avoided the trap")

        else:
            print("You took", 10, "dmg")
            ME["hp"] -= 10

    # elif event == ["discover secret"]:
    #   secret_event()


    input("Looks like the day is coming to an end...(press enter to continue)")
    GAMESYS["day"] += 1

