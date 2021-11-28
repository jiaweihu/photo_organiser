import os
from photo_info import Photo_Info
import shutil

ext = ('.jpg', '.jpeg', '.JPG')

'''
This function iterate all the photo files in the folder and subfolder
Re-name the photos usind address + datatime
And put them into the folder corresponding to the year the photo is made
'''
def organiseFiles(directory):
    for root, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            organiseFiles(subdirectory)
        for file in files:
            if file.endswith(ext):                
                photoFile = os.path.join(root, file)
                print(photoFile)
                photo_info = Photo_Info(photoFile)
                dateTimeStr = photo_info.getPhotoTime()
                address = photo_info.getPhotoAddress()
                extendedFolder = destFolder + "\\" + dateTimeStr[0:4]
                if not os.path.exists(extendedFolder):
                    os.makedirs(extendedFolder)
                newName = address + dateTimeStr + ".jpg"
                targetFile = os.path.join(extendedFolder, newName)
                action = "copy " + photoFile + " " + targetFile
                print(action)
                shutil.copyfile(photoFile, targetFile)


sourceDirectory = r'E:\Jiawei\Dropbox\Photos'

destFolder = "c:\\temp\\result"
if not os.path.exists(destFolder):
    os.makedirs(destFolder)

organiseFiles(sourceDirectory)