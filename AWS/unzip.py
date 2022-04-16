import os
import datetime
# unzips the zip file created
print("Unzipping the file downloaded from AWS S3")
print("Path to the zip file is /home/ubuntu/last/FROMS3")
date = datetime.datetime.now().strftime("%d%m%Y")
print("Unzipping the file")
try:
    os.system("unzip /home/ubuntu/last/FROMS3/{}.zip -d /home/ubuntu/last/captured_images/".format(date))
    print("Saved the files to /home/ubuntu/last/captured_images/")
except Exception as e:
    print("could not zip the file")
    print("Shutting down the ec2 instance in 5 minutes")
    time.sleep(300)
    os.system("sudo poweroff")


# deleting the zip file now
try:
    os.system("rm /home/ubuntu/last/FROMS3/{}.zip".format(date))
    print("Deleted the file from /home/ubuntu/last/FROMS3/{}.zip".format(date))
except Exception as e:
    print("Could not remove the zip file")
    print("Shutting down the ec2 instance in 5 minutes")
    time.sleep(300)
    os.system("sudo poweroff")


