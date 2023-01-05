from tokenize import Token
import requests
import os
import utils



"""
twice
/my_id @botusername
/my_id @botusername

https://api.telegram.org/bot{API TOKEN}/getUpdates

chatid  = 	-614486677

"""

chatid  = 	-614486677
TOKEN_KEY = "5513359344:AAEfZmRj1aTXVeqtiTM8UrUoHCTC1tbhPM0"

def send_image(file_name):
    path = os.path.join('tmp',file_name)
    print(path)
    fil = {'photo':open(path,'rb')}
    images = utils.unknown_image_list(main_path="tmp")
    if len(images) > 0:
        resp = requests.post("https://api.telegram.org/bot{0}/sendPhoto?chat_id={1}".format(TOKEN_KEY,chatid),files=fil)
    return resp.status_code


# chatid  = 	-614486677
# TOKEN_KEY = "5513359344:AAEfZmRj1aTXVeqtiTM8UrUoHCTC1tbhPM0"
# imagepath = "/Users/aiyaz-15199/Downloads/Door_opener/tmp/Unknown_Face_1.png"
# fil = {'photo':open(imagepath,'rb')}
# print(fil)
# url = "https://api.telegram.org/bot{0}/sendPhoto?chat_id={1}".format(TOKEN_KEY,chatid)

# requests.post(url,files=fil)