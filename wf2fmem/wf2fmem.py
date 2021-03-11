#!/usr/bin/env python3

# wf2fmem.py - Wavefront .obj to FPGA memory init converter
# By Will Green - https://projectf.io
# Copyright (c) 2021, Will Green, Licensed under BSD 3-Clause License
# For latest version and docs visit https://github.com/projf/fpgatools

# NB. This is an early version in development

import operator
import os
import sys

if (len(sys.argv) != 2):
    print("Convert Wavefront .obj files to FPGA memory init files in $readmemh format.")
    print("usage: wf2fmem.py model_file")
    print("         model_file: source model file name")
    print("\nExample: wf2fmem.py teapot.obj")
    sys.exit()

input_file = sys.argv[1]
base_name = os.path.splitext(input_file)[0]

# print("input_file: {}".format(input_file))
# print("base_name:  {}".format(base_name))

SC = 220  # scale factor for model vertices
# SC = 55  # scale factor for model vertices
X_OFFS = 0.0  # horizontal offset
# X_OFFS = 2.0  # horizontal offset
Y_OFFS = 0.0  # vertical offset

verts = []
faces = []

def gen_lines(face):
    x_coords = []
    y_coords = []
    for f in face:
        x_coords.append(verts[f-1][0])
        y_coords.append(verts[f-1][1])

    x_coords = [int(SC*(c+X_OFFS)) for c in x_coords]
    y_coords = [int(SC*(c+Y_OFFS)) for c in y_coords]

    hc = []
    for x,y in zip(x_coords, y_coords):
        hc.append("{:02X}{:02X}".format(x,y))
        # hc.append("{:03}{:03}".format(x,y))

    print("{}{}".format(hc[0],hc[1]))
    print("{}{}".format(hc[1],hc[2]))
    if len(face) == 4:  # quad
        print("{}{}".format(hc[2],hc[3]))
        print("{}{}".format(hc[3],hc[0]))
    else:  # triangle
        print("{}{}".format(hc[2],hc[0]))

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

print("There are {} vertices.".format(len(verts)))
print("There are {} faces.".format(len(faces)))

for f in faces:
    gen_lines(f)

# # Used to determine scale if we don't know it
# max_x = max(verts, key=operator.itemgetter(0))
# max_y = max(verts, key=operator.itemgetter(1))
# min_x = min(verts, key=operator.itemgetter(0))
# min_y = min(verts, key=operator.itemgetter(1))
# print("Max x={}, y={} ".format(max_x[0], max_y[1]))
# print("Min x={}, y={} ".format(min_x[0], min_y[1]))
