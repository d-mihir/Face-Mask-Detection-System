import time
import cv2
import os
import datetime
import logging
date = datetime.datetime.now().strftime("%d_%m_%Y")
path_images = f"/home/pi/shared/Images/"
# if os.path.isdir(path_images)==True:
#     os.rmdir(path_images)
#     os.mkdir(path_images)
# else:
#     os.mkdir(path_images)

cap = cv2.VideoCapture(0)

while True:
    # if time condition
    if ((datetime.datetime.now().strftime("%H%M%S")=="100500") or (datetime.datetime.now().strftime("%H%M%S")=="140500") or (datetime.datetime.now().strftime("%H%M%S")=="173000") or (datetime.datetime.now().strftime("%H%M%S")=="165000")):
        os.system("python3 /home/pi/miniproject/zip.py")
    else:
	    try:
	        today_date = datetime.datetime.now().strftime("%m_%d_%H_%M_%S")
	        ret, frame1 = cap.read()
	        ret, frame2 = cap.read()
	        diff = cv2.absdiff(frame1, frame2)
	        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
	        blur = cv2.GaussianBlur(gray, (5, 5), 0)
	        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
	        dialated = cv2.dilate(thresh, None, iterations=3)
	        contours, _ = cv2.findContours(dialated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	#       cv2.drawContours(frame1, contours, -1, (150, 12, 255), 2)
	        for c in contours:
	            if cv2.contourArea(c) < 4000:
	                continue
	            x, y, w, h = cv2.boundingRect(c)
	            temp = frame1
	            cv2.imwrite(os.path.join(path_images, today_date+".jpg"), frame1)
	            #cv2.rectangle(temp, (x, y), (x+w, y+h), (0, 255, 0), 2)
	            st= st+1
	            # time.sleep(1)
	            # count+=1
	            # if (count >= 55):
	            #         tryupload()
	            #         count = 0
	        if cv2.waitKey(10)==ord('q'):
	            break
	    except:
	        pass

