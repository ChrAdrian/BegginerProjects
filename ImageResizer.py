# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script to resize, rotate bulk images and save them as .JPG


from PIL import Image
import os
import cv2


global save_path, rotation_angle, count, width, height


def define_inputs():
    global save_path, rotation_angle, count, width, height
    count = 0
    folder = input("Please provide folder path: ")
    rotation_angle = input("Please insert the rotation angle: ")
    width = input("Please insert desired width: ")
    height = input("Please insert desired height: ")
    os.chdir(rf"{folder}")
    # Create folder to stock processed photos
    if os.path.exists("Processed JPG") is False:
        os.mkdir("Processed JPG")
    save_path = rf"{folder}\Processed JPG"
    return folder

def resize_image(folder):
    global save_path, rotation_angle, count, width, height
    # Iterate over all images in folder
    for image_name in os.listdir(folder):
        if os.path.isfile(image_name):
            # Open image
            image = Image.open(image_name)
            # Process image
            processed_image = image.rotate(int(rotation_angle)).resize((int(width), int(height)))
            processed_image.format = image.format
            # Select save photo directory
            os.chdir(save_path)
            processed_image.save(image_name + ".jpg")
            # revert to the initial directory
            os.chdir(rf"{folder}")
            count += 1
            print(f"Resizing {image_name} in image format: {processed_image.format}, "
                  f"image size: {processed_image.size}")
    print(f"Total number of resized images: {count}.")