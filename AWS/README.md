# AWS Instance

The scripts are executed in this order

1) ```Automate.py``` (this is given in the crontab of the instance)
2) ```copy_files_from_s3.py``` (it downloads the files from the s3 bucket)
3) ```unzip.py``` (it unzips the zip file downloaded from the s3 bucket)
4) ```detection.py``` (it performs face mask detection)
5) ```FaceDetection_2.py``` (it performs face recognition)
6) ```sendingemail.py``` (it is concerned with sending mails, it is present inside the folder ```Sendingmails```)


Note:
1. The paths have to be changed accordingly.
2. There is no need for executing the scripts individually.
