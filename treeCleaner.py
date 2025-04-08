import csv
import os
import shutil 


# for each dir B with a .txt file in it, 
#   rm dirs named "old" and "B-h" "B-page-images" "ogg" "m4b" "mp3" "spx"
#   rm files *.zip *.html

def cleanBook(dirPath):
    print("book:" + dirPath) 
    listing = os.listdir(dirPath)
    for aName in listing:
        print("     " + aName)
        aPath = dirPath + "\\" + aName 
        if (os.path.isdir(aPath)):
            shutil.rmtree(aPath, ignore_errors=True)
        else: 
            if (os.path.isfile(aPath)):
                filename, file_extension = os.path.splitext(aName)
                if (file_extension!=".txt"):
                    if (os.path.exists(aPath)):
                        os.remove(aPath)
            

# a book is a dir contains a .txt file
def isBook(path):
    listing = os.listdir(path)
    for aName in listing:
        aPath = path + "\\" + aName 
        txtPlace = aPath.find(".txt");
        if (txtPlace>0):
            print("found "+aPath+" in "+path)
            return True
    return False


# if we're in a book, clean it. OW clean subdirs
def recurseDir(path):
    listing = os.listdir(path)
    for aName in listing:
        aPath = path + "\\" + aName 
        if (os.path.isdir(aPath)):
            print("dir:" + aPath) 
            if (isBook(aPath)):
                cleanBook(aPath)
            else:
                recurseDir(aPath)


baseDirName = os.getcwd() 
recurseDir(baseDirName)


               