import os
import shutil
import numpy as np

# Path to your dataset
dataset_path = '/Users/datarist/labelImg/FULL [Heineken Vietnam] Developer Resources'
# Path where the folders will be created
output_path = '/Users/datarist/labelImg/Split'

# Create directories for the split if they don't exist
for i in range(1, 5):
    os.makedirs(os.path.join(output_path, f'Folder{i}'), exist_ok=True)

# List all images
all_images = [img for img in os.listdir(dataset_path) if img.endswith('.jpg') or img.endswith('.png')]

# Shuffle the list randomly if you want random distribution
np.random.shuffle(all_images)

# Split images into 4 roughly equal parts
split_1 = all_images[:250]
split_2 = all_images[250:500]
split_3 = all_images[500:750]
split_4 = all_images[750:]

# Function to copy images to respective folder
def distribute_images(images, folder_name):
    for image in images:
        shutil.copy(os.path.join(dataset_path, image), os.path.join(output_path, folder_name))

# Distribute images
distribute_images(split_1, 'Folder1')
distribute_images(split_2, 'Folder2')
distribute_images(split_3, 'Folder3')
distribute_images(split_4, 'Folder4')
