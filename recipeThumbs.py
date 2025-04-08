import csv
# import requests
import os
from shutil import copyfile
import xml.etree.ElementTree as ET 
import zipfile
import numpy as np
import cv2

# for resizing recipe cards: make each one 750*450 px.
# also save two copies: one b&w, one color


# for each file in directory
baseDirName = "C:\\Users\\mcdon\\Desktop\\scans\\b_rec\\"

src_files = os.listdir(baseDirName)
counter = 10
for fpath in src_files:
    print("file:", fpath)
    if os.path.isfile(fpath):
        # read it if you can
        srcImg = cv2.imread(fpath, cv2.IMREAD_COLOR)
        if srcImg is None:
            print("didnt load")
        else:
            # get size
            szy, szx, depth = srcImg.shape
            print("size ", szx, ",", szy)
            # resize src
            blurImg = cv2.blur(srcImg, (3,3))
            smImg = cv2.resize(blurImg, (int(szx/2), int(szy/2)))
            # split into RGB; use r for all three => grayscale!
            # bchan, gchan, rchan = cv2.split(smImg);
            # bwImg = cv2.merge((rchan,rchan,rchan))
            
            # make names
            newNm = baseDirName + str(counter) + ".jpg"
            cv2.imwrite(newNm, smImg, [int(cv2.IMWRITE_JPEG_QUALITY), 60])
            # newNm = baseDirName + str(counter) + "b.jpg"
            # cv2.imwrite(newNm, bwImg, [int(cv2.IMWRITE_JPEG_QUALITY), 60])
            counter = counter+1




#i = 10
#while (i<counter): 
#    n1 = str(i) + ".jpg"
#    n2 = str(i) + "t.jpg"
#    print("<div class=\"left\"><A HREF=\"",n1,"\"><img src=\"",n2,"\"></a></div>")
#    i = i+1
        