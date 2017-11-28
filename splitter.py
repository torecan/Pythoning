from tkinter.filedialog import askopenfilename
from tkinter import *
import cv2
import numpy as np
import os


root = Tk()




class imageSplitter():

    a1_right= [1440,192]
    a1_left = [1536,192]

    a4_right= [1184,192]
    a4_left= [1152,192]

    nord_right= [1184,192]


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
        print("TORE")
        global file
        global imageFile
        global directory
        global img
        global img_out
        self.file=self.fileOpener()
        print(self.file)
        self.img=cv2.imread(self.file)
        directory,imageFile = os.path.split(self.file)
        print(imageFile)
        dir_a1=directory+"/a1"
        dir_a4=directory+"/a4"
        dir_nord=directory+"/nord"
        if not os.path.exists(dir_a1):
         os.makedirs(dir_a1)
        if not os.path.exists(dir_a4):
         os.makedirs(dir_a4)
        if not os.path.exists(dir_nord):
         os.makedirs(dir_nord)
    
        
    def A1(self):
        
        self.img_out[0:self.a1_left[1],0:self.a1_left[0],:]= self.img[0:self.a1_left[1],0:self.a1_left[0],:]
        self.img_out[192:192+ self.a1_right[1],0:self.a1_right[0],:]= self.img[0:self.a1_right[1],self.a1_left[0]:self.a1_left[0]+self.a1_right[0],:]              
        #cv2.imshow("test",self.img)
        #cv2.imshow("test2",self.img_out)
        path_file=directory+"/a1/"+imageFile+".png"
        cv2.imwrite(path_file,self.img_out)
        print("SUCCESSFULLY")

    def A4(self):
        
        self.img_out[0:self.a4_left[1],0:self.a4_left[0],:]= self.img[0:self.a4_left[1],0:self.a4_left[0],:]
        self.img_out[192:192+ self.a4_right[1],0:self.a4_right[0],:]= self.img[0:self.a4_right[1],self.a4_left[0]:self.a4_left[0]+self.a4_right[0],:]              
        #cv2.imshow("test",self.img)
        #cv2.imshow("test2",self.img_out)
        path_file=directory+"/a4/"+imageFile+".png"
        cv2.imwrite(path_file,self.img_out)
        print("SUCCESSFULLY")

    def Nord(self):
        
        self.img_out[0:self.nord_right[1],0:self.nord_right[0],:]= self.img[0:self.nord_right[1],0:self.nord_right[0],:]
        #cv2.imshow("test",self.img)
        #cv2.imshow("test2",self.img_out)
        path_file=directory+"/nord/"+imageFile+".png"
        cv2.imwrite(path_file,self.img_out)
        print("SUCCESSFULLY")
    



        
n=imageSplitter()

frame=Frame(root,width=450,height=400)
frame.pack()
title=Label(frame,text="FC BAYERN SUD SCREENS",bg="red",fg="white")
title.pack(fill=X)

m1=Checkbutton(root)
m1.pack()
title=Label(frame,text="FC BAYERN SUD SCREENS",width=50,height=30)
title.pack(fill=X)


button1=Button(frame,text="Browse",command=n.pathDiverter)
button2=Button(frame,text="APPLY",command=n.distributer)
button1.pack(side="left")
button2.pack(side="left")

root.mainloop()

