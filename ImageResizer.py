# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script to resize bulk images and save them as .JPG


from PIL import Image
import os

folder = input("Please provide folder path: ")
os.chdir(rf"{folder}")
for image_name in os.listdir(folder):
    image = Image.open(image_name)
    image.thumbnail((3000, 2000))
    image.save(f"{image_name}_resized.jpg")
    print(f"Image format: {image.format}, image size: {image.size}")
