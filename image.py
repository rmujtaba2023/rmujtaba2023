import numpy as np
from PIL import Image

# create 3d number array of zeros, then replace zeros(black pixels) with values(color)
data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]
print(data)

# make a red patch
data[0:3:, 3:6] = [255, 200, 233]
data[0:3, 0:2] = [0, 200, 233]
data[3:5, 2:4] = [255, 23, 233]

img = Image.fromarray(data, "RGB")
img.save("canvass.png")
