#!/usr/bin/env python3
import os
import sys
from PIL import Image

(height, width) = tuple(map(int, os.popen('stty size', 'r').read().split()))

for infile in sys.argv[1:]:
    try:
        im = Image.open(infile).resize((width, height), Image.NEAREST).quantize(colors=256, kmeans=999)
        pixels = list(im.getdata())
        width, height = im.size
        string = ""
        for i in range(len(pixels)):
            string += "\033[48;5;%dm\255\033[0;37;0m" % pixels[i]
            if (i + 1) % width == 0:
                string += "\n"
        print(string)

    except IOError:
        print("ugh")
        exit(1)

