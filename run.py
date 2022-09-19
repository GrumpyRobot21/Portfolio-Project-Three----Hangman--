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