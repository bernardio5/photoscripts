import csv
import os
from shutil import copyfile
import zipfile
import random
import sys
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

Image.MAX_IMAGE_PIXELS = None

# goal: 20y of pics, organiz


for root, dirs, files in os.walk("D:\\homeServer\\famPics\\2016\\02"):
    for file in files:
        if ('(' in file):
            fullPath = os.path.join(root, file)
            print("delete " + fullPath)
            os.remove(fullPath)