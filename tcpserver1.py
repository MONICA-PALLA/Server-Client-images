import socket
import Image
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host,port = "localhost", 290
s.bind((host, port))
s.listen(5)
c, addr = s.accept()

s1 = "rk"
for i in range(5):
    s2 = s1 + str(i)
    f = open('%s.png' % s2,'wb')
    l = c.recv(4096)
    while True:
        f.write(l)
        time.sleep(5)
        l = c.recv(4096)
        if l=='' :        
            print "Done Receiving"
            f.close()
            break

#for i in range(4):
 #   image = Image.open('%s.png' % s2)
  #  image.show()

c.close()    
