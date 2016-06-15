import socket
import threading
import SocketServer
from PIL import Image


class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler): 

    def handle(self): 

        s1 = "rk"
        cur_thread = threading.current_thread()

        for i in range(11):
            s2 = s1 + str(i)
            f = open('%s.png' % s2,'wb')        
            while True:
                data = self.request.recv(1024)
                f.write(data)
                if data=='' :
                    print "Done Receiving"
                    f.close()
                    break
            image = Image.open(open('%s.png' % s2, "rb"))
            image.load()
            image.show()    

        #c.close()
        #s.close()
        server.shutdown()    
        server.server_close()

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    
    pass

if __name__ == "__main__":
    
    HOST,PORT = "localhost", 209
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address 
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    print "Server loop running in thread:", server_thread.name
    #server.shutdown()      # this two commonds are used to close the socketserver
    #server.server_close()
