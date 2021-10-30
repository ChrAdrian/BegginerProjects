# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script to resize, rotate bulk images and save them as .JPG


from PIL import Image
import os
import cv2


count = 0
folder = input("Please provide folder path: ")
rotation_angle = input("Please insert the rotation angle: ")
width = input("Please insert desired width: ")
height = input("Please insert desired height: ")
os.chdir(rf"{folder}")
if os.path.exists("Resized JPG") is False:
    os.mkdir("Resized JPG")
save_path = rf"{folder}\Resized JPG"
for image_name in os.listdir(folder):
    image = Image.open(image_name)
    processed_image = image.rotate(int(rotation_angle)).resize((int(width), int(height)))
    processed_image.format = image.format
    os.chdir(rf"{folder}\Resized JPG")
    processed_image.save(image_name + ".jpg")
    count += 1
    print(f"Resizing {image_name} in image format: {processed_image.format}, image size: {processed_image.size}")
    print(f"Total number of resized images: {count}.")
