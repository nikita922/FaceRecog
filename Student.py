import string
from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from numpy import true_divide

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1270x700+0+0")
        self.root.title("Student details")

        #-============variables==================-
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        img=Image.open(r"C:\Users\Admin\OneDrive\Desktop\PROJECTS\facial_recognition_project\college_img\sd3.jpg")
        img=img.resize((450,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=130)
        
        img1=Image.open(r"C:\Users\Admin\OneDrive\Desktop\PROJECTS\facial_recognition_project\college_img\sd2.jpg")
        img1=img1.resize((450,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl1=Label(self.root,image=self.photoimg1)
        f_lbl1.place(x=450,y=0,width=450,height=130)
        
        img2=Image.open(r"C:\Users\Admin\OneDrive\Desktop\PROJECTS\facial_recognition_project\college_img\sd5.png")
        img2=img2.resize((450,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl2=Label(self.root,image=self.photoimg2)
        f_lbl2.place(x=900,y=0,width=450,height=130)


        img3=Image.open(r"C:\Users\Admin\OneDrive\Desktop\PROJECTS\facial_recognition_project\college_img\bbb.jpg")
        img3=img3.resize((1530,680),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl3=Label(self.root,image=self.photoimg3)
        f_lbl3.place(x=0,y=130,width=1530,height=715)

        #bg_image
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=715)

        title_label = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="azure",fg="steelblue")
        title_label.place(x=0,y=0,width=1280,height=40)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=43,width=1265,height=535)

        #left frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",13,"bold"))
        Left_frame.place(x=10,y=8,width=570,height=520)

        img_left=Image.open(r"C:\Users\Admin\OneDrive\Desktop\PROJECTS\facial_recognition_project\college_img\sd1.jpg")
        img_left=img_left.resize((556,100),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl3=Label(Left_frame,image=self.photoimg_left)
        f_lbl3.place(x=5,y=0,width=556,height=100)

        #current course
        current_course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",13,"bold"))
        current_course_frame.place(x=15,y=130,width=558,height=95)
        
        #department
        dep_label=Label(current_course_frame,text ="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=2,pady=3,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=16,state="readonly")
        dep_combo["values"]=("Select Department","IT","CS","BCOM","BBA","BMS")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=20,pady=3,sticky=W)

        #course
        course_label=Label(current_course_frame,text ="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=2,pady=3,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=16,state="readonly")
        course_combo["values"]=("Select Course","FY","SY","TY")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=4,sticky=W)

        #Year
        year_label=Label(current_course_frame,text ="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=2,pady=3,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=16,state="readonly")
        year_combo["values"]=("Select Year ","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=20,pady=4,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text ="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=2,pady=3,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=16,state="readonly")
        semester_combo["values"]=("Select Semester","Semester I","Semester II")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=4,sticky=W)

        #class_student_info
        class_student_info_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",13,"bold"))
        class_student_info_frame.place(x=15,y=225,width=558,height=280)

        #Student ID
        student_id_label=Label(class_student_info_frame,text ="Student ID",font=("times new roman",12,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=2,pady=3,sticky=W)

        studentId_entry=ttk.Entry(class_student_info_frame,textvariable=self.var_std_id,width=14,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=2,pady=3,sticky=W)

        #Student name
        student_name_label=Label(class_student_info_frame,text ="Student Name",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=14,pady=4,sticky=W)

        studentname_entry=ttk.Entry(class_student_info_frame,textvariable=self.var_std_name,width=14,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=6,pady=4,sticky=W)
        
        #class_div
        class_div_label=Label(class_student_info_frame,text ="Class Division",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=2,pady=4,sticky=W)

        div_combo=ttk.Combobox(class_student_info_frame,textvariable=self.var_div,font=("times new roman",11,"bold"),width=12,state="readonly")
        div_combo["values"]=("A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=4,sticky=W)

        #Roll_no
        Roll_no_label=Label(class_student_info_frame,text ="Roll No",font=("times new roman",12,"bold"),bg="white")
        Roll_no_label.grid(row=1,column=2,padx=14,pady=4,sticky=W)

        studentrollno_entry=ttk.Entry(class_student_info_frame,textvariable=self.var_roll,width=14,font=("times new roman",12,"bold"))
        studentrollno_entry.grid(row=1,column=3,padx=6,pady=4,sticky=W)
        

        #Gender
        Gender_label=Label(class_student_info_frame,text ="Gender",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=2,pady=4,sticky=W)

        gender_combo=ttk.Combobox(class_student_info_frame,textvariable=self.var_gender,font=("times new roman",11,"bold"),width=12,state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=4,sticky=W)

        #DOB
        DOB_label=Label(class_student_info_frame,text ="DOB",font=("times new roman",12,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=14,pady=4,sticky=W)

        studentdob_entry=ttk.Entry(class_student_info_frame,textvariable=self.var_dob,width=14,font=("times new roman",12,"bold"))
        studentdob_entry.grid(row=2,column=3,padx=6,pady=4,sticky=W)

        #Email
        Email_label=Label(class_student_info_frame,text ="Email",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=2,pady=4,sticky=W)

        studentemail_entry=ttk.Entry(class_student_info_frame,textvariable=self.var_email,width=14,font=("times new roman",12,"bold"))
        studentemail_entry.grid(row=3,column=1,padx=2,pady=4,sticky=W)

        #Phone_no
        Phone_no_label=Label(class_student_info_frame,text ="Phone No",font=("times new roman",12,"bold"),bg="white")
        Phone_no_label.grid(row=3,column=2,padx=14,pady=4,sticky=W)

        studentno_entry=ttk.Entry(class_student_info_frame,textvariable=self.var_phone,width=14,font=("times new roman",12,"bold"))
        studentno_entry.grid(row=3,column=3,padx=6,pady=4,sticky=W)

        #Address
        Address_label=Label(class_student_info_frame,text ="Address",font=("times new roman",12,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=2,pady=4,sticky=W)

        studentaddress_entry=ttk.Entry(class_student_info_frame,textvariable=self.var_address,width=14,font=("times new roman",12,"bold"))
        studentaddress_entry.grid(row=4,column=1,padx=2,pady=4,sticky=W)

        #Teacher name
        Teacher_name_label=Label(class_student_info_frame,text ="Teacher Name",font=("times new roman",12,"bold"),bg="white")
        Teacher_name_label.grid(row=4,column=2,padx=14,pady=4,sticky=W)

        studentteach_entry=ttk.Entry(class_student_info_frame,textvariable=self.var_teacher,width=14,font=("times new roman",12,"bold"))
        studentteach_entry.grid(row=4,column=3,padx=6,pady=4,sticky=W)

        #Radiobutton
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_info_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        #Radiobutton2
        radiobtn2=ttk.Radiobutton(class_student_info_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)


        #SAVEUPDATEFRAME
        btn_frame=Frame(class_student_info_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=185,width=553,height=28)

        #savebutton
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=14,font=("times new roman",11,"bold"),bg="lightblue",fg="black")
        save_btn.grid(row=0,column=0)

        #updatebutton
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=14,font=("times new roman",11,"bold"),bg="crimson",fg="white")
        update_btn.grid(row=0,column=1)

        #deletebutton
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("times new roman",11,"bold"),bg="pink",fg="black")
        delete_btn.grid(row=0,column=2)

        #resetbutton
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",11,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=3)

        #photobuttonFRAME
        btn2_frame=Frame(class_student_info_frame,bd=2,bg="white",relief=RIDGE)
        btn2_frame.place(x=0,y=212,width=553,height=28)

        #photosamplebutton
        take_btn=Button(btn2_frame,command=self.generate_dataset,text="Take photo sample",width=30,font=("times new roman",11,"bold"),bg="yellow",fg="black")
        take_btn.grid(row=0,column=0)

        update_btn=Button(btn2_frame,text="Update photo sample",width=30,font=("times new roman",11,"bold"),bg="purple",fg="white")
        update_btn.grid(row=0,column=1)

        #right frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",13,"bold"))
        Right_frame.place(x=590,y=8,width=660,height=506)

        img_right=Image.open(r"C:\Users\Admin\OneDrive\Desktop\PROJECTS\facial_recognition_project\college_img\sdd.png")
        img_right=img_right.resize((650,120),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl3=Label(Right_frame,image=self.photoimg_right)
        f_lbl3.place(x=5,y=0,width=646,height=100)

        #====search system=====
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="SEARCH SYSTEM",font=("times new roman",13,"bold"))
        search_frame.place(x=10,y=100,width=635,height=60)

        #searchbar
        search_label=Label(search_frame,text ="Search By:",font=("times new roman",13,"bold"),bg="sandybrown")
        search_label.grid(row=0,column=0,padx=14,pady=4,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=13,state="readonly")
        search_combo["values"]=("Select","Roll No.","Phone no.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=4,sticky=W)

        #entry fill
        search_entry=ttk.Entry(search_frame,width=17,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=6,pady=4,sticky=W)        

        #searchbutton
        search_btn=Button(search_frame,text="Search",width=9,font=("times new roman",12,"bold"),bg="lightcoral",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        #showallbutton
        showall_btn=Button(search_frame,text="Show All",width=8,font=("times new roman",12,"bold"),bg="lightcoral",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)

        #====table system=====
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=165,width=635,height=280)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DateOfBirth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("email",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #=====function declaration==========

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="nkundu@922",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into studentt values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_std_id.get(),
                                                                                                self.var_std_name.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_radio1.get()

                                                                                               )) 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #==========fetchdata===========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="nkundu@922",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from studentt")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close() 

    #===================get cursor=============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #==============UPDATE FUNCTION=============
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="nkundu@922",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update studentt set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                   self.var_dep.get(),
                                                                                                                                                                                   self.var_course.get(),
                                                                                                                                                                                   self.var_year.get(),
                                                                                                                                                                                   self.var_semester.get(),
                                                                                                                                                                                   self.var_std_name.get(),
                                                                                                                                                                                   self.var_div.get(),
                                                                                                                                                                                   self.var_roll.get(),
                                                                                                                                                                                   self.var_gender.get(),
                                                                                                                                                                                   self.var_dob.get(),
                                                                                                                                                                                   self.var_email.get(),
                                                                                                                                                                                   self.var_phone.get(),
                                                                                                                                                                                   self.var_address.get(),
                                                                                                                                                                                   self.var_teacher.get(),
                                                                                                                                                                                   self.var_radio1.get(),
                                                                                                                                                                                   self.var_std_id.get()
                                                                                                                                                                                  ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #===============DELETE FUNCTION======================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID is mandatory",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do You want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="nkundu@922",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from studentt where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #============reset data ===============      
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #============generate data set and take photo sample==================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="nkundu@922",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from studentt")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update studentt set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                   self.var_dep.get(),
                                                                                                                                                                                   self.var_course.get(),
                                                                                                                                                                                   self.var_year.get(),
                                                                                                                                                                                   self.var_semester.get(),
                                                                                                                                                                                   self.var_std_name.get(),
                                                                                                                                                                                   self.var_div.get(),
                                                                                                                                                                                   self.var_roll.get(),
                                                                                                                                                                                   self.var_gender.get(),
                                                                                                                                                                                   self.var_dob.get(),
                                                                                                                                                                                   self.var_email.get(),
                                                                                                                                                                                   self.var_phone.get(),
                                                                                                                                                                                   self.var_address.get(),
                                                                                                                                                                                   self.var_teacher.get(),
                                                                                                                                                                                   self.var_radio1.get(),
                                                                                                                                                                                   self.var_std_id.get()==id+1
                                                                                                                                                                                  ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #=======================Load predefined data on face frontal from opencv===============

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.5
                    #munimum neighbur = 3

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,55),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)







        


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

