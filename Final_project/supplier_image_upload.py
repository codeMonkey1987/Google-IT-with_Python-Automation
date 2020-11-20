#!/usr/bin/env python3

import os
import requests


url = "http://localhost/upload/"
img_dir = os.path.expanduser('~') + '/supplier-data/images/'
#Uploads JPEG to specified destination
for file in os.listdir(img_dir):
    if file.endswith(".jpeg"):
        with open (img_dir + file, 'rb') as opened:
            r = requests.post(url, files={'file': opened})