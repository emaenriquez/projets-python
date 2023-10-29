
from PIL import Image

Image.open('mirror_img.jpg') # imagen original

img = Image.open('mirror_img.jpg') # clcoding.com
Mirror_Image = img.transpose(Image.FLIP_LEFT_RIGHT)
Mirror_Image.save(r'mirro.png')

Image.open('mirro.png')
