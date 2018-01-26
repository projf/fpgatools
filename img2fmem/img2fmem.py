#!/usr/bin/env python

# img2fmem.py - image to FPGA memory map converter
# By Will Green - https://timetoexplore.net
# Copyright (c) 2018, Will Green, Licensed under BSD 3-Clause License
# For latest version and docs visit https://github.com/WillGreen/fpgatools

import os
import sys
from PIL import Image

COLOURS = 64  # use 64 for 6-bit palette

if len(sys.argv) < 2:
    print("Usage: image_file")
    sys.exit()

# load source image
input_file = sys.argv[1]
source_img = Image.open(input_file)
prev_img = source_img.copy()  # take a copy for later preview process

base_name = os.path.splitext(input_file)[0]
(width, height) = source_img.size

# Reduce to 12-bit precision (4-bit per colour) in range 0-15
pixels = source_img.load()
for x in range(width):
    for y in range(height):
        pixels[x, y] = tuple([p / 16 for p in pixels[x, y]])

# Convert to limited colour palette
dest_img = source_img.convert('P', palette=Image.ADAPTIVE, colors=COLOURS)

# Generate hex image output
image_data = dest_img.getdata()
with open(base_name + '.mem', 'w') as f:
    f.write("// Generated by img2fmem.py - ")
    f.write("https://github.com/WillGreen/fpgatools\n")
    for d in image_data:
        f.write(hex(d)[2:])
        f.write("\n")


def chunk(seq, size):  # Extract palette
    return [seq[i:i+size] for i in range(0, len(seq), size)]
colours = [map(ord, bytes) for bytes in chunk(dest_img.palette.palette, 3)]

# Generate hex palette output
with open(base_name + '_palette.mem', 'w') as f:
    f.write("// Generated by img2fmem.py - ")
    f.write("https://github.com/WillGreen/fpgatools\n")
    for i in range(COLOURS):
        r = colours[i][0]
        g = colours[i][1]
        b = colours[i][2]
        f.write(hex(r*256 + g*16 + b)[2:])
        f.write("\n")

# Convert preview image and save
# 4-bit precision but we retain 0-255 range so image not too dark
prev_pixels = prev_img.load()
for x in range(width):
    for y in range(height):
        prev_pixels[x, y] = tuple([(p / 16) * 16 for p in prev_pixels[x, y]])
prev_img = prev_img.convert('P', palette=Image.ADAPTIVE, colors=COLOURS)
prev_img.save(base_name + '_preview.png')