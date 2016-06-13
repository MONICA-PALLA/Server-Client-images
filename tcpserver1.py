import socket
import Image
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host,port = "localhost", 290
s.bind((host, port))
s.listen(5)
c, addr = s.accept()

s1 = "rk"
s2 = s1 + str(0)
f = open('%s.png' %s2,'wb')
#l = c.recv(1024)
for i in range(1, 11):
    #s2 = s1 + str(i)
    #print "opening new file"
    #f = open('%s.png' % s2,'wb')
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

#for i in range(11):
 #   image = Image.open('%s.png' % s2)
  #  image.show()

#c.close()    
