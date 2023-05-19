import os, sys
from PIL import Image
import glob

files = glob.glob(sys.argv[1] + '/*.png', recursive=True)
for infile in files:
    with Image.open(infile).convert('RGBA') as im:
        newimg = im.reduce(2)
        newimg.save(infile)
        print(infile)