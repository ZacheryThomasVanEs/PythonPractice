# -*- coding: utf-8 -*-
"""
@author: Zachery Van Es
"""

from cryptography.fernet import Fernet

def createKey():   
    key = Fernet.generate_key()
    with open("main.key","wb") as key_file:
        key_file.write(key)


def loadKey():    
    return open("main.key","rb").read()


def encryptionMode(message):
    key = loadKey()
    encodedMessage = message.encode()
    f = Fernet(key)
    encryptedMessage = f.encrypt(encodedMessage)
    return(encryptedMessage)

def decryptionMode(message):
    key = loadKey()
    f = Fernet(key)
    decryptedMessage = f.decrypt(message)
    return(decryptedMessage)

if __name__ == "__main__":
    userMessage = input("Enter message to be encrypted:")
    encrptMess = encryptionMode(userMessage)
    print(encrptMess)
    decrptMess = decryptionMode(encrptMess)
    print(decrptMess)