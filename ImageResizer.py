# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script to resize a image


from PIL import Image
import os
import PIL
import glob


folder_path = input("Please provide folder path: ")
os.chdir(folder_path)
images = [file for file in os.listdir() if file.endswith(('jpeg', 'png', 'jpg'))]
for image in images:
    img = Image.open(image)
    img.resize((2500,1600))
    img.save("resized_"+image, optimize=True, quality=40)