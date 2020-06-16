#save ndarray as image file
pil_img = Image.fromarray(im)
pil_img.save('data/temp/lena_square_save.png')

# You can write it in one line.
Image.fromarray(im).save('data/temp/lena_square_save.png')

#If dtype of ndarray float convert it to uint8
#to save it as JPG or PNG.
pil_img_f = Image.fromarray(im_f.astype(np.uint8))
pil_img_f.save('data/temp/lena_square_save.png')
