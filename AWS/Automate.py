import os
import datetime
import time
import sqlite3
import boto3
from botocore.exceptions import ClientError

#DETAILS RELATED TO AWS S3
# I HAVE REMOVED THE KEYS, BUCKET NAME
access_key = ''
access_secret = ''
bucket_name = ''


#CONNECT TO AWS S3 BUCKET
client_s3 = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=access_secret

)
time.sleep(5)
# CHANGE THESE PATHS IF NECESSAY
python_interpreter_path = "/home/ubuntu/project_env/bin/python3"
base_path = "/home/ubuntu/last/"


#DOWNLOADING THE FILES FROM S3, CALLING THE copy_files_from_s3.py
os.system(f"{python_interpreter_path} {base_path}copy_files_from_s3.py")


#UNZIPPING THE FILE DOWNLOADED FROM S3
os.system(f"{python_interpreter_path} {base_path}unzip.py")




# Required Paths
#path_to_captured_images = f"{base_path}captured_images/"
path_to_captured_images = f"{base_path}captured_images/home/pi/shared/Images/"
path_to_without_mask_images = f"{base_path}without_mask/"
mask_detection_prog = f"{base_path}detection.py"
automate_prog = f"{base_path}Automate.py"
face_recognition_prog = f"{base_path}FaceDetection_2.py"
db_path = f"{base_path}Faces.db"
sending_mails_prog = f"{base_path}Sendingmails/sendingemail.py"



# START
try:
    print("[INFO]: Hello Admin!")
    print("[INFO]: Today is {}".format(datetime.datetime.now().strftime("%D %H:%M:%S")))
    print("[INFO]: The path to the captured images is set as {}!".format(path_to_captured_images),end="")
    print("[INFO]: The total number of images captured today are {}.".format(len(os.listdir(path_to_captured_images))))
except Exception as e:
    print(e)
# DETECTING THE PRESENCE OF MASK CALLING detection.py
os.system(f"{python_interpreter_path} {mask_detection_prog}")
try:

    print("[INFO]: Face Mask Detection Completed!")
    print("[INFO]: The total number of images where mask was not found is {}.".format(len(os.listdir(path_to_without_mask_images))))
except Exception as e:
    print(e)
# FACE RECOGNITION CALLING FaceDetection_2.py
os.system(f"{python_interpreter_path} {face_recognition_prog} {path_to_without_mask_images}")
print("[INFO]: Face Recognition Completed!")

#SENDING MAILS TO PEOPLE NOT WEARING  A MASK
print("Sending mails")
os.system(f"{python_interpreter_path} {sending_mails_prog}")

#UPLOADING DATABASE(Faces.db) FILE TO S3
print("Uploading Faces.db to s3")
try:
        client_s3.upload_file(
                                '/home/ubuntu/last/Faces.db',
                                bucket_name,
                                'Faces.db'
                        )
except ClientError as e:
        print("Error with credentials")
except Exception as e:
        print(e)


# REFRESHING DB
sqlite_connection = sqlite3.connect(f"{db_path}")
db = sqlite_connection.cursor()
db.execute('DELETE FROM face_table;')
#CLOSING DB
sqlite_connection.commit()
db.close()
sqlite_connection.close()

#DELETING THE FILES PRESENT IN CAPTURED_IMAGES FOLDER
print("Deleting the files present in captured_images")
os.system("rm -rf /home/ubuntu/last/captured_images/home/")


# SHUTTING DOWN THE EC2 INSTANCE IN 4 MINUTES
print("Shutting down the AMAZON AWS EC2 instance in 4 miutes!!")
print("Time: {}".format(datetime.datetime.now().strftime("%H:%M:%S")))
time.sleep(300)
os.system("sudo poweroff")
