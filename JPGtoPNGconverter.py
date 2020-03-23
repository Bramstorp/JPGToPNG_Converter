import sys
import os
from PIL import Image

# this will grav the first argument that is the folderpath of the one u want to be converted
FolderPath = sys.argv[1]

# this will grav the second argument that is the new folderpath it will save all pics 2
NewFolder = sys.argv[2]

# this will check if the new folder exist and if it dosnt make one
if not os.FolderPath.exists(NewFolder):
    os.makedirs(NewFolder)

# this will take each file in the the selected folder
for filename in os.listdir(FolderPath):
    # here we open the folder and just asign all files in the folder to img variable so we can save it later on 
    img = Image.open(f'{FolderPath}{filename}')
    # clean_name will take the pics in the folder and split them to a tuple so we can take only the name of the file and not the .jpg
    clean_name = os.FolderPath.splitext(filename)[0]
    #here we save all the splittet files and same them intro the new folder
    img.save(f'{NewFolder}/{clean_name}.png', 'png')
    print('All the files has been updated to .png')


"""
sys.argv[0] = name of the scipt
sys.argv[1] = selected folder
sys.argv[2] = new mkdir folder
"""
