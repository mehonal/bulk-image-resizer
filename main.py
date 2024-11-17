import os
from PIL import Image

class SETTINGS:
	MB = 1_048_576 # in bytes

print('''
	This is a script to mass resize images.
    Example Settings are as follows:

    New Aspect Ratio: 16:9
    Fill Color: #ffffff
	------------------------------------------------------------
	''')

new_aspect_ratio = input('Enter minimum size of images to compress in MB: ')
fill_color = input('Enter compression percentage (0-100): ')
desired_width = int(new_aspect_ratio.split(":")[0])
desired_height = int(new_aspect_ratio.split(":")[1])
desired_ratio_scale = desired_width / desired_height # higher width = higher ratio

for file in os.listdir():
    if file.upper().endswith('JPG') or file.upper().endswith('PNG'):
        image = Image.open(file)
        width, height = image.size
        ratio_scale = width / height

        # image conversion logic goes here

