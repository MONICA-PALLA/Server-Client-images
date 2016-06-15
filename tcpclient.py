from PIL import ImageGrab
from PIL import Image
import socket
import time

#HOST = socket.gethostname()
#PORT = 5051
HOST,PORT = "localhost", 2900
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)# creating a tcp socket
#sock.connect((HOST,PORT))# connecting a socket

s1 = "hk"
for i in range(11):
    sock.connect((HOST,PORT))# connecting a socket
    s2 = s1 + str(i)    
    im = ImageGrab.grab()
    im.save("%s.png" %s2)
    time.sleep(2)
    f = open('%s.png' % s2 ,'rb')
    l = f.read(1024)
    while (l):
        sock.send(l)
        l = f.read(1024)    
        if l == '':
            f.close()
            sock.send(l)
            break
    print "Done Sending"
    PORT = PORT + 1

sock.close()
