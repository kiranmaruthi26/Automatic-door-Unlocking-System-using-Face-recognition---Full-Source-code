"""import download as d
import face_modal as f

d.load_imagesFromServer()
f.start_modal()"""

import lock
from socket import *
from time import ctime
import RPi.GPIO as GPIO
import subprocess
import os
import signal



ctrCmd = ['manual','terminate']

HOST = ''
PORT = 21566
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
            print(": ",data.decode() == ctrCmd[1])
            if not data:
                break
            if data.decode() == ctrCmd[0]:
                lock.locker()
            if data.decode() == ctrCmd[1]:
                lock.locker()
                #print("termination")
                #with open('../app.pid') as f:
                    #line = f.readline()
                #os.kill(int(line), signal.SIGKILL)
    except KeyboardInterrupt:
        GPIO.cleanup()
tcpSerSock.close();