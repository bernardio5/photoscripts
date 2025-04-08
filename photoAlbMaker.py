import csv
# import requests
import os
from shutil import copyfile
import xml.etree.ElementTree as ET 
import zipfile
import numpy as np
import cv2


# traverse all directories in this dir
# start root index.html
# for each dirName, 
#   write a line in index.html
#   make fam/dirName
#   for each pic in dirname
#      resize to sanity
#      make thumbnail
#      save to fam/dirName/#.jpg 
#   make fam/dirName/index.html
#   
baseDirName = os.getcwd()
inDirName = baseDirName + "\\inputs"
outDirName = baseDirName + "\\outputs"
os.makedirs(outDirName)
indName = outDirName + "index.html"
        
for root, dirs, files in os.walk(inDirName):
    for dirName in dirs:
        currentDir = inDirName + "\\" + dirName
        targetPath = outDirName + "\\" + dirName
        os.makedirs(targetPath)
        counter = 100
        src_files = os.listdir(currentDir)
        print("  out: ", targetPath, " files found: ", len(src_files))
        #src_files.sort(key=lambda x: os.path.getctime(x))
        for fpath in src_files:
            fullPath = currentDir + "\\" + fpath
            print("fullp: ", fullPath)
            if os.path.isfile(fullPath):
                # if it's a .jpg, JPG, PNG, or png
                srcImg = cv2.imread(fullPath, cv2.IMREAD_COLOR)
                if srcImg is None:
                    print("didnt load")
                else:
                    # get size
                    szy, szx, depth = srcImg.shape
                    # print("size ", szx, ",", szy)
                    # uniform scale to fit in 1920x1080

                    # fit to width
                    pszx = 1920
                    pszy = int(1920*szy/szx)
                    pstx = 0
                    psty = int((1080-pszy) / 2)
                    # still too tall? tall image! fit to height
                    if (pszy>1080):
                        pszx = int(1080*szx/szy)
                        pszy = 1080
                        pstx = int((1920-pszx) / 2)
                        psty = 0 
                    # print("resize ", pszx, ",", pszy, "-- paste at", pstx, ",", psty)
                    # make a black background
                    pImg = np.ones((1080, 1920, 3), np.uint8)
                    pImg[:, :] = (128,128,128)
                    # resize src
                    blurmag = int(szx/pszx)
                    if (blurmag>1):
                        blurSz = -1 + (2 * blurmag) 
                        # print("blur mag:", blurmag, " sz:", blurSz)
                        blurImg = cv2.blur(srcImg, (blurSz, blurSz))
                        smImg = cv2.resize(blurImg, (pszx, pszy))
                    else: 
                        smImg = cv2.resize(srcImg, (pszx, pszy))
                    # paste smImg into pImg
                    pImg[psty:psty+pszy, pstx:pstx+pszx] = smImg
                    # make names & save
                    newNm = targetPath + "\\" + str(counter) + ".jpg"
                    cv2.imwrite(newNm, pImg, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

                    # make the thumb
                    # copy out a middle chunk of pImg
                    midImg = np.ones((540, 540, 3), np.uint8)
                    midImg = pImg[270:810, 690:1230]
                    blurCpImg = cv2.blur(midImg, (5,5))
                    thumbImg = cv2.resize(blurCpImg, (128,128))
                    newNm = targetPath + "\\" + str(counter) + "t.jpg"
                    cv2.imwrite(newNm, thumbImg, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
                    counter = counter+1

        indName = outDirName + "\\" + dirName + "\\index.html"
        with open(indName, "w") as f:
            print("<!DOCTYPE html ><head><title>workly.com/fam</title>", file=f)
            print("<link rel=\"stylesheet\" href=\"../styles.css\"></head>", file=f)
            print("<body><div class=\"container\"><div class=\"header\">", file=f)
            i = 100
            while (i<counter): 
                n1 = str(i) + ".jpg"
                n2 = str(i) + "t.jpg"
                print("<div class=\"left\"><A HREF=\"",n1,"\"><img src=\"",n2,"\"></a></div>", file=f)
                i = i+1
            print("</div></body></html>", file=f)
      



indName = outDirName + "index.html"
with open(indName, "w") as f:
    print("<!DOCTYPE html ><head><title>workly.com/fam</title>", file=f)
    print("<link rel=\"stylesheet\" href=\"styles.css\"></head>", file=f)
    print("<body><div class=\"container\"><div class=\"header\">", file=f)
    for root, dirs, files in os.walk(inDirName):
        for dirName in dirs:
            linkNm = dirName + "/index.html"
            iconName = dirName + "/110t.jpg"
            print("<div class=\"left\"><A HREF=\"",linkNm,"\"><img src=\"",iconName,"\"></a></div>", file=f)
    print("</div></body></html>", file=f)
      