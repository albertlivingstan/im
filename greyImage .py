from PIL import Image
myImage = Image.open('im/Blue_And_Red_Futuristic_Game_YouTube_Channel_Art_640x360_2.png') 
greyImage = myImage.convert('L') #to save - greyImage.save('location') 
greyImage.show()