import os
import zipfile
import datetime


print("[INFO]: Hello Admin!")
print("[INFO]: Today is {}".format(datetime.datetime.now().strftime("%D %H:%M:%S")))

date = datetime.datetime.now().strftime("%d%m%Y")
#print("Entered zip.py")
# path where the zip file is to be stored
path = "/home/pi/miniproject/to_be_uploaded/"
print("Starting the process of Zipping files")
images_path = "/home/pi/shared/Images"
if (len(os.listdir(images_path)) != 0):
    zf = zipfile.ZipFile("{}{}.zip".format(path,date),"w")
    # Path to the directory where captured images are stored
#os.system("cd /home/pi/shared/Images")
    images_path = "/home/pi/shared/Images/"
    for dirname,subdirs,files in os.walk(images_path):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname,filename))
    zf.close()
# the zipping process is completed
# calling the upload python script
# print("Called aws_upload.py)
    os.system("python3 /home/pi/miniproject/aws_upload.py")
#os.system("cd /")
else:
    print("Folder is Empty!!")

os.system("sudo rm -rf /home/pi/shared/Images")
os.system("sudo mkdir /home/pi/shared/Images")
