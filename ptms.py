#! /usr/bin/env python3

import ptlib

ver='PTMS=1.0, PTLIB=' + ptlib.ver

from config import config

### !!!IMPORTS!!! ###
import sys
import time

### !!!FUNCTIONS!!! ###
def get_values():
    global coretmp
    global fanspd
    global batlvl
    global batsts
    coretmp= int(ptlib.cat(config.cpu_temp)) / 1000
    if config.fan_speed[0]==False:
        fanspd=str('N/A')
        batlvl = int(ptlib.cat(config.battery))
        batsts = str(ptlib.cat(config.battery_status))
    else:

        fanspd= int(ptlib.cat(config.fan_speed)) / 256 * 100
        batlvl=int(ptlib.cat(config.battery))
        batsts=str(ptlib.cat(config.battery_status))

def monitorserverhlp():
    helptxt= """
help text for PTEC monitor server
commands:-
    help                displays help text
    start <output file> starts monitor server outputting html to output file
    """
    print(helptxt)

def start():
    while True:
        get_values()
        data=(str(coretmp), str(fanspd), str(batlvl))
        formatted_data= ptlib.html.p('core temp: ' + data[0]) + '\n'
        formatted_data+= ptlib.html.p('fan power: ' + data[1] + '%') + '\n'
        formatted_data+= ptlib.html.p('battery level: ' + data[2] + '%')
        ptlib.echotofile(args[2], ptlib.html.html(ptlib.html.header(
            ptlib.html.title('PTEC MonitorServer on ' + config.hostname + '(Version: ' + ver + ')') + ptlib.html.css('./style.css')) + ptlib.html.body(
            ptlib.html.center('PTMS-PTEC MonitorServer | ver:' + ver) + formatted_data)))
        time.sleep(0.1)

### !!!MAIN CODE!!! ###

args=sys.argv
usagehlp='!!!INVALID USAGE!!! (type \'monitorserver help\' for usage help) Quitting.'
if len(args) == 1:
    print(usagehlp)
    exit()
if args[1] == 'help':
    monitorserverhlp()
elif args[1] == 'start':
    if len(args) == 3:
        start()
    else:
        print('!!!OUTPUT WAS NOT SPECIFIED!!! Quitting.')
else:
    print(uagehlp)
