from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector





class student:


    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton system")



        #==================veriable
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_Id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_DOB=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_photo=StringVar()

   
        #   #  image first
        img=Image.open(r"C:\Users\HP\face reconice1\student2.jpg")
        img=img.resize((500, 130), Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

       
         #  image second
        img2=Image.open(r"C:\Users\HP\face reconice1\student3.jpg")
        img2=img2.resize((500, 130), Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)

        
        f_lbl=Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=130)

#          #  image third
        img3=Image.open(r"C:\Users\HP\face reconice1\student4.jpg")
        img3=img3.resize((500, 130), Image.ADAPTIVE)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=550, height=130)

#          #     # back ground
        img4=Image.open(r"C:\Users\HP\face reconice1\oist-i5.jpg")
        img4=img4.resize((1530, 710), Image.ADAPTIVE)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        title_lbl=Label(bg_img,text="student management system",font=("times new roman",35,"bold"),bg="red",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
 
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1505,height=600)
        
#         # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=750,height=580)
        
      
        img_left=Image.open(r"C:\Users\HP\face reconice1\student4.jpg")
        img_left=img_left.resize((720, 130), Image.ADAPTIVE)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)
        
        # current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="current course",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=750,height=200)
        
#         #Department

        dep_label=Label(current_course_frame,text="Department",font=("time new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)
          
        dep_combo=ttk.Combobox (current_course_frame,textvariable=self.var_dep ,font=("times new roman",12,"bold"),state="read only")
        dep_combo["value"]=("select Department","computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
#         #course
        # year_label=Label(current_course_frame,text="YEAR",font=("time new roman",12,"bold"),bg="white")
        # year_label.grid(row=1,column=0,padx=10)

        course_label=Label(current_course_frame,text="Course",font=("time new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10)
          
        course_combo=ttk.Combobox (current_course_frame,textvariable=self.var_course, font=("times new roman",12,"bold"),state="randomly")
        course_combo["value"]=("select course","B.TECH","PHARMECY","law","B.A")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
          
#         #Year
        year_label=Label(current_course_frame,text="YEAR",font=("time new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)
          
        year_combo=ttk.Combobox (current_course_frame, textvariable=self.var_year,font=("times new roman",12,"bold"),state="randomly")
        year_combo["value"]=("select YEAR","FIRST YEAR","2nd YEAR","3rd YEAR","4th YEAR")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

#         #semester
        semester_label=Label(current_course_frame,text="SEMESTER",font=("time new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10)
          
        semester_combo=ttk.Combobox (current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="randomly")
        semester_combo["value"]=("select semester"," 1st sem"," 2nd sem","3rd sem "," 4th sem"," 5th sem"," 6th sem","7th sem "," 8th sem")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

#         #class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="class student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=260,width=750,height=400)
        
# ###


# # student id
        studentId_label=Label(class_student_frame,text="StudentId",font=("time new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_Id,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady =5,sticky=W)


# # student names
        studentname_label=Label(class_student_frame,text="Student Name",font=("time new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady =5,sticky=W)

# # class didvision

        class_div_label=Label(class_student_frame,text="Class Didvision",font=("time new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady =5,sticky=W)

       

# # roll no
        roll_no_label=Label(class_student_frame,text="Roll No",font=("time new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady =5,sticky=W)

# gender 
        gender_label=Label(class_student_frame,text="Gender",font=("time new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady =5,sticky=W)

       

# DOB
        dob_label=Label(class_student_frame,text="Date Of Birth",font=("time new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_DOB,width=20,font=("times new roman",13,"bold"))
        dob_no_entry.grid(row=2,column=3,padx=10,pady =5,sticky=W)

# email
        email_label=Label(class_student_frame,text="emailId",font=("time new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady =5,sticky=W)

# phone no
        phone_label=Label(class_student_frame,text="Phone No",font=("time new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady =5,sticky=W)

# address
        address_label=Label(class_student_frame,text="Address",font=("time new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady =5,sticky=W)

# teacher name
        teac_label=Label(class_student_frame,text="Teacher Name",font=("time new roman",12,"bold"),bg="white")
        teac_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teac_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teac_entry.grid(row=4,column=3,padx=10,pady =5,sticky=W)

        # Reft label frame
        # self.var_radio1=StringVar()
        # left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student details",font=("time new roman",12,"bold"))
        # left_frame.place(x=770,y=10,width=725,height=580)
   
#     ######
#     #Radio button
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take photo sample",value="yes")
        radionbtn1.grid(row=6,column=0)
        


        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="no")
        radionbtn2.grid(row=6,column=1)
# # buttonframe
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=743,height=70)

        save_btn=Button(btn_frame,text="save",command=self.add_data,width=18,font=("time new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0 ) 

        save_btn=Button(btn_frame,text="update",width=17,font=("time new roman",13,"bold"),bg="pink",fg="black")
        save_btn.grid(row=0,column=1 ) 

        save_btn=Button(btn_frame,text="delete",width=18,font=("time new roman",13,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=2) 

        save_btn=Button(btn_frame,text="reset",width=17,font=("time new roman",13,"bold"),bg="red",fg="black")
        save_btn.grid(row=0,column=3) 

#take a photo semple

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=743,height=35)



        take_photo_btn=Button(btn_frame1,text="take photo semple",width=38  ,font=("time new roman",13,"bold"),bg="green",fg="black")
        take_photo_btn.grid(row=0,column=0 ) 

#update photo
        update_photo_btn=Button(btn_frame1,text="take photo semple",width=40,font=("time new roman",13,"bold"),bg="yellow",fg="black")
        update_photo_btn.grid(row=0,column=1 ) 

# # right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        img_right=Image.open(r"C:\Users\HP\face reconice1\oist-i5.jpg")
        img_right=img_right.resize((720, 130), Image.ADAPTIVE)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

#         #==============search system============#

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="search system",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(search_frame,text="search by:",font=("time new roman",15,"bold"),bg="red")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox (search_frame, font=("times new roman",13,"bold"),state="randomly", width=13)
        search_combo["value"]=("select "," roll no"," phone no",)
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady =5,sticky=W)

        search_btn=Button(search_frame,text="delete",width=10,font=("time new roman",13,"bold"),bg="green",fg="white")
        search_btn.grid(row=0,column=3) 

        showall_btn=Button(search_frame,text="reset",width=10,font=("time new roman",13,"bold"),bg="red",fg="black")
        showall_btn.grid(row=0,column=4) 

# # ###############table frame#################


      

        table_frame=Frame (right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5,y=210, width=710,height=350)

       
        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar (table_frame, orient=VERTICAL)

        self.student_table=ttk. Treeview(table_frame, column=("dep","course","year","sem","Id","name","div","roll no","gander","DOB","email","phone no","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X) 
        scroll_y.pack(side=RIGHT,fill=Y)
        # for doing scrollbar in table

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")

        self.student_table.heading("course", text="Course")

        self.student_table.heading("year", text="Year")

        self.student_table.heading("sem", text="Semester")

        self.student_table.heading("Id", text="StudentId")

        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")

        self.student_table.heading("roll no", text="roll no")
        self.student_table.heading("gander", text="gander")
        # self.student_table.heading("div", text="Division")

        self.student_table.heading("DOB", text="DOB")

        self.student_table.heading("email", text="Email")
        # changing here

        self.student_table.heading("phone no", text="phone")

       # changing here
        self.student_table.heading("address", text="Address")

        self.student_table.heading("teacher", text="Teacher")

        self.student_table.heading("photo", text="photosamplestatus")

        self.student_table["show"]="headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100) 
        self.student_table.column("sem", width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll no", width=100)
        self.student_table.column("gander", width=100)
       
        self.student_table.column("DOB",width=100) 
        self.student_table.column("email", width=100)
        self.student_table.column("phone no", width=100 )
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

       # ==================function decleratio
    def add_data(self): 
        if self.var_dep.get()=="select Department" or self.var_std_name.get()==" "or self.var_std_Id.get()==" ":
           messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
                                                                                                                     
                                                                                                          
          try:
                conn=mysql.connector.connect(host="localhost",username="root",password="vikash@123",database="facereconise")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_Id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_DOB.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_photo.get(),
                                                                                
                                                                                                   ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success"," Vikash sir,student details has been recorded successfully",parent=self.root)
          except Exception as es:
             messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


#==========fetch data============
    def fetch_data(self):
     conn=mysql.connector.connect(host="localhost",username="root",password="vikash@123",database="facereconise")
     my_cursor=conn.cursor()
     my_cursor.execute("select*from student")
     data=my_cursor.fetchall()

     if len(data)!=0:
      self.student_table.delete(*self.student_table.get_children())
      for i in data:
       self.student_table.insert("",END,values=i)
      conn.commit()
      conn.close()


# =========get cursor=======
    def get_cursor(self,event=""):
       cursor_focus=self.student_table.focus()
       content=self.student_table.item(cursor_focus)
       data=content["values"]

       self.var_dep.set(data[0])
       self.var_year.set(data[1])
       self.var_course.set(data[2])
       self.var_semester.set(data[3])
       self.var_std_Id.set(data[4])
       self.var_std_name.set(data[5])
       self.var_div.set(data[6])
       self.var_roll.set(data[7])
       self.var_gender.set(data[8])
       self.var_DOB.set(data[9])
       self.var_email.set(data[10])
       self.var_photo.set(data[11])
       self.var_address.set(data[12])
       self.var_teacher.set(data[13]) 
       self.var_radio1.set(data[14])
#       update function
    def update_data(self):
      if self.var_dep.get()=="select Department" or self.var_std_name.get()==" "or self.var_std_Id.get()==" ":
           messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
           try:
              upadate=messagebox.askyesno("upadate","do u want to update this student details",parent=self.root)
              if upadate>0:
                 conn=mysql.connector.connect(host="localhost",username="root",password="vikash@123",database="facereconise")
                 my_cursor=conn.cursor()
                 my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,teacher=%s,photosample=%s where student_id=%s",(
                    

                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_DOB.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_std_Id.get()
    
                 ))
              else:
                  if not upadate:
                    return
                  messagebox.showinfo("success","student details successfully update completed",parent=self.root)
                  conn.commit()
                  self.fetch_data()
                  conn.close()
           except Exception as es:
              messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
              
     
              



 





 
 
if __name__=="__main__":
   root=Tk()   
   obj=student(root)
   root.mainloop()
     
      