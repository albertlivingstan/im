# Importing Image and ImageFilter module from PIL package 
from PIL import Image, ImageFilter
im1 = Image.open("im/Blue_And_Red_Futuristic_Game_YouTube_Channel_Art_640x360_2.png")
# applying the blur filter
im2 = im1.filter(ImageFilter.BLUR) 
im3 = im2.filter(ImageFilter.EDGE_ENHANCE)
im4 = im3.filter(ImageFilter.EDGE_ENHANCE_MORE)
im1.show()
im2.show()
im3.show()
im4.show()