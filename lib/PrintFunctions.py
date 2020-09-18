from time import sleep
from termcolor import colored

from lib.Globals import *
from lib.TimeFunctions import *

def print_from_seconds(second, edict):
    Nepal = colored(time_from_seconds(second), color='cyan')
    India = colored(time_from_seconds(second-seconds_from_time('00:15:00')), color='yellow')
    Universal = colored(time_from_seconds(second-seconds_from_time('05:45:00')), color='red')
    print(f"{ColorObj.information} Event: {edict['event_name']}")
    print(f"{ColorObj.good} Nepali Time: {Nepal}, Indian Time: {India}, Universal Time: {Universal}")
    return True
