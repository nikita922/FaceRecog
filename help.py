import string
from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from numpy import true_divide

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1270x700+0+0")
        self.root.title("Help")
        
        title_label = Label(self.root,text="HELP DESK",font=("times new roman",30,"bold"),bg="mediumseagreen",fg="black")
        title_label.place(x=0,y=0,width=1280,height=40)

        #img1
        img_top=Image.open(r"college_img\images.png")
        img_top=img_top.resize((1270,650),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl3=Label(self.root,image=self.photoimg_top)
        f_lbl3.place(x=5,y=40,width=1270,height=650)
        
        #Dev4
        dev_label4=Label(f_lbl3,text ="Contact:",font=("comicsansns",24,"bold"),fg="darkolivegreen",bg="white")
        dev_label4.place(x=400,y=200)
        
        
        #Dev4
        dev_label4=Label(f_lbl3,text ="Email:nikita.kundu@somaiya.edu",font=("comicsansns",24,"bold"),fg="darkolivegreen",bg="white")
        dev_label4.place(x=400,y=250)
        
        #Dev4
        dev_label4=Label(f_lbl3,text ="Phone No: 9323222017",font=("comicsansns",24,"bold"),fg="darkolivegreen",bg="white")
        dev_label4.place(x=400,y=300)
        
        
if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()

        