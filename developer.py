import string
from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from numpy import true_divide

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1270x700+0+0")
        self.root.title("Developer")
        
        title_label = Label(self.root,text="DEVELOPER",font=("times new roman",30,"bold"),bg="mediumseagreen",fg="black")
        title_label.place(x=0,y=0,width=1280,height=40)

        #img1
        img_top=Image.open(r"college_img\bgg.jpg")
        img_top=img_top.resize((1270,650),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl3=Label(self.root,image=self.photoimg_top)
        f_lbl3.place(x=5,y=40,width=1270,height=650)
        
        #Frameee
        main_frame=Frame(f_lbl3,bd=2,bg="white")
        main_frame.place(x=420,y=40,width=425,height=535)
        
        ##img1
        #img_top1=Image.open(r"college_img\nikki.jpeg")
        #img_top1=img_top1.resize((150,150),Image.ANTIALIAS)
        #self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        #f_lbl3=Label(main_frame,image=self.photoimg_top1)
        #f_lbl3.place(x=260,y=10,width=150,height=150)
        
        #Dev
        dev_label=Label(main_frame,text ="BIO",font=("comicsansns",25,"bold"),fg="black",bg="white")
        dev_label.place(x=170,y=40)
        
        #Dev2
        dev_label2=Label(main_frame,text ="Hii,Myself Nikita Kundu",font=("comicsansns",14,"bold"),fg="black",bg="white")
        dev_label2.place(x=95,y=100)
        
        #Dev3
        dev_label3=Label(main_frame,text ="Roll No: 2106842,TYIT.",font=("comicsansns",14,"bold"),fg="black",bg="white")
        dev_label3.place(x=100,y=130)
        
        #Dev4
        dev_label4=Label(main_frame,text ="I have completed my Schooling from",font=("comicsansns",13,"bold"),fg="black",bg="white")
        dev_label4.place(x=60,y=170)
        
        #Dev3
        dev_label5=Label(main_frame,text ="'Blossom english high school' with 81.20%.",font=("comicsansns",13,"bold"),fg="black",bg="white")
        dev_label5.place(x=35,y=200)
        
        #Dev3
        dev_label6=Label(main_frame,text ="I have completed my 12th(SCIENCE) from",font=("comicsansns",13,"bold"),fg="black",bg="white")
        dev_label6.place(x=45,y=230)
        
        #Dev7
        dev_label7=Label(main_frame,text ="'KB College of Science and Commerce' with 70%.",font=("comicsansns",13,"bold"),fg="black",bg="white")
        dev_label7.place(x=16,y=260)
        
        #Dev8
        dev_label8=Label(main_frame,text ="I am currently pursuing my Bachelor's in IT from",font=("comicsansns",13,"bold"),fg="black",bg="white")
        dev_label8.place(x=20,y=290)
        
        #Dev9
        dev_label9=Label(main_frame,text ="'K.J Somaiya College Of Science and Commerce'",font=("comicsansns",13,"bold"),fg="black",bg="white")
        dev_label9.place(x=18,y=320)
        
        #Dev9
        dev_label9=Label(main_frame,text =" and I am in Last Semester (2022 passout).",font=("comicsansns",13,"bold"),fg="black",bg="white")
        dev_label9.place(x=40,y=350)
        
        
        
       # #img1
       # img_top2=Image.open(r"college_img\logo.png")
       # img_top2=img_top2.resize((420,360),Image.ANTIALIAS)
       # self.photoimg_top2=ImageTk.PhotoImage(img_top2)
       # f_lbl3=Label(main_frame,image=self.photoimg_top2)
       # f_lbl3.place(x=0,y=170,width=420,height=360)
        
if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
