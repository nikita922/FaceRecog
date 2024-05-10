import re
import string
from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from numpy import imag, true_divide
from time import strftime
from datetime import datetime
import os
import numpy as np
#42:50
from Student import Student

class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1270x700+0+0")
        self.root.title("Face recognition system")

        title_label = Label(self.root,text="FACE RECOGNITION",font=("times new roman",30,"bold"),bg="greenyellow",fg="black")
        title_label.place(x=0,y=0,width=1280,height=40)

        #img1
        img_top=Image.open(r"college_img\reecog.jpg")
        img_top=img_top.resize((630,640),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl3=Label(self.root,image=self.photoimg_top)
        f_lbl3.place(x=2,y=40,width=630,height=640)

        #img2
        img_top2=Image.open(r"college_img\reecog3.jpg")
        img_top2=img_top2.resize((640,640),Image.ANTIALIAS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl2=Label(self.root,image=self.photoimg_top2)
        f_lbl2.place(x=633,y=40,width=640,height=640)

        #button
        b2 = Button(f_lbl2,text="FACE RECOGNITION",command=self.face_recog,cursor="hand2",font=("times new roman",26,"bold"),bg="midnightblue",fg="white")
        b2.place(x=28,y=488,width=600,height=120)


    #attendance=================
    def mark_attendance(self,i,r,n,d):
        with open("Attend.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                
            
        

    #=============FACE RECOGNITITON ===============
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,25),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="nkundu@922",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from studentt where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from studentt where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from studentt where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                my_cursor.execute("select Student_id from studentt where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                

                if confidence>77:
                    cv2.putText(img,f"ID:{r}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Department:{d}",(x,y-15),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)
                    cv2.putText(img,"Unknown face",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,25),2)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()
