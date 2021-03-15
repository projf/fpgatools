#!/usr/bin/env python3

# wf2fmem.py - Wavefront .obj to FPGA memory init converter
# By Will Green - https://projectf.io
# (C)2021 Will Green, open source software released under the MIT License
# For latest version and docs visit https://github.com/projf/fpgatools

import operator
import os
import sys

if (len(sys.argv) != 4):
    print("Convert Wavefront .obj files to FPGA memory init files in $readmemh format.")
    print("usage: wf2fmem.py model_file size offset")
    print("         model_file: source model file name")
    print("         size:       size in pixels (16-255)")
    print("         offset:     offset from screen edge in pixels")
    print("                     size+offset must 255 or less")
    print("\nExample: wf2fmem.py icosphere.obj 220 8")
    sys.exit()

input_file = sys.argv[1]
base_name = os.path.splitext(input_file)[0]

size = int(sys.argv[2])
offs = int(sys.argv[3])
if (size < 16 or size > 255):
    print("Size must be 16-255 pixels")
    sys.exit()
if (size+offs > 255):
    print("size + offset must 255 or less")
    sys.exit()

# We'll generate an output file in a later version (instead of using stdout)
# print("input_file: {}".format(input_file))
# print("base_name:  {}".format(base_name))

# list of vertices and faces
verts = []
faces = []

# format lines in the same direction
def fmt_line(c0, c1):
    if (c1 > c0):
        return "{}{}".format(c0,c1)
    else:
        return "{}{}".format(c1,c0)

# generate lines from faces
def gen_lines(face, sf, min_x, min_y, min_z):
    x_coords = []
    y_coords = []
    z_coords = []
    for f in face:
        x_coords.append(verts[f-1][0])
        y_coords.append(verts[f-1][1])
        z_coords.append(verts[f-1][2])

    x_coords = [int(sf*(cx-min_x)) + offs for cx in x_coords]
    y_coords = [int(sf*(cy-min_y)) + offs for cy in y_coords]
    z_coords = [int(sf*(cz-min_z)) + offs for cz in z_coords]

    hc = []  # hex coordinates
    for x,y,z in zip(x_coords, y_coords, z_coords):
        hc.append("{:02X}{:02X}{:02X}".format(x,y,z))

    # output coordinates for each line of the face
    print(fmt_line(hc[0],hc[1]))
    print(fmt_line(hc[1],hc[2]))
    if len(face) == 4:  # quad
        print(fmt_line(hc[2],hc[3]))
        print(fmt_line(hc[3],hc[0]))
    else:  # triangle
        print(fmt_line(hc[2],hc[0]))

# read OBJ file; add vertices and faces to lists
with open(input_file, 'r') as obj_f:
    for line in obj_f:
        tok = line.split()
        if (tok):
            if (tok[0] == 'v'):
                coords = []
                for c in tok[1:]:
                    coords.append(float(c))
                verts.append(coords)
            elif (tok[0] == 'f'):
                fv = []
                for v in tok[1:]:
                    fv.append(int(v.partition('/')[0]))
                faces.append(fv)

# print("There are {} vertices.".format(len(verts)))
# print("There are {} faces.".format(len(faces)))

# determine scale factor and offsets
min_x = min(verts, key=operator.itemgetter(0))
min_y = min(verts, key=operator.itemgetter(1))
min_z = min(verts, key=operator.itemgetter(2))
max_x = max(verts, key=operator.itemgetter(0))
max_y = max(verts, key=operator.itemgetter(1))
max_z = max(verts, key=operator.itemgetter(2))
max_c = max([max_x[0]-min_x[0], max_y[1]-min_y[1], max_z[2]-min_z[2]])
sf = size / max_c

# print("Min x={}, y={}, z={} ".format(min_x[0], min_y[1], min_z[2]))
# print("Max x={}, y={}, z={} ".format(max_x[0], max_y[1], max_z[2]))
# print("Max c={}".format(max_c))
# print("Scale Factor: {}".format(sf))

for f in faces:
    gen_lines(f, sf, min_x[0], min_y[1], min_z[2])
