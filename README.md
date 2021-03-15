# FPGA Tools

Tools for FPGA development by [Project F](https://projectf.io/).

Licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## img2fmem

Image to FPGA memory map converter for use with Verilog `$readmemh()` or Xilinx core generator COE.
Output hex image uses 16, 64, or 256 colours from a 12 or 24-bit palette.
Written in Python 3 using the [Pillow](https://pillow.readthedocs.io) package.

More details, including usage instructions, in the [img2fmem README](img2fmem/).

## wf2fmem

Wavefront .obj to FPGA memory init file converter for use with Verilog `$readmemh()`.
Handles triangular and quad faces. Written in Python 3.

More details, including usage instructions, in the [wf2fmem README](wf2fmem/).
