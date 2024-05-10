from doctest import IGNORE_EXCEPTION_DETAIL
from time import strftime
from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
from Student import Student
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_recognition_sys:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1270x700+0+0")
        self.root.title("Face Recognition Based Attendence System")

        img=Image.open(r"college_img\face2.jpg")
        img=img.resize((450,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=130)
        
        img1=Image.open(r"college_img\face3.png")
        img1=img1.resize((450,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl1=Label(self.root,image=self.photoimg1)
        f_lbl1.place(x=450,y=0,width=450,height=130)
        
        img2=Image.open(r"college_img\face5.jpg")
        img2=img2.resize((450,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl2=Label(self.root,image=self.photoimg2)
        f_lbl2.place(x=900,y=0,width=450,height=130)

        img3=Image.open(r"college_img\backg.png")
        img3=img3.resize((1530,680),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl3=Label(self.root,image=self.photoimg3)
        f_lbl3.place(x=0,y=130,width=1530,height=710)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_label = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("century schoolbook",24,"bold"),bg="white",fg="midnightblue")
        title_label.place(x=0,y=0,width=1280,height=45)
        
        #========time==============
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
            
        lbl=Label(title_label,font=("times new roman",13,"bold"),background="white",foreground="black")
        lbl.place(x=0,y=0,width=100,height=40)
        time()

        #STUDENT BUTTON
        img4 = Image.open(r"college_img\selfservice.png")
        img4 = img4.resize((190,190),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image = self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x = 160,y = 100,width = 190, height = 160)

        b2 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b2.place(x = 160,y = 230,width = 190, height = 35)

        #DETECT FACE
        img5 = Image.open(r"college_img\report2.jpg")
        img5 = img5.resize((190,190),Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image = self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x = 410,y = 100,width = 190, height = 160)

        b2 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b2.place(x = 410,y = 230,width = 190, height = 35)


        #ATTENDANCE
        img6 = Image.open(r"college_img\attend.jpg")
        img6 = img6.resize((190,190),Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image = self.photoimg6,cursor="hand2",command=self.attendance)
        b1.place(x = 660,y = 100,width = 190, height = 160)

        b2 = Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b2.place(x = 660,y = 230,width = 190, height = 35)

         #HELP DESK
        img7 = Image.open(r"college_img\helpdesk.png")
        img7 = img7.resize((190,190),Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image = self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x = 910,y = 100,width = 190, height = 160)

        b2 = Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b2.place(x = 910,y = 230,width = 190, height = 35)

         #TRAIN FACE BUTTON
        img8 = Image.open(r"college_img\train.jpg")
        img8 = img8.resize((190,190),Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image = self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x = 160,y = 285,width = 190, height = 160)

        b2 = Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b2.place(x = 160,y = 410,width = 190, height = 35)


        #PHOTOS FACE BUTTON
        img9 = Image.open(r"college_img\facee.jpg")
        img9 = img9.resize((190,190),Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,image = self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x = 410,y = 285,width = 190, height = 130)

        b2 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b2.place(x = 410,y = 410,width = 190, height = 35)


        #DEVELOPER BUTTON
        img10 = Image.open(r"college_img\developer.png")
        img10 = img10.resize((190,190),Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,image = self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x = 660,y = 285,width = 190, height = 130)

        b2 = Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b2.place(x = 660,y = 410,width = 190, height = 35)


        #EXIT BUTTON
        img11 = Image.open(r"college_img\ex.jpg")
        img11 = img11.resize((190,190),Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,image = self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x = 910,y = 285,width = 190, height = 130)

        b2 = Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b2.place(x = 910,y = 410,width = 190, height = 35)

    def open_img(self):
        os.startfile("data")
        
    #============exit function==========
    def iExit(self):
        self.iExit=messagebox.askyesno("Face recognition","Are you sure you want to exit?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
        
    

        #===============Function buttons=========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
        
    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
        
    
    




if __name__=="__main__":
    root=Tk()
    obj=Face_recognition_sys(root)
    root.mainloop()
