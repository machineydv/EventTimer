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

event_3 = {
    "event_name":"h1-2010 Virtual Hacking (https://www.verizonmedia.com/insights/h1-2010--overview)",
    "event_date":"2020-09-22",
    "event_time":"11:00:00",
    "event_timeformat":"EST"
}

event_4 = {
    "event_name":"Lupin XSS Writeup",
    "event_date":"2020-09-18",
    "event_time":"17:00:00", #+- 2
    "event_timeformat":"GMT"
}


pacific_to_ktm = seconds_from_time('0:45:00') #For Nepal
gmt_to_ktm = seconds_from_time('5:45:00') #For Nepal
est_to_ktm = seconds_from_time('04:00:00')
est_to_ktm += seconds_from_time('5:45:00') #For Nepal

ColorObj = Color()
