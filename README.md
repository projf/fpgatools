# FPGA Tools
Assorted tools for FPGA development. Visit [timetoexplore.net](http://timetoexplore.net) to learn more.
They're all licensed under the BSD 3-Clause License. See the LICENSE file for details.

## img2fmem
Image to FPGA memory map converter for use with Verilog `$readmemh()` or Xilinx core generator COE.
Output hex image uses 16, 64, or 256 colours from a palette of 4096.
Written in Python using the [Pillow](https://pillow.readthedocs.io) package. Compatible with Python 3 and 2.

_NB. Support for Xilinx COE format is currently experimental. Testing is ongoing during February 2018._

### Usage
* To install Pillow: `pip install Pillow`
* To use run: `python img2fmem.py image_file colour_bits output_format`

* Input Arguments
	- `image_file`: source image file name
	- `colour_bits`: number of colour bits per pixel: 4, 6, or 8
	- `output_format`: `mem` or `coe`
* Output is three files (in same directory as source image):
	- 4, 6, or 8-bit image in hex text format
	- 12-bit palette in hex text format
	- PNG preview of converted image, so you can see what it will look like

### Examples:
For an image called `acme.png` that you want converted to 4-bit colour for use with Verilog `$readmemh()`:

	python img2fmem.py acme.png 4 mem

For an image called `acme.tiff` that you want converted to 8-bit colour for use with Xilinx core generator:

	python img2fmem.py acme.tiff 6 coe

### Notes
* Source image is in [any format Pillow supports](http://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html): PNG, JPEG, TIFF, BMP etc.
* Source images must be RGB rather than RGBA format. If you use RGBA then you'll probably end up with a screen of one solid colour. The file(1) command will tell you if you're using RGB or RGBA.
* If the value of `colour_bits` isn't valid it defaults to `8`
* img2fmem does not resize images: use your image editor to do this
* The `game.png` graphic comes from [KenneyNL](https://opengameart.org/content/space-shooter-redux) and is public domain.

Learn how to [initialize memory arrays in Verilog](https://timetoexplore.net/blog/initialize-memory-in-verilog).

### Troubleshooting

#### ImportError: No module named 'PIL'
You need to install Pillow. Run the following:

	pip install Pillow

Or check out the [Pillow documentation](https://pillow.readthedocs.io) for detailed install instructions.
