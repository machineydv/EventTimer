from os import system
from time import sleep
from termcolor import colored

from lib.Globals import *
from lib.TimeFunctions import *

def print_from_seconds(second, edict):
    system('clear')
    while second > 2:
        nepal = colored(time_from_seconds(second), color='cyan')
        india = colored(time_from_seconds(second-seconds_from_time('00:15:00')), color='yellow')
        universal = colored(time_from_seconds(second-seconds_from_time('05:45:00')), color='red')
        print("\x1b[%d;%dH" % (1, 1), end="")
        print(f"{ColorObj.information} Event: {edict['event_name']}")
        print(f"{ColorObj.good} Nepali Time: {nepal}, Indian Time: {india}, Universal Time: {universal}")
        sleep(1)
        second -= 1
    return True
