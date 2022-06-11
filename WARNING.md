* You could miss important events. Please pull request to make it better
* Providing wrong date time causes error. GIGO. 
* Cross check the time generated.
* Also, this generates for Nepal/India defaultly. To change settings go to lib/Globals.py
* EST time are different by 1hr on some time formats 

"""
* Places that use Eastern Standard Time (EST) when observing standard time (autumn/winter) are five hours behind Coordinated Universal Time (UTC−05:00). Eastern Daylight Time (EDT), when observing daylight saving time (spring/summer), is four hours behind Coordinated Universal Time (UTC−04:00). 
"""
* Also, it should be noted that running python3 for long time, days may cause incorrect time (not sure) as some milliseconds are lost in computin
* Passed events / Past events may cause error
