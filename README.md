# FPGA Tools

Handy Python tools for FPGA development by [Project F](https://projectf.io/). For our Verilog designs see [projf-explore](https://github.com/projf/projf-explore).

Licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## img2fmem

Image to FPGA memory map converter for Verilog $readmemh and Xilinx core generator COE.
Output can be in 2, 16, 64, or 256 colours with a 12 (RGB444), 15 (RGB555), or 24-bit (RGB888) palette. Monochrome (2 colour) output uses Floyd-Steinberg dithering.

Your source image needs to be in a format Pillow supports: PNG, JPEG, TIFF, BMP are amongst the formats supported.

For more details see the [img2fmem README](img2fmem/).

## sine2fmem

Generate a table of sine values between 0-90° (0 - π/2 radians) suitable for
loading into memory with Verilog $readmemh.

For more details see the [sine2fmem README](sine2fmem/).

## wf2fmem

Wavefront .obj (3D model) to FPGA memory init file converter for use with Verilog $readmemh.
Handles triangular and quad faces.

For more details see the [wf2fmem README](wf2fmem/).
