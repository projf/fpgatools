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

verts = []
faces = [] 

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
    if len(f) == 3:  # triangle
        print("triangle: ", end='')
        print("{}->{} ".format(f[0], f[1]), end='')
        print("{}->{} ".format(f[1], f[2]), end='')
        print("{}->{}".format(f[2], f[0]))
        (x0,y0) = verts[f[0]-1][0:2]
        (x1,y1) = verts[f[1]-1][0:2]
        (x2,y2) = verts[f[2]-1][0:2]
        print("({},{})".format(x0,y0))
        print("({},{})".format(x1,y1))
        print("({},{})".format(x2,y2))
    if len(f) == 4:  # quad
        print("quad: ", end='')
        print("{}->{} ".format(f[0], f[1]), end='')
        print("{}->{} ".format(f[1], f[2]), end='')
        print("{}->{} ".format(f[2], f[3]), end='')
        print("{}->{}".format(f[3], f[0]))
        (x0,y0) = verts[f[0]-1][0:2]
        (x1,y1) = verts[f[1]-1][0:2]
        (x2,y2) = verts[f[2]-1][0:2]
        (x3,y3) = verts[f[3]-1][0:2]
        print("({},{})".format(x0,y0))
        print("({},{})".format(x1,y1))
        print("({},{})".format(x2,y2))
        print("({},{})".format(x3,y3))

# max_x = max(verts, key=operator.itemgetter(0))
# max_y = max(verts, key=operator.itemgetter(1))
# min_x = min(verts, key=operator.itemgetter(0))
# min_y = min(verts, key=operator.itemgetter(1))
# print("Max x={}, y={} ".format(max_x[0], max_y[1]))
# print("Min x={}, y={} ".format(min_x[0], min_y[1]))
