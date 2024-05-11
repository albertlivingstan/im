from PIL import Image
myImage = Image.open("Blue_And_Red_Futuristic_Game_YouTube_Channel_Art_640x360_2.png")
print("The image format is :",myImage.format) 
print("The image mode is :",myImage.mode)
print("The image size is",myImage.size) 
myImage.close()