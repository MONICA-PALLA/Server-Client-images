import socket
import gtk.gdk

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         
host = socket.gethostname() 
port = 506
s.connect((host, port))
s1 = "hk"

for i in range(5):
    s2 = s1 + str(i)
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    print "The size of the window is %d x %d" % sz
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    if (pb != None):
        pb.save("%s.png" % s2,"png")
        print "Screenshot saved"
    else:
        print "Unable to get the screenshot."
    f = open('%s.png' % s2,'rb')
    l = f.read(1024)

    while (l):
        s.send(l)
        l = f.read(1024)    
        if l == '':
            f.close()
            s.send(l)
            break
    print "Done Sending"

s.close()
#print "Done Sending"       
