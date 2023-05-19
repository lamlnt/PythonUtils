import os, sys
from PIL import Image
import glob

files = glob.glob(sys.argv[1] + '/*.png', recursive=True)
for infile in files:
    with Image.open(infile).convert('RGBA') as im:
        originalsize = im.size
        a = (4 - im.size[0] % 4) 
        if a == 4:
            a = 0
        b = (4 - im.size[1] % 4)
        if b == 4:
            b = 0
        x = im.size[0] + a
        y = im.size[1] + b
        newimg = Image.new("RGB", (x,y))
        newimg.putalpha(0)
        newimg.paste(im)
        newimg.save(infile)
        if (a != 0 and b != 0):
            print(infile)