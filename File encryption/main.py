import random
import string
from time import sleep


chars = list(string.punctuation + " " + string.ascii_letters + string.digits)
key = chars.copy()


def encryption(chars,key,file):
    random.shuffle(key)
    sk = key
    enrypted_data = ""
    contetn = ""

    with open(file,"r") as reader:
        content = reader.read()

    with open("decryption.key","w") as dkey:
        for i in sk:
            dkey.write(i)

    for char in content:
        index = chars.index(char)
        enrypted_data += key[index]

    with open("data.encrypted","w") as enc:
        enc.write(enrypted_data)
        print("Encryption Sucessfull !")
             


def decryption(chars,key,file):
    decrypted_data = ""
    encrypted_data = ""
    contetn = ""


    with open(file,'r') as file:
        encrypted_data = file.read()

    with open(key,"r") as reader:
        content = reader.read()

    with open("Decrypted_data.txt","w") as enc:
        for char in encrypted_data:
            index = content.index(char)
            decrypted_data += chars[index]
        enc.write(decrypted_data)
        print(decrypted_data)
                   



encryption(chars,key,"luffy.txt")

sleep(5)

decryption(chars,"decryption.key","data.encrypted")
