# from random import randint, choice, choices, uniform
from os import system
# from items import SHOP, LOOT, ITEM_DATABASE
# from monsters import MONSTER_DATABASE
from display import *
from player import ME
from game_system import GAMESYS
from game_functions import *
from main_functions import *

# start of our game
show_welcome_message()

# game loop
while GAMESYS["state"] == "not over":
    system('cls')

    show_menu()

    action = input("what you want to do today?")

    if action == "1":
        system("cls")
        explore()

    elif action == "3":
        system("cls")
        show_status()


    elif action == "2":
        system("cls")
        shop()

        input("press enter to continue")

    input("enter to continue")
