from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_recognition_sys


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1280x700+0+0")
         
        img1 = Image.open("college_img/bbg.jpg")
        img1 = img1.resize((1280,700), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)  
        bg_lbl=Label(self.root,image=self.photoImg1)
        bg_lbl.place(x=0,y=0,width=1280,height=700)  
        
        
        frame=Frame(self.root,bg="white")   
        frame.place(x=455,y=90,width=400,height=500)
        
        img2 = Image.open("college_img/icon2.jpg")
        img2 = img2.resize((150,150), Image.ANTIALIAS)
        self.photoImg2 = ImageTk.PhotoImage(img2)  
        bg_lbl2=Label(frame,image=self.photoImg2,bg="black",borderwidth=0)
        bg_lbl2.place(x=120,y=2,width=150,height=150)  
        
        get_str=Label(frame,text="Get Started",font=("MS Serif",18,"bold"),fg="black",bg="white")
        get_str.place(x=130,y=136)
        
        username_lbl=Label(frame,text="Username",font=("times new roman",13,"bold"),fg="black",bg="white")
        username_lbl.place(x=81,y=170)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",14,"bold"),foreground="blue")
        self.txtuser.place(x=60,y=195,width=270)
        
        password=lbl=Label(frame,text="Password",font=("times new roman",13,"bold"),fg="black",bg="white")
        password.place(x=81,y=230)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman",14,"bold"),show="*")
        self.txtpass.place(x=60,y=254,width=270)
        
        # ======Icon Images=================
        img3=Image.open("college_img/icon2.jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(frame,image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=60,y=170,width=25,height=25)
        
        
        img4=Image.open("college_img/icon3.png")
        img4=img4.resize((20,20),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        lblimg4=Label(frame,image=self.photoimage4,bg="black",borderwidth=0)
        lblimg4.place(x=60,y=229,width=20,height=20)
        
        # LoginButton
        btn_login=Button(frame,command=self.login,text="Login",borderwidth=3,relief=RAISED,cursor="hand2",font=("times new roman",16,"bold"),fg="white",bg="red" ,activebackground="#228B22",activeforeground="#21093E")
        btn_login.place(x=130,y=300,width=120,height=35)
        
        # registerbutton
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
        registerbtn.place(x=21,y=340,width=160)
        
        # forgetpassbtn
        registerbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
        registerbtn.place(x=15,y=360,width=160)
        
        
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
        
        #----LOGIN=======
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required",parent=self.root)
        elif self.txtuser.get()=="nikki" and self.txtpass.get()=="1234":
            messagebox.showinfo("Success","Welcome to Face Recognition based Attendance System",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="nkundu@922",database="face_recognizer")
            mycursor=conn.cursor()
            mycursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                open_main=messagebox.askyesno("YesNo","Are you an Admin?")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_recognition_sys(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            
            
#===================reset password=================================
    def reset_password(self):
        if self.combo_sec_Q.get()=="Select":
            messagebox.showerror("Error","Select the security Question",parent=self.root2)
        elif self.sec_ans_entry.get()=="":
            messagebox.showerror("Error","please enter the answer",parent=self.root2)
        elif self.new_password_entry.get()=="":
            messagebox.showerror("Error","please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="nkundu@922",database="face_recognizer")
            mycursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            valu=(self.txtuser.get(),self.combo_sec_Q.get(),self.sec_ans_entry.get())
            mycursor.execute(qury,valu)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.new_password_entry.get(),self.txtuser.get())
                mycursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset successfully,login using new password",parent=self.root2)
                self.root2.destroy()
            
        
            
#===================forget password============================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="nkundu@922",database="face_recognizer")
            mycursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            #print(row)
            
            if row==None:
                messagebox.showerror("Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root.title("Forgot password")
                self.root2.geometry("440x470+450+120")
                
                l=Label(self.root2,text="Forget password",font=("times new roman",18,"bold"),fg="white",bg="red")
                l.place(x=0,y=0,relwidth=1)  
                
                sec_Que=Label(self.root2,text="Select Security Question",font=("times new roman",16,"bold"),fg="black",bg="white")
                sec_Que.place(x=50,y=50)

                self.combo_sec_Q=ttk.Combobox(self.root2,font=("times new roman",16,"bold"),state="readonly")
                self.combo_sec_Q["values"]=("Select","Your Birth Place","Your Best Friend","Your School Name","Your Pet Name")
                
                self.combo_sec_Q.place(x=50,y=95,width=250)
                self.combo_sec_Q.current(0)

                self.sec_ans=Label(self.root2,text="Security Answer",font=("times new roman",16,"bold"),fg="black",bg="white")
                self.sec_ans.place(x=50,y=140)
                
                self.sec_ans_entry=ttk.Entry(self.root2,font=("times new roman",16,"bold"))
                self.sec_ans_entry.place(x=50,y=185,width=250)  
                
                self.new_password=Label(self.root2,text="Enter New Password",font=("times new roman",16,"bold"),fg="black",bg="white")
                self.new_password.place(x=50,y=230)
                self.new_password_entry=ttk.Entry(self.root2,font=("times new roman",16,"bold"))
                self.new_password_entry.place(x=50,y=275,width=250)  
                
                btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",14,"bold"),fg="black",bg="pink")
                btn.place(x=115,y=320,width=123)
        
#=======================Register class===========================================
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1280x700+0+0")
        
        
        #=========variables==========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        
        #img1bg
        img1 = Image.open("college_img/bgr.jpg")
        img1 = img1.resize((1280,700), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)  
        bg_lbl=Label(self.root,image=self.photoImg1)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        #img2 left
        img2 = Image.open("college_img/reg.png")
        img2 = img2.resize((370,500), Image.ANTIALIAS)
        self.photoImg2 = ImageTk.PhotoImage(img2)  
        bg_lbl=Label(self.root,image=self.photoImg2)
        bg_lbl.place(x=40,y=80,width=370,height=520)
        
        #main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=430,y=80,width=750,height=520)
        
        #reg label
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)
        
        
        #labels and entries
        fname=Label(frame,text="First Name",font=("times new roman",16,"bold"),fg="black",bg="white")
        fname.place(x=40,y=80)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",16,"bold"))
        fname_entry.place(x=43,y=110,width=250)
        
        lname=Label(frame,text="Last Name",font=("times new roman",16,"bold"),fg="black",bg="white")
        lname.place(x=390,y=80)
    
        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",16,"bold"))
        lname_entry.place(x=393,y=110,width=250)
        
        contact=Label(frame,text="Contact No.",font=("times new roman",16,"bold"),fg="black",bg="white")
        contact.place(x=40,y=150)
        
        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",16,"bold"))
        contact_entry.place(x=43,y=180,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",16,"bold"),fg="black",bg="white")
        email.place(x=390,y=150)
        
        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",16,"bold"))
        email_entry.place(x=393,y=180,width=250)
        
        sec_Que=Label(frame,text="Select Security Question",font=("times new roman",16,"bold"),fg="black",bg="white")
        sec_Que.place(x=40,y=220)
        
        self.combo_sec_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",16,"bold"),state="readonly")
        self.combo_sec_Q["values"]=("Select","Your Birth Place","Your Best Friend","Your School Name","Your Pet Name")
        self.combo_sec_Q.place(x=40,y=250,width=250)
        self.combo_sec_Q.current(0)
        
        sec_ans=Label(frame,text="Security Answer",font=("times new roman",16,"bold"),fg="black",bg="white")
        sec_ans.place(x=390,y=220)
        
        sec_ans_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",16,"bold"))
        sec_ans_entry.place(x=393,y=250,width=250)
        
        passw=Label(frame,text="Password",font=("times new roman",16,"bold"),fg="black",bg="white")
        passw.place(x=40,y=290)
        
        passw_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",16,"bold"))
        passw_entry.place(x=43,y=320,width=250)
        
        cnf_pass=Label(frame,text="Confirm Password",font=("times new roman",16,"bold"),fg="black",bg="white")
        cnf_pass.place(x=390,y=290)
        
        cnf_pass_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",16,"bold"))
        cnf_pass_entry.place(x=393,y=320,width=250)
        
        
        #=======checkbutton===========
        self.var_check_button=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check_button,text="I Agree To The Terms & Conditions",font=("times new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=40,y=360)
        
        #-------buttons-------
        immg=Image.open("college_img/untitled.png")
        immg.resize((200,40),Image.ANTIALIAS)
        self.photoImg=ImageTk.PhotoImage(immg)
        b1=Button(frame,image=self.photoImg,borderwidth=0,command=self.register_data,cursor="hand2")
        b1.place(x=40,y=400,width=200,height=40)
        
        
        #==========register=========
        imglg=Image.open("college_img/lgn.png")
        imglg=imglg.resize((150,38),Image.ANTIALIAS)
        self.photoimagelg=ImageTk.PhotoImage(imglg)
        b1=Button(frame,image=self.photoimagelg,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=250,y=400,width=150)
        
        #=====FUNCTION============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error"," Both passwords must be same",parent=self.root)
        elif self.var_check_button.get()==0:
            messagebox.showerror("Error","Please agree the Terms and Conditions",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="nkundu@922",database="face_recognizer")
            mycursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exists,Try another Email",parent=self.root)
            else:
                mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get(),
                    
                                                                                    ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registered Successfully",parent=self.root)


    def return_login(self):
        self.root.destroy()











if __name__=="__main__":
    main()
    