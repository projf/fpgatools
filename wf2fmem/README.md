# wf2fmem

Wavefront .obj to FPGA memory init file converter for use with Verilog `$readmemh()`.
Handles triangular and quad faces. Written in Python 3.

Example projects using this tool:

* [Project F Shapes & Simple 3D](https://projectf.io/posts/shapes-3d/)

Licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

## Usage

```bash
wf2fmem.py model_file size offset
```

* `model_file`: source model file name
* `size`: maximum size in pixels for output (minimum 16)
* `offset`: offset from screen edge in pixels for output

Example:

```bash
wf2fmem.py test/icosphere.obj 220 8
```

Converts the icosphere model file with a maximum pixel dimensions of 220 and an offset of 8 pixels from the edge of the screen.

For advice on working with Verilog .mem files, see [Initialize Memory in Verilog](https://projectf.io/posts/initialize-memory-in-verilog/).

## Test Data

* [cube](test/cube.obj) - a hand-crafted cube created by the author (8 vertices and 6 faces)
* [icosphere](test/icosphere.obj) - icosphere exported from [Blender](https://docs.blender.org/manual/en/latest/modeling/meshes/primitives.html) (42 vertices and 80 faces)
* [monkey](test/monkey.obj) - Monkey exported from [Blender](https://docs.blender.org/manual/en/latest/modeling/meshes/primitives.html) (507 vertices and 500 faces)
* [teapot](test/teapot.obj) - Utah Teapot from [University of Utah](https://www.cs.utah.edu/~natevm/newell_teaset/newell_teaset.zip) (3241 vertices and 3464 faces)

## References

* [Wavefront .obj file](https://en.wikipedia.org/wiki/Wavefront_.obj_file) (Wikipedia)
