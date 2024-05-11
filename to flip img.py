from PIL import Image
myImage = Image.open("im/Blue_And_Red_Futuristic_Game_YouTube_Channel_Art_640x360_2.png")
flippedImage = myImage.transpose(Image.FLIP_LEFT_RIGHT) 
flippedImage.save('flip.png')
myImage.show()
flippedImage.show()