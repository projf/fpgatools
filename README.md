# FPGA Tools
Assorted tools for FPGA development. Visit [timetoexplore.net](http://timetoexplore.net) to learn more.
They're all licensed under the BSD 3-Clause License. See the LICENSE file for details.

## img2fmem
Image to FPGA memory map converter for use with **Verilog** `$readmemh()` etc.
Output hex image uses up to 64 colours from a palette of 4096.
Written in Python using the [Pillow](https://pillow.readthedocs.io) package. Compatible with Python 3 and 2.

### Usage
* To install Pillow: `pip install Pillow`
* To use run: `python img2fmem.py <image_file>`

### Notes
* Input is image in [any format Pillow supports](http://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html): PNG, JPEG, TIFF, BMP etc.
* Output is three files (in same directory as source image):
  - 6-bit image in hex text format
  - 12-bit palette in hex text format
  - PNG preview of converted image
* img2fmem does not resize images: use your image editor to do this

Learn how to [initialize memory arrays in Verilog](https://timetoexplore.net/blog/initialize-memory-in-verilog).
