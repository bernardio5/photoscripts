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

# goal: 20y of pics, organized by year, by month, no duplicates. 
# source is all dirs in /familyData
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class pic: 
    def __init__(self):
        self.sourcePath = " "
        self.year = "2000"
        self.month = "01"
        self.targetDir = " "
        self.mainTarget = "F:\\sampOrg\\"
        self.targetPath = " "
        self.ready = False

    def tryA(self, img):
        res = "fail"
        try:
            info = i.getexif() 
            if info:
                for tag, value in info.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
                if "DateTimeOriginal" in ret:
                    res = ret["DateTimeOriginal"]
                if "DateTime" in ret:
                    res = ret["DateTime"]
        except:
            res = "fail"
        return res

    def tryB(self, img):
        res = "fail"
        try:
            info = getattr(i, "_getexif()", "error")
            if (info!="error"):
                for tag, value in info.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
                if "DateTimeOriginal" in ret:
                    res = ret["DateTimeOriginal"]
                if "DateTime" in ret:
                    res = ret["DateTime"]
        except:
            res = "fail"
        return res

    def tryC(self, img):
        res = "fail"
        try:
            info = getattr(i, "_getexif()", "error")
            if (info!="error"):
                for tag, value in info.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
                if "DateTimeOriginal" in ret:
                    res = ret["DateTimeOriginal"]
                if "DateTime" in ret:
                    res = ret["DateTime"]
        except:
            res = "fail"
        return res

    def tryD(self, sn):
        res = "fail"
        # 0326091425 : Mar 26 2009 2:25PM
        if ((len(sn)==10) or (len(sn)==11)) and is_int(sn[:10]):
            yr = sn[4:6]
            mo = sn[:2]
            res = "20"+yr+":"+mo
        return res

    def tryE(self, fn):
        res = "fail"
        stat = os.stat(fn)
        tstamp = getattr(stat, "st_mtime", "error")
        if (tstamp!="error"):
            dt = datetime.fromtimestamp(tstamp)
            res = dt.strftime("%Y:%m")
        return res

    def get_exif_date(self, fn, sn):
        ret = {}
        try: 
            i = Image.open(fn)
        except:
            dt = "1000:noExif"
            return dt
        dt = self.tryA(i)
        if (dt=="fail"):
            dt = self.tryB(i)
        if (dt=="fail"):
            dt = self.tryC(i)
        if (dt=="fail"):
            dt = self.tryD(sn)
        if (dt=="fail"):
            dt = self.tryE(fn)
        if (dt=="fail"):
            dt = "1000:noExif"
        return dt

    # load y,m,title from exif in file at path
    def scanner(self, pt, fn, type):
        self.sourcePath = pt;
        # print("source:", pt)
        # break off end of path to get name
        dt = "1000:01"
        dt = self.get_exif_date(pt, fn)
        sfx = ""
        if (type==1):           
            sfx = ".jpg"
        if (type==2):
            sfx = ".png"
        dateParts = dt.split(":")
        # break off yyyy:mm: from dt to get date vals
        self.year = dateParts[0]
        self.month = dateParts[1]
        if int(self.year)>2020 or int(self.year)<1990 or int(self.month)>12:
            self.year = "1001"
            self.month = "1"
        self.targetDir = self.mainTarget + self.year + "\\" + self.month
        self.targetPath = self.targetDir + "\\" + fn + sfx
        self.ready = True

    #def scanPng(self, fn):

    # save self at sink path 
    def saveSelf(self):
        if (not self.ready):
            return
        if (not (os.path.isdir(self.targetDir))):
            os.makedirs(self.targetDir)
        if (not (os.path.isfile(self.targetPath))):
            copyfile(self.sourcePath, self.targetPath)
        print("=>", self.targetPath)

print("defined")

picky = pic(); 

for root, dirs, files in os.walk("E:\\familyData\\2004"):
    for file in files:
        fullPath = os.path.join(root, file)
        filename, file_extension = os.path.splitext(file)
        print(fullPath)
        picky.ready = False
        #if (file_extension == ".png"):
        #    picky.scanPng(file)
        if (file_extension == ".jpg"):
            picky.scanner(fullPath, filename, 1)
        if (file_extension == ".JPG"):
            picky.scanner(fullPath, filename, 1)
        if (file_extension == ".png"):
            picky.scanner(fullPath, filename, 2)
        if (file_extension == ".PNG"):
            picky.scanner(fullPath, filename, 2)
        picky.saveSelf()
