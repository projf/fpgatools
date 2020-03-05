# FPGA Tools

Tools for FPGA development. Licensed under the BSD 3-Clause License. See the LICENSE file for details.

## img2fmem

Image to FPGA memory map converter for use with Verilog `$readmemh()` or Xilinx core generator COE.
Output hex image uses 16, 64, or 256 colours from a 12 or 24-bit palette.
Written in Python using the [Pillow](https://pillow.readthedocs.io) package.

_NB. Xilinx COE format has undergone limited testing._

### Changes in 2020 Version

* Adds support for 24-bit palettes (16.7 million colours), but retains a default of 12-bit palettes (4,096 colours).
* Drops Python 2 support - it might still work, but the author no longer develops with Python 2
* Hex values in output are now in upper case

### Install Pillow

Install Pillow using **one** of the following methods:

* Debian/Ubuntu: `apt install python-pil`
* Use `pip` or `pip3` to install package `pillow`
* Or follow [Pillow Installation](https://pillow.readthedocs.io/en/stable/installation.html)

### Usage

* To use run: `img2fmem.py image_file colour_bits output_format palette_bits`
* Input Arguments
  * `image_file`: source image file name (see below for supported formats)
  * `colour_bits`: number of colour bits per pixel: 4, 6, or 8
  * `output_format`: `mem` or `coe`
  * `palette_bits`: number of palette bits: 12 (default) or 24
* Output is three files (in same directory as source image):
  * 4, 6, or 8-bit image in hex text format
  * 12 or 24 bit palette in hex text format
  * PNG preview of converted image, so you can see what it will look like

### Examples

For an image called `acme.png` that you want converted to 4-bit colour with 12-bit palette for use with Verilog `$readmemh()`:

    python img2fmem.py acme.png 4 mem 12

For an image called `acme.tiff` that you want converted to 8-bit colour with 24-bit palette for use with Xilinx core generator:

    python img2fmem.py acme.tiff 6 coe 24

### Supported Image Formats

* Your source image needs to be in a [format Pillow supports](http://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html): PNG, JPEG, TIFF, BMP are amongst the formats supported.
* Source images must be RGB rather than RGBA format. If you use RGBA then you'll probably end up with a screen of one solid colour. The `file(1)` command will tell you if you're using RGB or RGBA.
* Images with transparency (such as PNGs) may fail with a message about not being iterable. Save your image without transparency and all should be well.

The [ImagePalette interface isn't well documented](https://pillow.readthedocs.io/en/stable/reference/ImagePalette.html). This script was written by looking at the Pillow source code, so isn't guaranteed to work with newer versions, but then again the palette code doesn't seem to have changed since 2001.

### Usage Notes

* If the value of `colour_bits` isn't valid it defaults to `8`
* If the value of `palette_bits` isn't valid it defaults to `12`
* img2fmem does not resize images: use your image editor to do this
* The `game.png` graphic comes from [KenneyNL](https://opengameart.org/content/space-shooter-redux) and is in the public domain; other included images were created by the author.

Learn how to [initialize memory arrays in Verilog](https://timetoexplore.net/blog/initialize-memory-in-verilog).

### Troubleshooting

If you're having issues:

* Check you're using a supported image format without transparency (see above)
* Check the script is working correctly using using one of the included test images (e.g. photo.png)
* Make sure you're using Python 3

#### ImportError: No module named 'PIL'

You haven't installed the Python 'Pillow' package (see Install Pillow, above).
