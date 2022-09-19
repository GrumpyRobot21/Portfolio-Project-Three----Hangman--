import random  # random choice method
from gamewords import words  # custom gameword list
import keyboard  # hotkey support for user interaction
import string  # ascii alphabet function
import time  # time sleep function
import pyfiglet  # big letter graphics module


class Colortext:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    BLUE = '\033[0;34m'
    YELLOW = '\033[1;33m'
    BOLD = '\033[1m'

def start_intro():
    """
    Generates game options for player: intro to the game, difficulty, rules.
    """
    print(Colortext.BOLD + Colortext.YELLOW + """
        _____________________________________________
       |_____________________________________________|
         ||                              \ \     |  |
         ||                               \ \    |  |
        /==\                               \ \   |  |
       |____|                               \ \  |  |
       |____|                                \ \ |  |
       |____|                                 \ \|  |
       //  \\\                                  \ |  |
      //    \\\                                  \|  |
     //      \\\                                  |  |
    ||        ||
    ||        ||
    ||        ||
     \\\      // 
      \\\    //
       \\\__// 
    """)
    print(Colortext.BLUE + Colortext.BOLD + "Welcome to ye olde game of HANGMAN!!!!\n\nYou the player must carefully select letters in the vain hope of avoiding the gallows \nby guessing the word before it's too late!\n\nCan you cheat the hangmans noose in time?  Find out....if you dare!\n")

    print(Colortext.BLUE + Colortext.BOLD + "Enter " +Colortext.GREEN + Colortext.BOLD + "'p' "+ Colortext.BLUE + Colortext.BOLD +  "to continue: ")

    run = input('\n')
    if run != ('p'):
        print(Colortext.GREEN + Colortext.BOLD +"\n\nWRONG KEY!!! (I would go for the easy setting if I were you...). \n\nPress 'p' to continue: ")
        time.sleep(3)
        print('\033c', end='')  # clears the console - \033 is the ASCII escape character.
        start_intro()
    else:
        print(Colortext.YELLOW + Colortext.BOLD + '\n\nGOOD LUCK!')
        time.sleep(2)
        print('\033c', end='')  # clears the console - \033 is the ASCII escape character.
        game_rules()