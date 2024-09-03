from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import mysql.connector



class Cust_window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x670+250+180")

    #_______inner frame_______
        self.cust_label=Label(self.root,text="Customer Details",font=("times new roman",20,"bold"),bd=3,relief=RIDGE,bg="black",fg="white")
        self.cust_label.place(x=0,y=0,width=1250)

    #______label frame________
        self.lframe=LabelFrame(self.root,text="customer entry",font=("times new roman",12,"normal"),bd=3,relief=RIDGE)
        self.lframe.place(x=0,y=40,width=350,height=580)

    #_____Customer entry______
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        self.var_name=StringVar()
        self.var_phn=StringVar()
        self.var_add=StringVar()
        self.var_gen=StringVar()
        
        self.cid=Label(self.lframe,text="Customer id",font=("times new roman",16,"normal"),padx=2,pady=4)
        self.cid.grid(row=0,column=0)

        self.cid2=ttk.Entry(self.lframe,textvariable=self.var_ref,font=("times new roman",16,"normal"),state="readonly")
        self.cid2.grid(row=0,column=1)

        self.cname=Label(self.lframe,text="Name",font=("times new roman",16,"normal"),padx=2,pady=4)
        self.cname.grid(row=1,column=0)

        self.cname1=ttk.Entry(self.lframe,textvariable=self.var_name,font=("times new roman",16,"normal"))
        self.cname1.grid(row=1,column=1)

        self.cph=Label(self.lframe,text="Phone no.",font=("times new roman",16,"normal"),padx=2,pady=4)
        self.cph.grid(row=2,column=0)

        self.cph1=ttk.Entry(self.lframe,textvariable=self.var_phn,font=("times new roman",16,"normal"))
        self.cph1.grid(row=2,column=1)

        self.cadd=Label(self.lframe,text="Address",font=("times new roman",16,"normal"),padx=2,pady=4)
        self.cadd.grid(row=3,column=0)

        self.cadd1=ttk.Entry(self.lframe,textvariable=self.var_add,font=("times new roman",16,"normal"))
        self.cadd1.grid(row=3,column=1)

        self.cgen=Label(self.lframe,text="Gender",font=("times new roman",16,"normal"),padx=2,pady=4)
        self.cgen.grid(row=4,column=0)

        self.cgen1=ttk.Entry(self.lframe,textvariable=self.var_gen,font=("times new roman",16,"normal"))
        self.cgen1.grid(row=4,column=1)

        #________button_______

        self.btn1=Frame(self.lframe,bd=5,relief=RIDGE)
        self.btn1.place(x=0,y=300,width=350,height=50)

        self.btnadd=Button(self.btn1,text='Add',command=self.add_data,font=("times new roman",18,"normal"),bd=3,bg='black',fg="white",height=1,padx=3)
        self.btnadd.grid(row=0,column=0)

        self.btnupdate=Button(self.btn1,text='Update',command=self.update,font=("times new roman",18,"normal"),bd=3,bg='black',fg="white",height=1,padx=3)
        self.btnupdate.grid(row=0,column=1)

        self.btnreset=Button(self.btn1,text='Reset',command=self.Reset,font=("times new roman",18,"normal"),bd=3,bg='black',fg="white",height=1,padx=3)
        self.btnreset.grid(row=0,column=2)

        self.btndelete=Button(self.btn1,text='Delete',command=self.mdelete,font=("times new roman",18,"normal"),bd=3,bg='black',fg="white",height=1,padx=7)
        self.btndelete.grid(row=0,column=3)

        #_______-customer details frame_______

        self.lframe1=LabelFrame(self.root,text="customer table",font=("times new roman",12,"normal"),bd=3,relief=RIDGE)
        self.lframe1.place(x=360,y=40,width=950,height=580)

        self.csrc=Label(self.lframe1,text="Search By customer id :",font=("times new roman",16,"normal"),padx=3,pady=3,bg='red')
        self.csrc.grid(row=0,column=0)
        
        self.reference=StringVar()

        self.csrc1=ttk.Entry(self.lframe1,textvariable=self.reference,font=("times new roman",16,"normal"))
        self.csrc1.grid(row=0,column=1)
        self.btndelete=Button(self.lframe1,text='Search',command=self.Search,font=("times new roman",14,"normal"),bd=3,bg='black',fg="white",height=1,padx=7)
        self.btndelete.grid(row=0,column=2)
        
        self.btndelete=Button(self.lframe1,text='Show all',command=self.fetch_data,font=("times new roman",14,"normal"),bd=3,bg='black',fg="white",height=1,padx=7)
        self.btndelete.grid(row=0,column=3)
        
        #______show table_________
        table_frame=Frame(self.lframe1,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=50,width=860,height=500)
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.cust_details=ttk.Treeview(table_frame,columns=("cid2","cname1","cph1","cadd1","cgen1"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.cust_details.xview)
        scroll_y.config(command=self.cust_details.yview)
        self.cust_details.heading("cid2",text="Reference No")
        self.cust_details.heading("cname1",text="Customer Name")
        self.cust_details.heading("cph1",text="Phone No")
        self.cust_details.heading("cadd1",text="Address")
        self.cust_details.heading("cgen1",text="Gender")
        self.cust_details["show"]="headings"
        self.cust_details.pack(fill=BOTH,expand=1)
        self.cust_details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()        
        
    def add_data(self):
        if(self.var_name.get()=="" or self.var_phn.get()==""):
            messagebox.showerror("error","All fields must be filled",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='W@2915djkq#',database='hotelmanagement')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into Customer values(%s,%s,%s,%s,%s)",(
                    self.var_ref.get(),
                    self.var_name.get(),
                    self.var_phn.get(),
                    self.var_add.get(),
                    self.var_gen.get()
                ))
                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es :
                messagebox.showwarning("Warning",f"Something went wrong :{str(es)}",parent=self.root)
    
    def fetch_data(self): 
        conn = mysql.connector.connect(host='localhost',username='root',password='W@2915djkq#',database='hotelmanagement')
        my_cursor=conn.cursor() 
        my_cursor.execute("select * from Customer")  
        rows = my_cursor.fetchall()
        if len(rows)!=0 :
            self.cust_details.delete(*self.cust_details.get_children())
            for i in rows:
                self.cust_details.insert("",END,values=i)
            conn.commit()
            conn.close()    
            
                        
    def get_cursor(self,event):
        cursor_row=self.cust_details.focus()
        content=self.cust_details.item(cursor_row)
        row = content["values"]
        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_phn.set(row[2]),
        self.var_add.set(row[3]),
        self.var_gen.set(row[4])
        
    
    def update(self):
        if self.var_phn=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost',username='root',password='W@2915djkq#',database='hotelmanagement')
            my_cursor=conn.cursor() 
            my_cursor.execute("update Customer set Name=%s,phoneno=%s,address=%s,gender=%s where Ref=%s",(
                    
                    self.var_name.get(),
                    self.var_phn.get(),
                    self.var_add.get(),
                    self.var_gen.get(),
                    self.var_ref.get()
                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details updated successfully",parent=self.root)
        
                    

    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel management system","Do you want delete this customer",parent=self.root)
        if mdelete>0:   
            conn = mysql.connector.connect(host='localhost',username='root',password='W@2915djkq#',database='hotelmanagement')
            my_cursor=conn.cursor() 
            my_cursor.execute("delete from Customer where Ref=%s",(self.var_ref.get(),))
        else :
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()  
        
        
    def Reset(self):
        self.var_ref.set(""),
        self.var_name.set(""),
        self.var_phn.set(""),
        self.var_add.set(""),
        self.var_gen.set("")
             
    
    def Search(self):
        conn = mysql.connector.connect(host='localhost',username='root',password='W@2915djkq#',database='hotelmanagement')
        my_cursor=conn.cursor() 
        my_cursor.execute("select * from Customer where Ref=%s",(int(self.reference.get()),))
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.cust_details.delete(*self.cust_details.get_children())
            for i in row:
                self.cust_details.insert("",END,values=i)
            conn.commit()
        conn.close()
            
        

def main():
    root=Tk()
    obj1=Cust_window(root)
    root.mainloop()
    
#main()
