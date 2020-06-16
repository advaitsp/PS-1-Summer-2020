from PIL import Image
import numpy as np

im = np.array(Image.open('data/src/lena_square.png'))

print(im.dtype)
# uint8

print(im.ndim)
# 3

print(im.shape)
# (512, 512, 3)
