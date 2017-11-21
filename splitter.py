from tkinter.filedialog import askopenfilename
from tkinter import *
import cv2
import numpy as np

root = Tk()


class imageSplitter():
    
    def fileOpener(self):
        file = askopenfilename()
        return file

    def shower1(self):
        file=self.fileOpener()
        img=cv2.imread(file)
        cv2.imshow("test",img)

    def shower2(self):
        file=self.fileOpener()
        img=cv2.imread(file)
        cv2.imshow("test2",img)



n=imageSplitter()


frame=Frame(root,width=800,height=900)
frame.pack()
title=Label(frame,text="FC BAYERN SUD SCREENS",bg="red",fg="white")
title.pack(fill=X)

button1=Button(frame,text="Browse",command=n.shower1)
button2=Button(frame,text="Browse",command=n.shower1)
button1.pack(side="bottom")
button2.pack(side="bottom")

root.mainloop()
