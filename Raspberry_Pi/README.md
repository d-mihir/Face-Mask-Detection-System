# The order that is followed in the Raspberry Pi

1) ```motionfinal_2.py``` (this is placed in the crontab)
2) ```zip.py``` (it zips the images!!)
3) ```aws_upload.py``` (it uploads the files into the s3 bucket)
4) ```copying_zip.py``` (it copies the files into a separate folder for safe keeping)

Note:
1. The paths have to be changed accordingly.
2. There is no need for executing the scripts individually.