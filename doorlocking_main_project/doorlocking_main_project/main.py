"""import download as d
import face_modal as f

d.load_imagesFromServer()
f.start_modal()"""

import download as d
import face_modal as f
from socket import *
from time import ctime
import RPi.GPIO as GPIO
import os



ctrCmd = ['train','unlock']

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)



while True:
    print ('Waiting for connection')
    tcpCliSock,addr = tcpSerSock.accept()
    print ('...connected from :', addr)
    try:
        while True:
            data = ''
            data = tcpCliSock.recv(BUFSIZE)
            print(data)
            print(": ",data.decode() == ctrCmd[0])
            if not data:
                break
            if data.decode() == ctrCmd[0]:
                print("Modal Trained")
                d.load_imagesFromServer()
                f.start_modal(tcpCliSock)
                print("Modal Trained")
            if data.decode() == ctrCmd[1]:
                print ("###")
    except KeyboardInterrupt:
        GPIO.cleanup()
tcpSerSock.close();