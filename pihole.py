


#!/usr/bin/python

import urllib2
import os

#checks to see if PH01 is up

def internet_on():
    try:
        urllib2.urlopen('http://192.168.1.13/admin', timeout=5)
        return True
    except urllib2.URLError as err:
        return False

#if Internet is up sync all lists from PH01 to PH02, if down enable PH02

if internet_on():
        print ("PH01 is running")

else:
        print ("PH01 is down, reverting to PH02")
        os.system('pihole enable')


