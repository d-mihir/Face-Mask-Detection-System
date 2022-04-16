# copy the zip file to another folder for reference

import os
import datetime
path_to_zip = "/home/pi/miniproject/to_be_uploaded"
os.system("cp {}/{}.zip {}/{}.zip".format(path_to_zip,datetime.datetime.now().strftime("%d%m%Y"),"/home/pi/miniproject/copies",datetime.datetime.now().strftime("%d%m%Y")))
print("Copied to the file to a new folder for safety and reference")

