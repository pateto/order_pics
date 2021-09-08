import os
import piexif
import datetime
import shutil
from pathlib import Path
from collections import Counter
from PIL import Image
import pdb

dir = 'C:\\Users\\cace_al\\Desktop\\img\\pics'
output_dir = 'E:\\pics'


def count_extensions():

    files = []

    for path in Path(dir).rglob('*'):
        name, ext = os.path.splitext(path)
        files.append(ext)

    print(Counter(files))


def copy_move_files(move=False):    

    img_extensions = [".jpg", ".JPG", ".jpeg", ".JPEG",  ".png", ".PNG",
                      ".gif", ".GIF", ".bmp", ".MOV", ".mp4", ".MP4"]

    for path in Path(dir).rglob('*'):
        name, ext = os.path.splitext(path)
        if ext in img_extensions:

            try:  # Get date taken
                pic_date = piexif.load(str(path))[
                    'Exif'][36867].decode('ascii')
                #day = pic_date[8:10]
                month = '{:02d}'.format(int(pic_date[5:7]))
                year = pic_date[0:4]
            except:  # Get modified date
                pic_date = datetime.datetime.fromtimestamp(
                    os.path.getmtime(path))
                #day = '{:02d}'.format(pic_date.day)
                month = '{:02d}'.format(pic_date.month)
                year = str(pic_date.year)

            # Create folder directory (if doesnt exist)
            new_dir = os.path.join(output_dir, year, month)
            if not os.path.exists(new_dir):
                print("Creating directory", new_dir)
                os.makedirs(new_dir)

            # copy files
            new_path = os.path.join(new_dir, path.name)
            if not os.path.isfile(new_path):
                if(move):
                    print("moving", path, "-->", new_path)
                    shutil.move(path, new_path)

                else:
                    print("copying", path, "-->", new_path)
                    shutil.copyfile(path, new_path)


count_extensions()
copy_move_files(move=True)

print("Done!")
