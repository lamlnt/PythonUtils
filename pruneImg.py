import os, sys
import glob
from os import path
from pathlib import Path

files = glob.glob(sys.argv[1] + '/*.png', recursive=True)
for infile in files:
    if (Path(infile).stem.startswith(sys.argv[2]) == False):
        newName = sys.argv[2] + Path(infile).stem
        newPath = sys.argv[1] + '/' +newName+ '.png'
        if (path.exists(newPath)):
            print("already existed: " + newName)
            os.remove(infile)