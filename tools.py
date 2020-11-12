import PIL.Image
import numpy as np
from PIL import ImageFile
import cv2


def load_image_file(file, size=(-1, -1), mode='RGB'):
    """
    Loads an image file (.jpg, .png, etc) into a numpy array

    :param file: image file name or file object to load
    :param mode: format to convert the image to. Only 'RGB' (8-bit RGB, 3 channels) and 'L' (black and white) are supported.
    :return: image contents as numpy array
    """
    im = PIL.Image.open(file)
    (x, y) = im.size
    if size[0] != -1 and size[1] != -1:
        ratio = y / x
        new_x = size[0]
        new_y = int(size[0] * ratio)
        im = im.resize((new_x, new_y))
    if mode:
        im = im.convert(mode)
    return np.array(im)