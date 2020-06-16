from PIL import Image

im = Image.open('data/src/lena.jpg')

print(im.size)
print(type(im.size))
# (400, 225)
# <class 'tuple'>

w, h = im.size
print('width: ', w)
print('height:', h)
# width:  400
# height: 225
