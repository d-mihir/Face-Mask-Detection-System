import os
import boto3
from botocore.exceptions import ClientError

# I HAVE REMOVED THE ACCESS KEY AND THE ACCESS SECRET
access_key = ''
access_secret = ''
bucket_name = ''

print("Uploading files")

#connect  amazon client instance

client_s3 = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=access_secret

)

'''
Upload files to s3 Bucket
'''
# path to the zip file that has been created
data_file_folder  = "/home/pi/miniproject/to_be_uploaded"
#data_file_folder = captured_images_path
for file in os.listdir(data_file_folder):
        if not file.startswith('~'):
                try:
                        print("Uploading file {0}...".format(file))
                        client_s3.upload_file(
                                os.path.join(data_file_folder,file),
                                bucket_name,
                                file
                        )

		# handling exceptions
                except ClientError as e:
                        print('Credential is incorrect')
                        print(e)
                except Exception as e:
                        print(e)


print("Completed")
# copied the file to another folder for reference
os.system("python3 /home/pi/miniproject/copying_zip.py")

# deleting the zip file that has been uploaded
os.system("sudo rm -rf /home/pi/miniproject/to_be_uploaded")
os.system("sudo mkdir /home/pi/miniproject/to_be_uploaded")
print("Deleted the zip file, the number of files present in the folder is {}".format(len(os.listdir(data_file_folder))))
print("returned from upload.py")
