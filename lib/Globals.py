from lib.ColoredObject import Color
from lib.TimeFunctions import seconds_from_time

event_1 = {
    "event_name":"BsidesBOS CTF",
    "event_date":"2020-09-26",
    "event_time":"19:00:00",
    "event_timeformat":"EST"
}

event_2 = {
    "event_name":"HTB Crossfit Release",
    "event_date":"2020-09-19",
    "event_time":"19:00:00",
    "event_timeformat":"UTC"
}

event_2 = {
    "event_name":"h1-2010 Virtual Hacking",
    "event_date":"2020-09-22",
    "event_time":"11:00:00",
    "event_timeformat":"EST"
}


pacific_to_ktm = seconds_from_time('0:45:00') #For Nepal
gmt_to_ktm = seconds_from_time('5:45:00') #For Nepal
est_to_ktm = seconds_from_time('04:00:00')
est_to_ktm += seconds_from_time('5:45:00') #For Nepal

ColorObj = Color()
