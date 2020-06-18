from PIL import Image
import numpy as np


im = np.array(Image.open('sachin.png'))
print(im.shape)
