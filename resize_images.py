from PIL import Image
from pathlib import Path
import os

def size_in_MB(file):
    return os.path.getsize(file)/1048576

def optimize_img(file):

    # Converting file
    print("Converting: {}".format(file))
    
    # iterate process until the file size is lower than 2MB    
    im = Image.open(file)    
    im_size = size_in_MB(file)
    quality = 90    
    
    while im_size > 2:
        # optimize image
        im.save(file, "JPEG", optimize = True, quality = quality)            
        im_size = size_in_MB(file)
        quality -= 10
            
        
# main

input_dir = Path("/mnt/c/Users/Asus/Desktop/cerinza/pics_2")

files = [file for file in input_dir.rglob('*.[jpg JPG]*')]

for file in files:

    # if file exceds the limit (2MB), optimize it
    if size_in_MB(file) > 2:
        optimize_img(file)
        
print("Done!")