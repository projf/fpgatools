# Wavefront Object to FPGA Memory File

Wavefront .obj to FPGA memory init file converter for use with Verilog `$readmemh()`.
Written in Python 3.

## Usage

```bash
wf2fmem.py model_file size offset
```

* model_file: source model file name
* size: size in pixels of output (minimum 16)
* offset: offset from screen edge in pixels of output

Example:

```bash
wf2fmem.py test/icosphere.obj 220 8
```

Converts the icosphere model file with a maximum pixel dimensions of 220 and an offset of 8 pixels from the edge of the screen.

For advice on working with Verilog .mem files, see [Initialize Memory in Verilog](https://projectf.io/posts/initialize-memory-in-verilog/).

## Test Data

* [cube](test/cube.obj) - a hand-crafted cube created by the author (6 faces and 8 vertices)
* [icosphere](test/icosphere.obj) - icosphere exported from [Blender](https://docs.blender.org/manual/en/latest/modeling/meshes/primitives.html)
* [monkey](test/monkey.obj) - Monkey exported from [Blender](https://docs.blender.org/manual/en/latest/modeling/meshes/primitives.html)
* [teapot](test/teapot.obj) - Utah Teapot from [University of Utah](https://www.cs.utah.edu/~natevm/newell_teaset/newell_teaset.zip)

## References

* [Wavefront .obj file](https://en.wikipedia.org/wiki/Wavefront_.obj_file) (Wikipedia)
