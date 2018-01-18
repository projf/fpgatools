# FPGA Tools
Assorted tools for FPGA development. Visit [timetoexplore.net](http://timetoexplore.net) to learn more.
They're all licensed under the BSD 3-Clause License. See the LICENSE file for details.

## img2fmem.py
Image to FPGA memory map converter for use with **Verilog** $readmemh() etc.
Uses Python Pillow to convert images to suitable format for FPGA use.

* Input is image in [any format Pillow supports](http://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html): PNG, JPEG, TIFF, BMP etc.
* Output is three files:
  - 6-bit image in hex text format
  - 12-bit palette in hex text format
  - PNG preview of converted image
* img2fmem does not resize images: use your image editor to do this
* [Pillow Docs](https://pillow.readthedocs.io)
  - To install Pillow: `pip install Pillow`

Learn how to [initialize memory arrays in Verilog](https://timetoexplore.net/blog/initialize-memory-in-verilog).
