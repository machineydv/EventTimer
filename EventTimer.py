from datetime import date, datetime
from termcolor import colored

from lib.TimeFunctions import *
from lib.DateFunctions import *
from lib.PrintFunctions import *
from lib.Globals import *

current_time = seconds_from_time(datetime.now().strftime("%H:%M:%S"))
current_date = seconds_from_date(date.today().isoformat()) 
current_seconds = current_time + current_date

def EventSeconds(edict: dict):
    if edict["event_timeformat"] == "GMT" or edict["event_timeformat"] == "UTC": #UTC Time
        event_seconds = int(seconds_from_date(edict["event_date"])) + int(seconds_from_time(edict["event_time"])) + int(gmt_to_ktm)
    elif edict["event_timeformat"] == "PCT": #Pacific Time
        event_seconds = int(seconds_from_date(edict["event_date"])) + int(seconds_from_time(edict["event_time"])) +int(pacific_to_ktm)
    elif edict["event_timeformat"] == "EST": #Eastern Time
        event_seconds = int(seconds_from_date(edict["event_date"])) + int(seconds_from_time(edict["event_time"])) + int(est_to_ktm)
    return event_seconds

event_seconds = EventSeconds(event_1)
date, seconds = date_from_seconds(event_seconds-current_seconds)
counter_seconds = seconds_from_date(date) + int(seconds)

try:
    print_from_seconds(counter_seconds, event_1)
except KeyboardInterrupt:
    print(f"{ColorObj.bad} Exiting")
    exit()
