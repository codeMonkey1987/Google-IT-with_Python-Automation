#!/usr/bin/env python3

from PIL import Image
import os


img_dir = os.path.expanduser('~') + '/supplier-data/images/'


#Iterate through images in directory then resize, convert to RGB, then save as jpeg#
for file in os.listdir(img_dir):
    if "tiff" in file:
        name = os.path.splitext(file)[0]
        new_im = Image.open(img_dir + file)
        new_im.resize((600, 400)).convert("RGB").save(img_dir + name + '.jpeg')
        new_im.close()
    else:
        print("Could not convert {}".format(file))