from PIL import ImageGrab
from PIL import Image
import socket
import time

HOST,PORT = "localhost", 290
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)# creating a tcp socket
sock.connect((HOST,PORT))# connecting a socket

s1 = "hk"
for i in range(11):
    s2 = s1 + str(0)
    im = ImageGrab.grab()
    im.save("%s.png" %s2)

for i in range(11):
    s2 = s1 + str(i)
    f = open('%s.png' % s2 ,'rb')     
    l = f.read(1024)
    print l
    sock.send(l)
    while True:
        l = f.read(1024)
        if not l:
            print "l = ",l
            sock.send(" ")
            f.close()           
            print "Done Sending"
            break    
        sock.send(l)
sock.send(" ")

