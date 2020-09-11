from lib.ColoredObject import Color
from lib.TimeFunctions import seconds_from_time

event_name = 'HTB Compromised Box Release'  #Event Name
event_date = '2020-09-12'   #Event Date
event_time = '19:00:00' #Event Time

pacific_to_ktm = seconds_from_time('0:45:00') #For Nepal
gmt_to_ktm = seconds_from_time('5:45:00')   #For Nepal

ColorObj = Color()
