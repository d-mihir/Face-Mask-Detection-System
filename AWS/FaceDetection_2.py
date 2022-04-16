import os, shutil
import sqlite3
import pickle
import face_recognition
from datetime import datetime
import numpy as np
import sys


# ALL REQUIRED PATHS
db_path = "/home/ubuntu/last/Faces.db"
pickle_file = "/home/ubuntu/last/Encodings1.pickle"

wm = '/home/ubuntu/last/without_mask/'

sqlite_connection = sqlite3.connect(db_path)
db = sqlite_connection.cursor()
# creates a table in the database if not present
db.execute("CREATE TABLE IF NOT EXISTS face_table (Date_ NUMERIC,Roll NUMERIC, Image BLOB);")
if len(sys.argv)!=2:
    print("Usage: python3 FaceDetection.py path_to_the_image_directory")
    exit(0)
db.execute('DELETE FROM face_table;')

with open(f"{pickle_file}",'rb') as file:
    knownEncodings = pickle.load(file)
pathh = str(sys.argv[1])

knownFaceNames = list(knownEncodings.keys())
knownEncodings = np.array(list(knownEncodings.values()))
for eachImage in os.listdir(sys.argv[1]):
    unknownImage = face_recognition.load_image_file(sys.argv[1]+eachImage)
    unknownFace = face_recognition.face_encodings(unknownImage)
    # converting the image to byte form
    with open(sys.argv[1]+eachImage, "rb") as file:
        data = file.read()

    try:
        # Lower tolerance means more accuracy
        result = face_recognition.compare_faces(knownEncodings,unknownFace,tolerance=0.5)
        # iterating over the results
        face_distance = face_recognition.face_distance(knownEncodings,unknownFace)
        face_distance = face_distance.tolist()
        
        # if we get more than two true statements
        if result.count(True)>1:
            temp = sorted(face_distance)
            smallestFaceDistance = temp[0]
            db.execute("INSERT INTO face_table (Date_,Roll,Image) VALUES(?,?,?)",(datetime.now().strftime("%D"), knownFaceNames[face_distance.index(smallestFaceDistance)], data))
            os.remove(sys.argv[1]+eachImage)

        else:
            for flag,name in zip(result,knownFaceNames):
                if flag==True:
                    print(f'Face found and recognized {name}')
                    db.execute("INSERT INTO face_table (Date_,Roll,Image) VALUES(?,?,?)",(datetime.now().strftime("%D"),name,data))
                    os.remove(sys.argv[1]+eachImage)
                else:
                    print(' ') # Face found but could not recognize it
    except:
        print("Error could not find face")
        continue
sqlite_connection.commit()
db.close()
sqlite_connection.close()

os.system("rm -rf /home/ubuntu/last/captured_images")
os.system("mkdir /home/ubuntu/last/captured_images")
