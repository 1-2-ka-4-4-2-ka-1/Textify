import cv2
import numpy as np
from PIL import Image, ImageDraw,ImageFont
import os

img = cv2.imread('2.JPG')
edges = cv2.Canny(img,100,200)
ans = []
highestY = 0
highestX = 0
highestCoordinate = [0, 0]

for x in range(0, edges.shape[0]):
    for y in range(0, edges.shape[1]):
        if edges[x, y] != 0:            
            ans = ans + [[x, y]]
            if highestX < x:
                highestX = x
            if highestY < y:
                highestY = y
                highestCoordinate = [x, y]       

print(f"Highest y is {highestY}")
print(f"Highest x is {highestX}")
print(f"Highest coordinate is {highestCoordinate}")


import numpy as np
from matplotlib import pyplot as plt

ind=0

folder='frames1'
images = []
for filename in os.listdir(folder):
    
    img = cv2.imread(os.path.join(folder,filename),0)
    if img is not None:

        output_size = (120,120)
        i = Image.open(os.path.join(folder,filename))
        #new_img = i.resize((10,10))
        i.thumbnail(output_size)
        i.save("med/out"+str(ind)+".jpg", "JPEG", optimize=True)
        
        output_size=(500,500)
        img2 = Image.new('RGB', output_size)
        d = ImageDraw.Draw(img2)
        font_size=2
        font_path = "C:/Users/Tiwari/Desktop/REDENSEK.ttf"
        font = ImageFont.truetype(font_path, font_size)






    #    img = cv2.imread('out.JPG',0)
       #img = cv2.imread('med/'+str(ind)+'.jpg',0)
        img=cv2.imread('med/out'+str(ind)+'.jpg',0)
        edges = cv2.Canny(img,100,200)

        # plt.subplot(121),plt.imshow(img,cmap = 'gray')
        # plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        # plt.subplot(122),plt.imshow(edges,cmap = 'gray')
        # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

        k=100
        l=200
        stri=''
        for i in edges :
            print(stri)
            stri=''
            k=k+2
            l=200
            for j in i:
                l=l+2
                if not j==0:
                    stri=stri+'.'
                    d.text((int(l), int(k)), '+', fill=(255, 0, 0),font=font)
                else:
                    stri=stri+' '
       
        plt.show()



        print(edges[0])



        img2.save('output/'+str(ind)+'.png','png')
        ind+=1



# import cStringIO
# s = cStringIO.StringIO()
# img.save(s, 'png')
# in_memory_file = s.getvalue()
