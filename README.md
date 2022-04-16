# Face Mask Detection System

My friends and I made a project on face mask detection that alerts people if they are found not wearing a mask.

### Below is the work flow of the project.
- Raspberry Pi captures the images on detection of some motion.
- At a particular time of the day the captured images are sent to an AWS S3 Bucket in zip format.
- After the uploading has been completed, the AWS EC2 instance boots up and performs the process of mask detection on the images present in the S3 bucket.
- If mask is not detected on a persons face, face recognition is performed on that person. 
- This image is sent to the mail address of the recognized person as an attachment.



### Prerequisites
1. A high definition web camera is required for capturing the images.
2. Raspberry Pi 4, for more details please visit their official site.
3. An AWS account, free tier will be sufficient for this project.
4. The **Windows**  operating system downloading the ``` Visual Studio Build Tools ``` are required, since we need ``` cmake ``` for the process of face recognition. A **Linux** operating system does not require these.
For more information regarding the installation on the **Windows** operating system refer to this [video](https://youtu.be/xaDJ5xnc8dc). 
5. Python 3.8 and above.
6. AWS CLI must be installed on the raspberry pi, for more information regarding the installation please go through this [page](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
7. It is better to create a virtual environment.

### Contents
1. Raspberry Pi
    1. It contains the code that has to be present in the raspberry pi for capturing the images and uploading them to the AWS. Refer to the readme present in the Raspberry_Pi folder.
2. AWS
	1. It contains the code that has to be present in the AWS instance for downloading the files and performing the processes of face mask detection, face recognition and sending mails. Refer to the readme present in the AWS folder.


## This is the flow chart of the project
![Flow_Chart](https://github.com/d-mihir/Face-Recognition/blob/main/Flowchart%20(1).png)
