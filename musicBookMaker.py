import csv
import requests
import os
from shutil import copyfile
import xml.etree.ElementTree as ET 
import zipfile
import numpy as np
import cv2

from fpdf import FPDF


# use all the images in baseDir/inputs


baseDirName = os.getcwd()
inDirName = baseDirName + "/comboBook"
outFileName = baseDirName + "/nealTabs.pdf"
tempDirName = baseDirName + "/temps"
pdf = FPDF()
        
maxHt = 720
maxWd = 800

src_files = os.listdir(inDirName)
src_files.sort()
counter = 0; 
for fpath in src_files:
    fullPathIn = inDirName + "/" + fpath
    fullPathTemp = tempDirName + "/" + fpath
    if (counter<200):
        print("img: ", fullPathIn)
        if os.path.isfile(fullPathIn):

            # if it's a .jpg, JPG, PNG, or png
            srcImg = cv2.imread(fullPathIn, cv2.IMREAD_COLOR)
            if srcImg is None:
                print("didnt load")
            else:
                # get size
                szy, szx, depth = srcImg.shape                
                pszx = maxWd
                pszy = int(maxWd*szy/szx)
                print("size ", szx, ",", szy, "   resize to ", pszx, ",", pszy)

                hiCont = cv2.convertScaleAbs(srcImg, alpha=1.05, beta=0.0)
                blurmag = int(szx/pszx)
                if (blurmag>1):
                    blurSz = -1 + (2 * blurmag) 
                    # print("blur mag:", blurmag, " sz:", blurSz)
                    blurImg = cv2.blur(hiCont, (blurSz, blurSz))
                    smImg = cv2.resize(blurImg, (pszx, pszy))
                else: 
                    smImg = cv2.resize(hiCont, (pszx, pszy))
                # make names & save
                cv2.imwrite(fullPathTemp, smImg)
    counter = counter + 1

counter = 0; 
for fpath in src_files:
    fullPathTemp = tempDirName + "/" + fpath
    if (counter<200):
        srcImg = cv2.imread(fullPathTemp, cv2.IMREAD_COLOR)
        szy, szx, depth = srcImg.shape
        width = 136
        rtX = 64
        scaleFac = 1.0;
        
        scaleFac = 1500.0 / szy
        width = 136.0 * scaleFac
        rtX = 80.0 - (45.0*scaleFac) 
        if (szy<1020):
            width = 180
            rtX = 30
        
        print("img ", fpath, szy, width, rtX)
        pdf.add_page('P', 'Letter')
        if (counter%2==0):
            pdf.image(fullPathTemp, rtX,10.0, w=width)
        else:
            pdf.image(fullPathTemp, 10.0,10.0, w=width)
        counter = counter + 1

pdf.output(outFileName, 'F')

