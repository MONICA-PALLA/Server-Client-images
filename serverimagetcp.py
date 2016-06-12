import socket
import Image

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 506
s.bind((host, port))
s.listen(10)
c, addr = s.accept()
s1 = "rk"

for i in range(5):
    s2 = s1 + str(i)
    f = open('%s.png'% s2,'wb')
    l = c.recv(1024)
    while True:
        f.write(l)
        l = c.recv(1024)
        if l=='' :
            print "Done Receiving"
            f.close()
            break
        
#for k in range(5):
 #   s3 = s1 + str(k)
  #  image = Image.open("%s.png"% s3)
   # image.show()

c.close()
