from lib.ColoredObject import Color
from lib.TimeFunctions import seconds_from_time
# Note: For GMT only if event occurs in GMT+2 then subtract 2 hour, i.e if sth start in 17:00:00 GMT +2 then, set 15:00:00 with timeformat GMT

event_1 = {
    "event_name":"BsidesBOS CTF",
    "event_date":"2020-09-26",
    "event_time":"19:00:00",
    "event_timeformat":"EST",
    "event_description":"A CTF"
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
    "event_name":"CyberSecurity Challenge 2020 (Reply)",
    "event_date":"2020-10-09",
    "event_time":"19:30:00",
    "event_timeformat":"CEST"
}


pacific_to_ktm = seconds_from_time('00:45:00') #For Nepal
gmt_to_ktm = seconds_from_time('05:45:00') #For Nepal
est_to_ktm = seconds_from_time('04:00:00')
est_to_ktm += seconds_from_time('05:45:00') #For Nepal
cest_to_ktm = seconds_from_time('03:45:00') #For Nepal

ColorObj = Color()
