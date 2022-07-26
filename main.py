from kitties import kitties
from treasures import treasures
from dataclasses import dataclass, field
import random


@dataclass
class Backpack:
    treasures: list = field(default_factory=list)
    phonebook: list = field(default_factory=list)
    lives: int = 9
    points: int = 0


def mainloop(backpack):
    user_input = ''
    while user_input != 'q' and backpack.lives != 0:
        user_input = input("---------------\nType 'q' to quit\nType 't' to dig in the trash\nType 'r' to visit the roof\nType 'p' to see your phonebook\n>")
        if user_input == 'r':
            meet_kitty(backpack)
        elif user_input == 't':
            dig_in_the_trash(backpack)
        elif user_input == 'p':
            for kitty in backpack.phonebook:
                print("-----")
                print(kitty.title())
                print("Breed: " + kitties[kitty][0])
                print("Description: " + kitties[kitty][1])
                print("Treasure: " + kitties[kitty][2])
                print("-----")


def homescreen():
    print("--------------------------------\nWelcome to Trash Kitty Love!")
    print(r"""
        |\__/,|   (`\
      _.|o o  |_   ) )
    -(((---(((--------

            """)
    print("The goal of the game is to find true love... or as many trash as you can. And, of course, you have only 9 lives. Be careful, but brave.")
    backpack = Backpack()
    mainloop(backpack)


def dig_in_the_trash(backpack):
    print(r"""

      ,-.       _,---._ __  / \
     /  )    .-'       `./ /   \
    (  (   ,'            `/    /|
     \  `-"             \'\   / |
      `.              ,  \ \ /  |
       /`.          ,'-`----Y   |
      (            ;        |   '
      |  ,-.    ,-'         |  /
      |  | (   |            | /
      )  |  \  `.___________|/
      `--'   `--'

    ...digging
    			""")
    offered_treasures = random.sample(treasures, 2)
    the_treasure = random.choice(offered_treasures)
    choice = input(f"You stumbled upon something, but can't see clearly what it is. Is it {offered_treasures[0]} or {offered_treasures[1]}?\n>")
    if backpack.lives == 0:
        print("---GAME OVER---")
        print(f"Your score is {backpack.points} points")
        homescreen()
    elif choice == the_treasure and the_treasure in backpack.treasures:
        print(f"You already have {the_treasure} in your backpack!")
    elif choice == the_treasure:
        backpack.treasures.append(the_treasure)
        backpack.points += 10
        print(f"Congrats! You found {the_treasure}! It's now in your backpack. 10 points is yours =^.^=")
    elif backpack.lives > 0:
        backpack.lives -= 1
        if backpack.lives == 0:
            print("---GAME OVER---")
            print(f"Your score is {backpack.points} points")
            homescreen()
        else:
            print(f"You lost a life. You have {backpack.lives} lives left.")


def meet_kitty(backpack):
    kitty = random.choice(list(kitties))
    if kitty in backpack.phonebook:
        print(f"You chilled with {kitty} on the roof")
    elif not backpack.treasures:
        print(f"Kitties dig those who dig in the trash. You met {kitty.title()}, but you have nothing to offer.")
    elif kitty not in backpack.phonebook:
        user_input = input(f"You met {kitty.title()}. Offer them one of your treasures: {backpack.treasures}\nHere's a hint: {kitties[kitty][]}>")
        if user_input == kitties[kitty][2]:
            backpack.phonebook.append(kitty)
            backpack.treasures.remove(user_input)
            print(f"{kitty.title()} gave you their number. Call them sometime ;)")
        else:
            print(f"{kitty.title()} is disappointed. They don't like things such as {user_input}.")


homescreen()
