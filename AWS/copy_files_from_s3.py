import os
import time
import datetime
# copying or downloading files from s3 to ec2

date = datetime.datetime.now().strftime("%d%m%Y")
print("Downloading files from s3 ")
try:
    os.system(f"aws s3 cp s3://bucket_name/{date}.zip /home/ubuntu/last/FROMS3")
except:
    print("There is a error in downloading file!\n File not downloaded")
    print("Shutting down the aws instance in 5 minutes")
    time.sleep(300)


print("Finished downloading the file from S3")
try:
    print("Deleting the zip file FROM S3 BUCKET")
except:
    print("There is error in deleting the file\n file not deleted")
finally:
    print("Exiting the copy_files_from_s3.py")

