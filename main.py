from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import student


class face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton system")

        #  image first
        img=Image.open(r"C:\Users\HP\face reconice1\images(2).jpg")
        img=img.resize((500, 130), Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

       
#          #  image second
        img2=Image.open(r"C:\Users\HP\face reconice1\facialrecognition.webp")
        img2=img2.resize((500, 130), Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)

        
        f_lbl=Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=130)

         #  image third
        img3=Image.open(r"C:\Users\HP\face reconice1\images(2).jpg")
        img3=img3.resize((500, 130), Image.ADAPTIVE)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=550, height=130)

#     #     # back ground
        img4=Image.open(r"C:\Users\HP\face reconice1\oist-i5.jpg")
        img4=img4.resize((1530, 710), Image.ADAPTIVE)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        title_lbl=Label(bg_img,text="VIKASH FACE RECOGNITION ATTANDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
       
#     #     # student butten
        img5=Image.open(r"C:\Users\HP\face reconice1\vikashimag.jpeg")
        img5=img5.resize((220, 220), Image.ADAPTIVE)
        self.photoimg5=ImageTk.PhotoImage(img5)
         
        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2") 
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="student details",command=self.student_details,cursor="hand2",font=("times new roman",25,"bold"),bg="white",fg="green") 
        b1_1.place(x=200,y=300,width=220,height=40)

    #     # detect face
        img6=Image.open(r"C:\Users\HP\face reconice1\download.jpg")
        img6=img6.resize((220, 220), Image.ADAPTIVE)
        self.photoimg6=ImageTk.PhotoImage(img6)
         
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2") 
        b1.place(x=500,y=100,width=220,height=220)
        
        b1=Button(bg_img,text="face dector",cursor="hand2",font=("times new roman",25,"bold"),bg="white",fg="brown") 
        b1.place(x=500,y=300,width=220,height=40)
        
    # #     # attandance
        img7=Image.open(r"C:\Users\HP\face reconice1\attandance.jpg")
        img7=img7.resize((220, 220), Image.ADAPTIVE)
        self.photoimg7=ImageTk.PhotoImage(img7)
         
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2") 
        b1.place(x=800,y=100,width=220,height=220)
        
        b1=Button(bg_img,text="attandance",cursor="hand2",font=("times new roman",25,"bold"),bg="white",fg="orange") 
        b1.place(x=800,y=300,width=220,height=40)
      
    #     # help face button
        img8=Image.open(r"C:\Users\HP\face reconice1\help.jpg")
        img8=img8.resize((220, 220), Image.ADAPTIVE)
        self.photoimg8=ImageTk.PhotoImage(img8)
         
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2") 
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1=Button(bg_img,text="Help desk",cursor="hand2",font=("times new roman",25,"bold"),bg="white",fg="black") 
        b1.place(x=1100,y=300,width=220,height=40)
        
    #     #  train data 
        img9=Image.open(r"C:\Users\HP\face reconice1\trainimage.jpg")
        img9=img9.resize((220, 220), Image.ADAPTIVE)
        self.photoimg9=ImageTk.PhotoImage(img9)
         
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2") 
        b1.place(x=200,y=380,width=220,height=220)
        
        b1=Button(bg_img,text="train data ",cursor="hand2",font=("times new roman",25,"bold"),bg="white",fg="purple") 
        b1.place(x=200,y=580,width=220,height=40)

    # #   photo face button
        img10=Image.open(r"C:\Users\HP\face reconice1\facebutton.jpg")
        img10=img10.resize((220, 220), Image.ADAPTIVE)
        self.photoimg10=ImageTk.PhotoImage(img10)
         
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2") 
        b1.place(x=500,y=380,width=220,height=220)
        
        b1=Button(bg_img,text=" Photos",cursor="hand2",font=("times new roman",25,"bold"),bg="white",fg="green") 
        b1.place(x=500,y=580,width=220,height=40)

    #    # develepor
        img11=Image.open(r"C:\Users\HP\face reconice1\developer.jpg")
        img11=img11.resize((220, 220), Image.ADAPTIVE)
        self.photoimg11=ImageTk.PhotoImage(img11)
         
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2") 
        b1.place(x=800,y=380,width=220,height=220)
        
        b1=Button(bg_img,text="Developer ",cursor="hand2",font=("times new roman",25,"bold"),bg="white",fg="blue") 
        b1.place(x=800,y=580,width=220,height=40)
 
    #     # exit
        img12=Image.open(r"C:\Users\HP\face reconice1\exit.jpg")
        img12=img12.resize((220, 220), Image.ADAPTIVE)
        self.photoimg12=ImageTk.PhotoImage(img12)
         
        b1=Button(bg_img,image=self.photoimg12,cursor="hand2") 
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1=Button(bg_img,text="Exit ",cursor="hand2",font=("times new roman",25,"bold"),bg="white",fg="red") 
        b1.place(x=1100,y=580,width=220,height=40)
 
#    #================================function button========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)












if __name__=="__main__":
    root=Tk()
    obj=face_Recognition_system(root)
    root.mainloop()
    
        