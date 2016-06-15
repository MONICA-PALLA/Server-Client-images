import socket
import threading
import SocketServer
from PIL import Image
import time


class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler): 

    def handle(self): 

        s1 = "rk"
        cur_thread = threading.current_thread()

        s2 = s1 + str(0)
        f = open('%s.png' %s2,'wb')
        i = 1
        while True :
        #for i in range(1, 11):
            l = self.request.recv(1024)
            print l
            while True:
                f.write(l)
                l = self.request.recv(1024)     
                if l == " ":
                    print "EOF"
                    time.sleep(2)
                    f.close()
                    s2 = s1 + str(i)
                    f = open('%s.png' % s2,'wb')
                    print "Done receiving"
                    break    
            s3 = s1 + str(i-1)
            image = Image.open('%s.png' % s3)
            image.show()
            i += 1
            #time.sleep(1)
  
        server.shutdown()    
        server.server_close()

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    
    pass

if __name__ == "__main__":
    
    HOST,PORT = "192.168.100.21", 2900
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address 
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    print "Server loop running in thread:", server_thread.name
    #server.shutdown()      # this two commonds are used to close the socketserver
    #server.server_close()
