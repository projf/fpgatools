# FPGA Tools

Handy Python tools for FPGA development by [Project F](https://projectf.io/). For our Verilog designs see [projf-explore](https://github.com/projf/projf-explore).

Licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## img2fmem

Image to FPGA memory map converter for use with Verilog `$readmemh()` or Xilinx core generator COE.
Output hex image uses 16, 64, or 256 colours from a 12 or 24-bit palette.
Written in Python 3 using the [Pillow](https://pillow.readthedocs.io) package.

Your source image needs to be in a format Pillow supports: PNG, JPEG, TIFF, BMP are amongst the formats supported.

For full usage instructions see the [img2fmem README](img2fmem/).

## sine2fmem

Generate a table of sine values between 0-90° (0 - π/2 radians) suitable for
loading into memory with Verilog `$readmemh()`.

For usage instructions see the [sine2fmem README](sine2fmem/).

## wf2fmem

Wavefront .obj (3D model) to FPGA memory init file converter for use with Verilog `$readmemh()`.
Handles triangular and quad faces. Written in Python 3.

For usage instructions see the [wf2fmem README](wf2fmem/).
