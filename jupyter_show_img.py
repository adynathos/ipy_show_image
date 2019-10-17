
import numpy as np
import PIL.Image
from matplotlib import cm
from IPython.display import display, display_png, display_jpeg, Image as ipy_Image

def adapt_img_data(img_data, cmap_pos=cm.get_cmap('magma'), cmap_div=cm.get_cmap('Spectral').reversed(), ret_compr=False):
	num_dims = img_data.shape.__len__()
	c = 'jpg'

	if num_dims == 3:
		if img_data.shape[2] > 3:
			img_data = img_data[:, :, :3]

		if img_data.dtype != np.uint8 and np.max(img_data) < 1.1:
			img_data = (img_data * 255).astype(np.uint8)


	elif num_dims == 2:
		if img_data.dtype == np.bool:

			img_data = img_data.astype(np.uint8)*255
			c = 'png'

		else:
			vmax = np.max(img_data)
			if img_data.dtype == np.uint8 and vmax == 1:
				img_data = img_data * 255

			else:
				vmin = np.min(img_data)

				if vmin >= 0:
					img_data = (img_data - vmin) * (1 / (vmax - vmin))
					img_data = cmap_pos(img_data, bytes=True)[:, :, :3]

				else:
					vrange = max(-vmin, vmax)
					img_data = img_data / (2 * vrange) + 0.5
					img_data = cmap_div(img_data, bytes=True)[:, :, :3]

	if ret_compr:
		return img_data, c
	else:
		return img_data 

DISPLAY_FUNCS = {
	'jpg': display_jpeg,
	'png': display_png,
}

def show(image, compression='png'):
	image = adapt_img_data(image, ret_compr=False)
	DISPLAY_FUNCS[compression](PIL.Image.fromarray(image))
