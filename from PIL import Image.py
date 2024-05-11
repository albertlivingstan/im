from PIL import Image
im = Image.open("Blue_And_Red_Futuristic_Game_YouTube_Channel_Art_640x360_2.png")
newim=im.resize((600,600)) 
newim.save("m.png")
newim.show()
im.close() 
newim.close()