from PIL import ImageGrab
from PIL import Image
import socket
import time

#HOST = socket.gethostname()
#PORT = 5051
HOST,PORT = "localhost", 290
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)# creating a tcp socket
sock.connect((HOST,PORT))# connecting a socket

s1 = "hk"
for i in range(5):
    #sock.connect((HOST,PORT))# connecting a socket
    s2 = s1 + str(i)    
    im = ImageGrab.grab()
    im.save("%s.png" %s2)
    #time.sleep(2)
    f = open('%s.png' % s2 ,'rb')
    l = f.read(4096)
    while (l):
        sock.send(l)
        l = f.read(4096)    
        if l == '':
            f.close()
            sock.send(l)
            break
    print "Done Sending"
    

sock.close()
