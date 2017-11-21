from tkinter.filedialog import askopenfilename
from tkinter import *
import cv2
import numpy as np
import os


root = Tk()


file=" "


class imageSplitter():

    a1_right= [1440,192]
    a1_left = [1536,192]

    img_out=np.zeros((1080,1920,3), np.uint8)


    
    
    def fileOpener(self):
        file = askopenfilename()
        return file

    def distributer(self):
     height,width,chan=self.img.shape
     print (width,height,chan)
     if (width == 2976 and height == 192):
         self.A1()
     elif (width == 2336 and height == 192):
         self.A4()
     elif (width == 1184 and height == 192):
         self.Nord()
     else:
         print("THERE IS A PROBLEM !..")
    
                
    def pathDiverter(self):
        global file
        global img
        global img_out
        self.file=self.fileOpener()
        self.img=cv2.imread(self.file)
        directory,imageFile = os.path.split(file)
        print(directory)
        print(imageFile)
        

        self.distributer()
        
    
    
        
    def A1(self):
        
        self.img_out[0:self.a1_left[1],0:self.a1_left[0],:]= self.img[0:self.a1_left[1],0:self.a1_left[0],:]
        self.img_out[192:192+ self.a1_right[1],0:self.a1_right[0],:]= self.img[0:self.a1_right[1],self.a1_left[0]:self.a1_left[0]+self.a1_right[0],:]              
        cv2.imshow("test",self.img)
        cv2.imshow("test2",self.img_out)


        
n=imageSplitter()



frame=Frame(root,width=250,height=300)
frame.pack()
title=Label(frame,text="FC BAYERN SUD SCREENS",bg="red",fg="white")
title.pack(fill=X)

title=Label(frame,text="FC BAYERN SUD SCREENS",width=50,height=30)
title.pack(fill=X)

button1=Button(frame,text="Browse",command=n.pathDiverter)
button2=Button(frame,text="APPLY",command=n.distributer)
button1.pack(side="left")
button2.pack(side="left")

root.mainloop()







