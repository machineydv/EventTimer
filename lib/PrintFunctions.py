from time import sleep
from termcolor import colored

from lib.Globals import *
from lib.TimeFunctions import *

def counter_time_from_seconds(second):
    while second > 2:
        nepal = time_from_seconds(second)
        india = time_from_seconds(second-seconds_from_time('00:15:00'))
        pacific = time_from_seconds(second-seconds_from_time('00:45:00'))
        print("{} Nepali Time: {}, Indian Time: {}, Pacific region/time: {}".format(
            ColorObj.good,
            colored(nepal, color='cyan'),
            colored(india, color='yellow'),
            colored(pacific, color='red')
            ) + '\r',
            end=""
        )
        #print("{} Nepali Time: {}".format(ColorObj.good, colored(nepal, color='cyan')) + '\r', end="")
        sleep(1)
        second -= 1
    return "{} {}".format(ColorObj.good,time_from_seconds(second))
