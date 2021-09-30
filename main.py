import PIL
from PIL import Image
import numpy as np

raw_img = Image.open('pic.jpg').convert('L')
img = list(np.asarray(Image.open('pic.jpg').convert('L').resize((800, 150))))

key = ['-', '+', 'I', 'T', 'H', 'N', 'E', 'M', '#', 'X', '%', '&', '$']

txt_pic = ''

for x in range(len(img)):
    for y in range(len(img[x])):
        txt_pic += key[12 - int(img[x][y] / 255 * 13)]
    txt_pic += '\n'

with open('pic.txt', 'w+') as f:
    f.write(txt_pic)

















