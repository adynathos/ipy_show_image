
# Interactive Show Image

Display images in Jupyter web UI, that is JupyterLab and Jupyter Notebook.

Encodes the image directly into HTML (base64) without going through matplotlib. 

The compression format is customizable. A single function call can show multiple images in a grid.

* `show(img_1, img_2)` will draw each image on a separate row
* `show([img_1, img_2])` will draw both images in one row
* `show([img_1, img_2], [img_3, img_4])` will draw two rows of two images

Specifying the format:  
* `show(..., fmt='webp')`: image format, usually png jpeg webp
* `show.set_default_image_format('webp')`
* The default is `png`, please use `webp` or `jpeg` to reduce notebook file size

Whether to try converting unusual shapes and datatypes to the needed RGB:  
* `show(..., adapt=True or False)`

Convenience functions `imread`, `imwrite` are also provided (based on PIL). 

### Demo

Try the [demo notebook](demo.ipynb).

### Installation

* `pip install show-image`

or

* Include the file `show_image.py` in your project
* Ensure libraries are installed: `Pillow numpy matplotlib ipython`


