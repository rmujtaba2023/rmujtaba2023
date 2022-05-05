import numpy as np
from PIL import Image


class Canvas:
    """
    Object where all the shapes will be printed
    """

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # create a 3d nump array of zeros and then add values for color
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, imagepath):
        # convert array to image file
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
