from PIL import ImageGrab
from PIL import Image
import socket
import time

HOST,PORT = "localhost", 2900
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((HOST,PORT))

s1 = "hk"
for i in range(2):
    time.sleep(3)
    s2 = s1 + str(i)
    im = ImageGrab.grab()
    im.save("%s.png" %s2)
i = 2
while True :
#for i in range(2, 11):
    s3 = s1 + str(i-2)
    s2 = s1 + str(i)
    im = ImageGrab.grab()
    im.save("%s.png" %s2)
    f = open('%s.png' % s3 ,'rb')     
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
    i += 1    
sock.send(" ")

