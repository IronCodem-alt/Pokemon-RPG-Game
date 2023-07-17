import random
import os
import sys
import time
from time import sleep
from poke_files import title
from poke_data import pokelist


def slowPrint(text, slptime):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(slptime)


def clear():
    os.system('clear')


# COLOURS
strong = '\033[1m'
normal = '\033[0m'

gold = "\033[0;33m"

pale = '\033[38;2;107;90;0m'
turquoise = '\033[38;2;0;255;255m'
teal = '\033[38;2;0;170;170m'

yellow = '\033[38;2;255;225;0m'
green = '\033[38;2;00;160;00m'
blue = '\033[38;2;0;30;255m'
orange = '\033[38;2;230;190;0m'
purple = '\033[38;2;130;0;250m'
red = '\033[0;31m'
brown = '\033[38;2;135;62;35m'

white = '\033[38;2;255;255;255m'
platinum = '\033[38;2;205;190;205m'
dark = '\033[38;2;100;100;100m'

# [POKÉMON INTRO THEME]
slowPrint(title, 0.005)

# NEW PLAYER
n = name_auth = input(f"{normal}\n\nName:{dark} ")


def File():
    f = open(n + "_PLYR.py", "w+")
    f.write(f"from poke_data import {starter}")
    f.write("\n\nname = '" + n + "'")
    f.write("\nstarter = " + starter)
    f.write("\n\nPokémon_met = 0\nPokémon_caught = 0")
    f.close()


if os.path.exists(f"{name_auth}_PLYR.py"):
    print(f"{white}\n  Found file(s)...")
    time.sleep(0.5)
    clear()
    print("Loading file...")
    time.sleep(2.5)
    clear()

else:
    print(f"{white}\n  File not found...")
    time.sleep(0.5)
    clear()
    print("Creating file...")
    time.sleep(2.5)
    clear()

    File()

    print(f"Choose a {yellow}starter Pokémon{white}:")
    starter = input(
        f"{green}Bulbasaur{white} or {red}Charmander{white} or {blue}Squirtle{white} -{dark} "
    )
    clear()

    def poké_stater():
        open(f"{name_auth}_PLYR.py", "w+")


def wild_pokémon():
    random_pokémon = random(pokelist)
    print(f"You found a {pale}{random_pokémon}{white}!")


if starter == "Bulbasaur":
    print(f"{white}Welcome {dark}{n}!")
    print(f"{white}You have obtained {green}{starter}{white}!")

if starter == "Charmander":
    print(f"{white}Welcome {dark}{n}!")
    print(f"{white}You have obtained {red}{starter}{white}!")

if starter == "Squirtle":
    print(f"{white}Welcome {dark}{n}!")
    print(f"{white}You have obtained {blue}{starter}{white}!")

    while True:
        ch = input(
            f"{white}Type 'find' to {purple}find{purple} {yellow}Pokémon{white} or 'save and exit' to {purple}save and exit{white} -{dark} "
        ).lower()

        if (ch == "save and exit"):
            f = open(n + "_PLYR.py", "w+")
            f.write(f"from poke_data import {starter}")
            f.write("\n\nname = '" + n + "'")
            f.write("\nstarter = " + starter)
            f.write("\n\nPokémon_met = 0\nPokémon_caught = 0")
            f.close()
            clear()
            time.sleep(0.5)
            auto = 0
            sys.exit('Progress Saved.\n' + clear())

        if (ch == "find"):
            f = open(n + "_PLYR.py", "w+")
            f.write(f"from poke_data import {starter}")
            f.write("\n\nname = '" + n + "'")
            f.write("\nstarter = " + starter)
            f.write("\n\nPokémon_met = 0\nPokémon_caught = 0")
            f.close()
            clear()
            time.sleep(0.5)
            auto = 0
            sys.exit('Progress Saved.\n' + clear())
