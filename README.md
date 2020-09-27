
# Jupyter Show Image

Display images in jupyter web UI
* `show(img_1, img_2)` will draw each image on a separate row
* `show([img_1, img_2])` will draw both images in one row
* `show([img_1, img_2], [img_3, img_4])` will draw two rows of two images

Specifying the format:  
* `show(..., fmt='webp')`: image format, usually png jpeg webp

Whether to try converting unusual shapes and datatypes to the needed RGB:  
* `show(..., adapt=True or False)`

Convenience functions `imread`, `imwrite` are also provided (based on PIL). 

### Demo

Try the [demo notebook](demo.ipynb).

### Installation

* Copy the file `jupyter_show_image.py`
* Ensure libraries are installed: `Pillow numpy matplotlib ipython`


