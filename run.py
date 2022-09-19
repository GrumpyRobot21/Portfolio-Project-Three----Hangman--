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