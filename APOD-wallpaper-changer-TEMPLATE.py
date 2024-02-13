#!/usr/bin/env python

import time
import json
import requests
import re
import struct
import ctypes

apirawdata = requests.get("https://api.nasa.gov/planetary/apod?api_key=<nnYV5OIeodUmpWegH54Roc55LuZwCuHE4RwAC93d>&hd=true")  #NOTE: REPLACE <INSERT YOUR API KEY HERE> WITH YOUR API KEY (DON'T INCLUDE <>)

apidata = apirawdata.json()

hdurl = apidata['hdurl']

image = requests.get(hdurl, allow_redirects=True)

open ('background.jpg', 'wb').write(image.content)

time.sleep(300)

PATH = 'C:\\PATH\\TO\\BACKGROUND\\IMAGE\\background.jpg' # NOTE: USE DOUBLE BACKSLASHES!
SPI_SETDESKWALLPAPER = 20

ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PATH, 3)
