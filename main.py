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

        # Case 1: Square Image
        if width == height: # 1:1 Ratio
            if desired_width > desired_height: # Desired Ratio: 16:9
                # space must be added to right and left
                pass
            elif desired_height > desired_width: # Desired Ratio: 9:16
                # space must be added to the top and bottom
                pass
            else: # Desired Ratio: 1:1
                # don't do anything
                pass

        # Case 2: Landscape Image
        elif width > height: # 16:9 Ratio
            if desired_ratio_scale > ratio_scale:
                # space must be added to the right and left
            elif desired_ratio_scale < ratio_scale:
                # space must be added to the top and bottom
            else:
                # don't do anything
                pass

        # Case 3: Portrait Image 
        else: # 9:16 Ratio
            if desired_ratio_scale > ratio_scale:
                # space must be added to the right and left
            elif desired_ratio_scale < ratio_scale:
                # space must be added to the top and bottom
            else:
                # don't do anything
                pass

