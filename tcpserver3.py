import socket
import Image
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host,port = "localhost", 2900
s.bind((host, port))
s.listen(5)
c, addr = s.accept()

s1 = "rk"
s2 = s1 + str(0)
f = open('%s.png' %s2,'wb')
#l = c.recv(1024)
i = 1
#for i in range(1, 11):
while True :    
    l = c.recv(1024)
    print l
    while True:
        f.write(l)
        l = c.recv(1024)     
        if l == " ":
            print "EOF"
            time.sleep(2)
            f.close()
            s2 = s1 + str(i)
            f = open('%s.png' % s2,'wb')
            print "Done receiving"
            break        
    s3 = s1 + str(i-1)
    im = Image.open('%s.png' % s3)
    im.show()
    time.sleep(1)
    #im.close()
    i += 1
    time.sleep(1)
    
        
#c.close()    
