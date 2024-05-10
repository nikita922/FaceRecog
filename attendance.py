import re
import string
from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
#from numpy import imag, true_divide
#from time import strftime
from datetime import datetime
# from mysqlx import Row
import numpy as np
from Student import Student
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1270x700+0+0")
        self.root.title("Attendance system")
        
        #===============variables=========
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_attendance=StringVar()
        
        img=Image.open(r"C:\Users\Admin\OneDrive\Desktop\PROJECTS\facial_recognition_project\college_img\trrainn.jpg")
        img=img.resize((675,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=675,height=130)
        
        img1=Image.open(r"C:\Users\Admin\OneDrive\Desktop\PROJECTS\facial_recognition_project\college_img\traint.jpg")
        img1=img1.resize((675,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl1=Label(self.root,image=self.photoimg1)
        f_lbl1.place(x=675,y=0,width=675,height=130)

        img3=Image.open(r"C:\Users\Admin\OneDrive\Desktop\PROJECTS\facial_recognition_project\college_img\bg.jpg")
        img3=img3.resize((1530,680),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl3=Label(self.root,image=self.photoimg3)
        f_lbl3.place(x=0,y=130,width=1530,height=715)
        
        title_label = Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="greenyellow",fg="black")
        title_label.place(x=0,y=130,width=1280,height=40)
        
        main_frame=Frame(f_lbl3,bd=2,bg="white")
        main_frame.place(x=5,y=43,width=1265,height=535)
        
        #left frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT ATTENDANCE DETAILS",font=("times new roman",13,"bold"))
        Left_frame.place(x=10,y=8,width=570,height=480)
        
        img_left=Image.open(r"C:\Users\Admin\OneDrive\Desktop\PROJECTS\facial_recognition_project\college_img\traindataaa.png")
        img_left=img_left.resize((556,100),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl3=Label(Left_frame,image=self.photoimg_left)
        f_lbl3.place(x=5,y=0,width=556,height=100)
        
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=105,width=555,height=325)
        
        
        #label and entry
        attendance_id_label=Label(left_inside_frame,text ="Attendance ID:",font=("comicsansns",12,"bold"),bg="white")
        attendance_id_label.grid(row=0,column=0,padx=2,pady=3,sticky=W)
        
        attendanceId_entry=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_atten_id,font=("comicsansns",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=2,pady=3,sticky=W)
        
        #name
        name_id_label=Label(left_inside_frame,text ="Name:",font=("comicsansns",12,"bold"),bg="white")
        name_id_label.grid(row=0,column=2,padx=2,pady=3,sticky=W)
        
        nameId_entry=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_atten_name,font=("comicsansns",12,"bold"))
        nameId_entry.grid(row=0,column=3,padx=2,pady=3,sticky=W)
        
        #Rollno
        roll_id_label=Label(left_inside_frame,text ="Roll No:",font=("comicsansns",12,"bold"),bg="white")
        roll_id_label.grid(row=1,column=0,padx=2,pady=3,sticky=W)
        
        rollId_entry=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_atten_roll,font=("comicsansns",12,"bold"))
        rollId_entry.grid(row=1,column=1,padx=2,pady=3,sticky=W)
        
        #Dep
        dep_id_label=Label(left_inside_frame,text ="Department No.",font=("comicsansns",12,"bold"),bg="white")
        dep_id_label.grid(row=1,column=2,padx=2,pady=3,sticky=W)
        
        depId_entry=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_atten_dep,font=("comicsansns",12,"bold"))
        depId_entry.grid(row=1,column=3,padx=2,pady=3,sticky=W)
        
        #Date
        date_id_label=Label(left_inside_frame,text ="Date:",font=("comicsansns",12,"bold"),bg="white")
        date_id_label.grid(row=2,column=0,padx=2,pady=3,sticky=W)
        
        dateId_entry=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_atten_date,font=("comicsansns",12,"bold"))
        dateId_entry.grid(row=2,column=1,padx=2,pady=3,sticky=W)
        
        #Time
        time_id_label=Label(left_inside_frame,text ="Time:",font=("comicsansns",12,"bold"),bg="white")
        time_id_label.grid(row=2,column=2,padx=2,pady=3,sticky=W)
        
        timeId_entry=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_atten_time,font=("comicsansns",12,"bold"))
        timeId_entry.grid(row=2,column=3,padx=2,pady=3,sticky=W)
        
        #attendance
        attendancelabel=Label(left_inside_frame,text="Attendance status:",bg="white",font=("comicsansns",12,"bold"))
        attendancelabel.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=14,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=4)
        self.atten_status.current(0)
        
        #SAVEUPDATEFRAME
        btn_frame=Frame(left_inside_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=290,width=553,height=30)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=14,font=("times new roman",11,"bold"),bg="lightblue",fg="black")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=14,font=("times new roman",11,"bold"),bg="crimson",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=14,font=("times new roman",11,"bold"),bg="pink",fg="black")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=15,command=self.reset_data,font=("times new roman",11,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=3)

        #right frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="ATTENDANCE DETAILS",font=("times new roman",13,"bold"))
        Right_frame.place(x=590,y=8,width=660,height=506)
        
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=645,height=450)
        
        
        #========scroll bar============
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.attendanceReportTabl=ttk.Treeview(table_frame,column=("id","roll","name","department","date","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.attendanceReportTabl.xview)
        scroll_y.config(command=self.attendanceReportTabl.yview)
        
        self.attendanceReportTabl.heading("id",text="Attendance ID")
        self.attendanceReportTabl.heading("roll",text="Roll No.")
        self.attendanceReportTabl.heading("name",text="Name")
        self.attendanceReportTabl.heading("department",text="Department")
        self.attendanceReportTabl.heading("date",text="Date")
        self.attendanceReportTabl.heading("time",text="Time")
        self.attendanceReportTabl.heading("attendance",text="Attendance")
        
        self.attendanceReportTabl["show"]="headings"
        
        self.attendanceReportTabl.column("id",width=100)
        self.attendanceReportTabl.column("roll",width=100)
        self.attendanceReportTabl.column("name",width=100)
        self.attendanceReportTabl.column("department",width=100)
        self.attendanceReportTabl.column("date",width=100)
        self.attendanceReportTabl.column("time",width=100)
        self.attendanceReportTabl.column("attendance",width=100)
        
        self.attendanceReportTabl.pack(fill=BOTH,expand=1)
        
        self.attendanceReportTabl.bind("<ButtonRelease>",self.get_cursor)
        
    #=================fetchdata================
    
    def fetchData(self,rows):
        self.attendanceReportTabl.delete(*self.attendanceReportTabl.get_children())
        for i in rows:
            self.attendanceReportTabl.insert("",END,values=i)
    #-==============import csv===  ==========      
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
                
                
    #-==============export csv===============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Data Exported to "+os.path.basename(fln)+" Successfully.")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            
    def get_cursor(self,event=""):
        cursor_row=self.attendanceReportTabl.focus()
        content=self.attendanceReportTabl.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_time.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_date.set("")
        self.var_atten_time.set("")
        self.var_atten_attendance.set("")
        
        
        
        

        
if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
