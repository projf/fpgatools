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

## these parameters should be calculated automatically

# cube
SC = 220  # scale factor for model vertices
D_OFFS = 10   # draw offset (pixels to add to all dimensions)
X_OFFS = 0.0  # X offset
Y_OFFS = 0.0  # Y offset
Z_OFFS = 0.0  # Z offset

# # teapot
# SC = 32  # scale factor for model vertices
# D_OFFS = 10   # draw offset (pixels to add to all dimensions)
# X_OFFS = 2.0  # X offset
# Y_OFFS = 0.0  # Y offset
# Z_OFFS = 3.434  # Z offset

# # monkey
# SC = 88  # scale factor for model vertices
# D_OFFS = 10   # draw offset (pixels to add to all dimensions)
# X_OFFS = 1.367188  # X offset
# Y_OFFS = 0.984375  # Y offset
# Z_OFFS = 0.851562  # Z offset

verts = []
faces = []

def fmt_line(c0, c1):
    if (c1 > c0):
        return "{}{}".format(c0,c1)
    else:
        return "{}{}".format(c1,c0)

def gen_lines(face):
    x_coords = []
    y_coords = []
    z_coords = []
    for f in face:
        x_coords.append(verts[f-1][0])
        y_coords.append(verts[f-1][1])
        z_coords.append(verts[f-1][2])

    x_coords = [int(SC*(c+X_OFFS)) + D_OFFS for c in x_coords]
    y_coords = [int(SC*(c+Y_OFFS)) + D_OFFS for c in y_coords]
    z_coords = [int(SC*(c+Z_OFFS)) + D_OFFS for c in z_coords]

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

for f in faces:
    gen_lines(f)

# print("There are {} vertices.".format(len(verts)))
# print("There are {} faces.".format(len(faces)))

# # Used to determine scale if we don't know it
# max_x = max(verts, key=operator.itemgetter(0))
# max_y = max(verts, key=operator.itemgetter(1))
# max_z = max(verts, key=operator.itemgetter(2))
# min_x = min(verts, key=operator.itemgetter(0))
# min_y = min(verts, key=operator.itemgetter(1))
# min_z = min(verts, key=operator.itemgetter(2))
# print("Max x={}, y={}, z={} ".format(max_x[0], max_y[1], max_z[2]))
# print("Min x={}, y={}, z={} ".format(min_x[0], min_y[1], min_z[2]))
