import numpy as np
from skimage import data, io, filters
from PIL import Image
from PIL import ImageFilter
# openvision.py - description
__author__ = "Cameron Flannery, Hui Jiang"
__copyright__ = "Copyright 2017"
__credits__ = ["Cameron Flannery, Hui Jiang"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Alpha"


class lanedetect(object):
    """docstring for lanedetect."""
    def __init__(self, image):
        super(lanedetect, self).__init__()
        self.image = image
        self.create_PIL_Image()
        self.find_edges()

    def find_edges(self):
        self.im = self.im.filter(ImageFilter.FIND_EDGES)

    def show_image(self):
        self.im.show()

    def create_PIL_Image(self):
        self.im = Image.open(self.image).convert('LA')
