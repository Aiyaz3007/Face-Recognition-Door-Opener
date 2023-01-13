import cv2
import face_recognition
import os
import utils
import pickle
import numpy as np
from send_image import send_image

red = (255,0,0)
green = (0,255,0)
color = red
name = "unknown"
font = cv2.FONT_HERSHEY_SIMPLEX
known_faces_foldername = "known_faces"
tmp_dir = "tmp"


image_files = utils.files_name(foldername=known_faces_foldername)

encoding = utils.generate_face_encoding(main_path=known_faces_foldername,listvalue=image_files)

known_face_encodings = encoding

unknown_face_encodings = utils.unknown_face_encoding(main_path=tmp_dir)

known_face_names = utils.generate_user_names(listvalue=image_files)


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret,frame = cap.read()
    print("Camera Status:",ret)
    if not ret:
        continue
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)


    rgb_small_frame = cv2.flip(small_frame,1)


    face_locations = face_recognition.face_locations(small_frame)
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)
    face_names = []

    for (top,right,bottom,left) in (face_locations):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), color, thickness=4)
        cv2.rectangle(frame, (left, bottom), (right, bottom+30), color, thickness=4)
        cv2.putText(frame,text=name,org=(left+10,bottom+22),fontFace=font,color=(255,255,255),thickness=2,fontScale=0.9)
        


    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
        if True in matches:
            color = green
            index_of_true = matches.index(True)
            name = known_face_names[index_of_true]
        else:
            color = red
            # cropped_face = frame[top:bottom,left:right]
            cropped_face = frame


            # Unknown user without pickle file
            if int(utils.get_pkl_value(main_path=tmp_dir)) == 0:
                num = int(utils.unknown_image_count(tmp_dir)+1)
                tmp_path = os.path.join(tmp_dir,"pkl/info.pkl")
                with open(tmp_path,"wb") as f:
                    myvar = [face_encoding]
                    pickle.dump(myvar,f)
                cv2.imwrite(tmp_dir+"/Unknown_Face_{}.png".format((utils.unknown_image_count(tmp_dir)+1)),cropped_face)
                print(send_image("Unknown_Face_{}.png".format(num)))

                
            # Unknown user with pickle file
            else:
                # read pkl file 
                tmp_path = os.path.join(tmp_dir,"pkl/info.pkl")
                with open(tmp_path,"rb") as f:
                    myvar = pickle.load(f)

                
                with open(tmp_path,mode="wb") as f: 
                    num = int(utils.unknown_image_count(tmp_dir)+1)  
                    unknown_match = face_recognition.compare_faces(myvar,face_encoding)
                    False_index = [i for i, x in enumerate(unknown_match) if x == False]
                    print(unknown_match)
                    # if new unknown found  
                    if not (True in unknown_match):
                        myvar.append(face_encoding)
                        cv2.imwrite(tmp_dir+"/Unknown_Face_{}.png".format((utils.unknown_image_count(tmp_dir)+1)),cropped_face)
                        print(send_image("Unknown_Face_{}.png".format(num)))
                        

                    pickle.dump(myvar,f)


                        


    cv2.imshow("FRAME",frame)
    k = cv2.waitKey(1)
    if k == 27:
        break