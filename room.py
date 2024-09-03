from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from time import strftime
from datetime import datetime
import mysql.connector


class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management system")
        self.root.geometry("1250x670+250+180") 
        
        #_____Inner Frame______
        self.cust_label=Label(self.root,text="Room Booking",font=("times new roman",20,"bold"),bd=3,relief=RIDGE,bg="black",fg="white")
        self.cust_label.place(x=0,y=0,width=1250)
        
        self.lframe=LabelFrame(self.root,text="Room entry",font=("times new roman",12,"normal"),bd=3,relief=RIDGE)
        self.lframe.place(x=0,y=40,width=400,height=580)
        
        #______room entry_______
        
        self.var_contact=StringVar()
        self.var_indate=StringVar()
        self.var_outdate=StringVar()
        self.var_roomtype=StringVar()
        self.var_albroom=StringVar()
        self.var_num=StringVar()
        self.var_cost=StringVar()
        
        
        self.cust_contact=Label(self.lframe,text="Customer reference",font=("times new roman",16,"normal"),padx=2,pady=4)
        self.cust_contact.grid(row=0,column=0)

        self.cust_contact1=ttk.Entry(self.lframe,textvariable=self.var_contact,font=("times new roman",16,"normal"),width=10)
        self.cust_contact1.grid(row=0,column=1,sticky=W)
        
        self.in_date=Label(self.lframe,text="Check in Date",font=("times new roman",16,"normal"),padx=2,pady=4)
        self.in_date.grid(row=1,column=0)

        self.in_date1=ttk.Entry(self.lframe,textvariable=self.var_indate,font=("times new roman",16,"normal"),width=19)
        self.in_date1.grid(row=1,column=1)
        
        self.out_date=Label(self.lframe,text="Check out Date",font=("times new roman",16,"normal"),padx=2,pady=4)
        self.out_date.grid(row=2,column=0)

        self.out_date1=ttk.Entry(self.lframe,textvariable=self.var_outdate,font=("times new roman",16,"normal"),width=19)
        self.out_date1.grid(row=2,column=1)
        
        self.room_type=Label(self.lframe,text="Room Type:",font=("times new roman",16,"normal"),padx=2,pady=4)
        self.room_type.grid(row=3,column=0)
        
        self.room_type1=ttk.Combobox(self.lframe,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=19)
        self.room_type1["value"]=("Single","Double","Luxury")
        self.room_type1.current(0)
        self.room_type1.grid(row=3,column=1,sticky=W)
        
        self.available_room1=Label(self.lframe,text="Room no:",font=("times new roman",16,"normal"),padx=2,pady=4)
        self.available_room1.grid(row=4,column=0)
        
        self.available_room=ttk.Entry(self.lframe,textvariable=self.var_albroom,font=("times new roman",16,"normal"),width=19)
        self.available_room.grid(row=4,column=1)
        
        self.num_days=Label(self.lframe,text="Num of days:",font=("times new roman",16,"normal"),padx=2,pady=4)
        self.num_days.grid(row=5,column=0)
        
        self.num_days1=ttk.Entry(self.lframe,textvariable=self.var_num,font=("times new roman",16,"normal"),width=19)
        self.num_days1.grid(row=5,column=1)
        
        self.cost=Label(self.lframe,text="Cost:",font=("times new roman",16,"normal"),padx=2,pady=4)
        self.cost.grid(row=6,column=0)
        
        self.cost1=ttk.Entry(self.lframe,textvariable=self.var_cost,font=("times new roman",16,"normal"),width=19)
        self.cost1.grid(row=6,column=1)
        
        self.fetch_btn=Button(self.lframe,text='fetch details',command=self.fetch_data,font=("times new roman",12,"normal"),bd=3,bg='black',fg="white",height=1)
        self.fetch_btn.place(x=320,y=4)
        
        self.btnadd=Button(self.lframe,text='Bill', command=self.total,font=("times new roman",15,"normal"),bd=3,bg='black',fg="white",height=1,padx=3,width=15)
        self.btnadd.grid(row=7,column=0,sticky=W)
        
        
        #__________butttons_______________
        self.btn1=Frame(self.lframe,bd=5,relief=RIDGE)
        self.btn1.place(x=0,y=300,width=350,height=50)

        self.btnadd=Button(self.btn1,text='Add',command=self.add_data,font=("times new roman",18,"normal"),bd=3,bg='black',fg="white",height=1,padx=3)
        self.btnadd.grid(row=0,column=0)

        self.btnupdate=Button(self.btn1,text='Update',command=self.update, font=("times new roman",18,"normal"),bd=3,bg='black',fg="white",height=1,padx=3)
        self.btnupdate.grid(row=0,column=1)

        self.btnreset=Button(self.btn1,text='Reset',command=self.Reset,font=("times new roman",18,"normal"),bd=3,bg='black',fg="white",height=1,padx=3)
        self.btnreset.grid(row=0,column=2)

        self.btndelete=Button(self.btn1,text='Delete',command=self.mdelete, font=("times new roman",18,"normal"),bd=3,bg='black',fg="white",height=1,padx=7)
        self.btndelete.grid(row=0,column=3)
        
        #__________Room data table___________
        
        self.lframe1=LabelFrame(self.root,text="Room table",font=("times new roman",12,"normal"),bd=3,relief=RIDGE)
        self.lframe1.place(x=400,y=250,width=900,height=580)

        self.csrc=Label(self.lframe1,text="Search By customer contact:",font=("times new roman",16,"normal"),padx=3,pady=3,bg='red')
        self.csrc.grid(row=0,column=0)
        
        self.contact=StringVar()

        self.csrc1=ttk.Entry(self.lframe1,textvariable=self.contact,font=("times new roman",16,"normal"))
        self.csrc1.grid(row=0,column=1)
        self.btndelete=Button(self.lframe1,text='Search',font=("times new roman",14,"normal"),bd=3,bg='black',fg="white",height=1,padx=7)
        self.btndelete.grid(row=0,column=2)
        
        self.btndelete=Button(self.lframe1,text='Show all',font=("times new roman",14,"normal"),bd=3,bg='black',fg="white",height=1,padx=7)
        self.btndelete.grid(row=0,column=3)
        
        
        #_______show table data__________
        
        table_frame=Frame(self.lframe1,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=40,width=800,height=250)
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.room_details=ttk.Treeview(table_frame,columns=("cust_contact1","in_date1","out_date1","room_type1","available_room","num_days1","cost"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_details.xview)
        scroll_y.config(command=self.room_details.yview)
        self.room_details.heading("cust_contact1",text="Customer Reference")
        self.room_details.heading("in_date1",text="Check in date")
        self.room_details.heading("out_date1",text="Check out date")
        self.room_details.heading("room_type1",text="Room Type")
        self.room_details.heading("available_room",text="Room no")
        self.room_details.heading("num_days1",text="Number of days")
        self.room_details.heading("cost",text="Total Cost")
        
        
        self.room_details["show"]="headings"
        self.room_details.pack(fill=BOTH,expand=1)
        self.room_details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data1()
        
    def fetch_data(self): 
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter reference number",parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost',username='root',password='W@2915djkq#',database='hotelmanagement')
            my_cursor=conn.cursor() 
            my_cursor.execute("select Name from Customer where Ref=%s",(self.var_contact.get(),))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","This number not found",parent=self.root) 
            else:
                conn.commit()
                conn.close()
                
                show_dataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                show_dataframe.place(x=455,y=40,width=300,height=180)
                
                labelname=Label(show_dataframe,text="Name :",font=("arial",12,"bold"))
                labelname.place(x=0,y=0)
                
                labeln=Label(show_dataframe,text=row,font=("arial",12,"bold"))
                labeln.place(x=90,y=0)  
                
                conn = mysql.connector.connect(host='localhost',username='root',password='W@2915djkq#',database='hotelmanagement')
                my_cursor=conn.cursor() 
                my_cursor.execute("select phoneno from Customer where Ref=%s",(self.var_contact.get(),))
                row=my_cursor.fetchone() 
                
                labelphn=Label(show_dataframe,text="Phone NO:",font=("arial",12,"bold"))
                labelphn.place(x=0,y=30)
                
                labeln=Label(show_dataframe,text=row,font=("arial",12,"bold"))
                labeln.place(x=90,y=30)  
                
                conn = mysql.connector.connect(host='localhost',username='root',password='W@2915djkq#',database='hotelmanagement')
                my_cursor=conn.cursor() 
                my_cursor.execute("select address from Customer where Ref=%s",(self.var_contact.get(),))
                row=my_cursor.fetchone() 
                
                labeladr=Label(show_dataframe,text="Address:",font=("arial",12,"bold"))
                labeladr.place(x=0,y=60)
                
                labeln=Label(show_dataframe,text=row,font=("arial",12,"bold"))
                labeln.place(x=90,y=60)
                
                conn = mysql.connector.connect(host='localhost',username='root',password='W@2915djkq#',database='hotelmanagement')
                my_cursor=conn.cursor() 
                my_cursor.execute("select gender from Customer where Ref=%s",(self.var_contact.get(),))
                row=my_cursor.fetchone() 
                
                labelgn=Label(show_dataframe,text="Gender:",font=("arial",12,"bold"))
                labelgn.place(x=0,y=90)
                
                labeln=Label(show_dataframe,text=row,font=("arial",12,"bold"))
                labeln.place(x=90,y=90)  
                         

     
    def add_data(self):
        if(self.var_contact.get()=="" or self.var_indate.get()==""):
            messagebox.showerror("error","All fields must be filled")
        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='W@2915djkq#',database='hotelmanagement')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s)",(
                                                                    self.var_contact.get(),
                                                                    self.var_indate.get(),
                                                                    self.var_outdate.get(),
                                                                    self.var_roomtype.get(),
                                                                    self.var_albroom.get(),
                                                                    self.var_num.get()
                ))
                conn.commit()
                self.fetch_data1()
                conn.close()
                messagebox.showinfo("Success","Customer has been added")
            except Exception as es :
                messagebox.showwarning("Warning",f"Something went wrong :{str(es)}",parent=self.root)          
        
    def fetch_data1(self): 
            conn = mysql.connector.connect(host='localhost',username='root',password='W@2915djkq#',database='hotelmanagement')
            my_cursor=conn.cursor() 
            my_cursor.execute("select * from room")  
            rows = my_cursor.fetchall()
            if len(rows)!=0 :
                self.room_details.delete(*self.room_details.get_children())
                for i in rows:
                    self.room_details.insert("",END,values=i)
                conn.commit()
            conn.close()  
            
            
    def get_cursor(self,event):
        cursor_row=self.room_details.focus()
        content=self.room_details.item(cursor_row)
        row = content["values"]
        self.var_contact.set(row[0]),
        self.var_indate.set(row[1]),
        self.var_outdate.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_albroom.set(row[4]),
        self.var_num.set(row[5]) 
         

    def update(self):
        if self.var_contact=="":
            messagebox.showerror("Error","Please enter reference number",parent=self.root)
        else:
        
                conn = mysql.connector.connect(host='localhost',username='root',password='W@2915djkq#',database='hotelmanagement')
                my_cursor=conn.cursor() 
                my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,available=%s,num_days=%s where contact=%s",(
                        
                                                                        self.var_indate.get(),
                                                                        self.var_outdate.get(),
                                                                        self.var_roomtype.get(),
                                                                        self.var_albroom.get(),
                                                                        self.var_num.get(),
                                                                        self.var_contact.get()
                                                                            
                                                                        )
                    )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update","Room details updated successfully",parent=self.root)
            
            
    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel management system","Do you want delete this customer",parent=self.root)
        if mdelete>0:   
            conn = mysql.connector.connect(host='localhost',username='root',password='W@2915djkq#',database='hotelmanagement')
            my_cursor=conn.cursor() 
            my_cursor.execute("delete from room where contact=%s",(self.var_contact.get(),))
        else :
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()  
        
    def Reset(self):
        self.var_contact.set(""),
        self.var_indate.set(""),
        self.var_outdate.set(""),
        self.var_roomtype.get(),
        self.var_albroom.set(""),
        self.var_num.set("")  
        
        
    def total(self):
        inDate=self.var_indate.get()
        outDate=self.var_outdate.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        
        self.var_num.set(abs(outDate-inDate).days)
        
        if self.var_roomtype.get()=="Single" :
            n=500*int(self.var_num.get())
            self.var_cost.set(n)
        if self.var_roomtype.get()=="Double" :
            n=750*int(self.var_num.get())
            self.var_cost.set(n)
        if self.var_roomtype.get()=="Luxury" :
            n=1000*int(self.var_num.get())
            self.var_cost.set(n)
            
    
    def Search(self):
        conn = mysql.connector.connect(host='localhost',username='root',password='W@2915djkq#',database='hotelmanagement')
        my_cursor=conn.cursor() 
        my_cursor.execute("select * from room where contact=%s",(int(self.var_contactnum.get()),))
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.cust_details.delete(*self.cust_details.get_children())
            for i in row:
                self.cust_details.insert("",END,values=i)
            conn.commit()
        conn.close()
            
            
          

        
def main():
    root=Tk()
    obj1=RoomBooking(root)
    root.mainloop()
    
    
#main()
    