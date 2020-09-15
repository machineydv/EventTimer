from lib.ColoredObject import Color
from lib.TimeFunctions import seconds_from_time

event_name = 'BsidesBOS CTF'  #Event Name
event_date = '2020-09-26'   #Event Date
event_time = '19:00:00' #Event Time
event_timeformat = "GMT" #Event Timeformat

pacific_to_ktm = seconds_from_time('0:45:00') #For Nepal
gmt_to_ktm = seconds_from_time('5:45:00') #For Nepal
est_to_ktm = seconds_from_time('04:00:00')
est_to_ktm += seconds_from_time('5:45:00') #For Nepal

ColorObj = Color()
