#!/usr/bin/env python
import os
import sys
import inspect
import cv2
from PIL import Image
from numpy import matrix
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split
                                 (inspect.getfile(inspect.currentframe()))[0],
                                 "common")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
from lanedetection import *
# openvision.py - description
__author__ = "Cameron Flannery, Hui Jiang"
__copyright__ = "Copyright 2017"
__credits__ = ["Cameron Flannery, Hui Jiang"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Alpha"


class vision(object):
    """docstring for vision."""
    def __init__(self, image):
        super(vision, self).__init__()
        self.image = image
        self.find_lanes()

    def find_lanes(self):
        lanes = lanedetect(self.image)
        lanes.show_image()


def main():
    prototyping_image = os.path.join(os.getcwd(), 'resources', 'frontfacing01.jpeg')
    auto_view = vision(prototyping_image)


if __name__ == "__main__":
    try:
        os.system('cls')
        main()
    except KeyboardInterrupt:
        "KeyboardInterrupt: exiting..."
else:
    "openvision.py must be run as the main script"
