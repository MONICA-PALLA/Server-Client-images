from PIL import ImageGrab
from PIL import Image

s1 = "screen"

#for i in range(3):
 #   s2 = s1 + str(i)
  #  im = ImageGrab.grab()
   # im.save("%s.png" % s2)

    #image = Image.open("%s.png" % s2)
    #image.show()

#path=r'C:/Users/Mounika/Desktop/codes/screen0.png'

for j in range(3):
    #s2 = s1 + str(j)
    #image = Image.open(path)
    image = Image.open(open("screen0.png", "rb"))
    image.show()
    
