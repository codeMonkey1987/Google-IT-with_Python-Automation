#!/usr/bin/env python3


import requests
import os


desc_dir = os.path.expanduser('~') + '/supplier-data/descriptions/'
url = "http://localhost/fruits/"

#Parse through text files, insert data into a dictionary for each file then append the dictionary to fruits list
for file in os.listdir(desc_dir):
    if file.endswith(".txt"):
        with open(desc_dir + file, 'r') as new_file:
            img_name = os.path.splitext(file)[0]
            data = new_file.read()
            data = data.split('\n')
            fruits = {"name": data[0], "weight": int(data[1].strip(" lbs")), "description": data[2], "image_name": img_name + ".jpeg"}
            r = requests.post(url, json=fruits)