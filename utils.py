import os
import face_recognition
import pickle
import numpy as np

def files_name(foldername):
    value = os.listdir(foldername)
    return value

def remove_hidden_files(list):
    tmp = []
    for x in list:
        if str(x).endswith(".pkl"):
            tmp.append(x)
    return tmp

def generate_user_names(listvalue):
    tmp = []
    for images in listvalue:
        if not images.endswith(".jpg"):
            continue
        data = str(images).split(".")[0]
        if '_' in data or '-' in data:
            if '-' in data:
                data = data.replace("-"," ")
            if '_' in data:
                data = data.replace("_"," ")
        data = data.capitalize()
        tmp.append(data)
    return tmp


def generate_face_encoding(main_path,listvalue):
    tmp = []
    for image in listvalue:
        if not image.endswith(".jpg"):
            continue
        path = os.path.join(main_path,image)
        image_data = face_recognition.load_image_file(path)
        image_face_encoding = face_recognition.face_encodings(image_data)[0]
        tmp.append(image_face_encoding)
    return tmp
    
def get_pkl_value(main_path):
    tmp = []
    path = os.path.join(main_path,"pkl")
    files = os.listdir(path=path)
    for file in files:
        if file.endswith(".pkl"):
            tmp.append(file)
    return len(tmp)


def unknown_face_encoding(main_path):
    tmp = ""
    path = os.path.join(main_path,"pkl")
    value = remove_hidden_files(os.listdir(path=path))
    print(value)
    print("pkl file count :",len(value))
    if len(value) != 0:
        with open(path+"/info.pkl","rb") as f:
            tmp = pickle.load(f)

    return tmp

def array_recreation(corrupted_array):
    value = corrupted_array 
    value = str(value).replace("[array(","")
    value = str(value).replace(")]","")
    value = value.split(",")
    print(value)
    # return np.array(value)

def unknown_image_count(main_path):
    tmp = []
    path = os.path.join(main_path)
    files = os.listdir(path)
    for file in files:
        if file.endswith(".png"):
            tmp.append(file)
    return len(tmp)

def unknown_image_list(main_path):
    tmp = []
    path = os.path.join(main_path)
    files = os.listdir(path)
    for file in files:
        if file.endswith(".png"):
            tmp.append(file)
    return tmp