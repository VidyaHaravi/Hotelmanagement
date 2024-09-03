from tkinter import *
from customer import Cust_window
from room import RoomBooking
class hotel:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel management")
        self.root.geometry("1550x800+0+0")
        self.l1=Label(self.root,text="Hotel Management System",font=("times new roman",45,"bold"),bd=5,relief=RIDGE,bg="black",fg="white")
        self.l1.place(x=0,y=50,width=1530,height=80)

        #_____inner frame_______
        self.frame1 = Frame(self.root,bd=10,relief=SUNKEN)
        self.frame1.place(x=0,y=130,width=1530,height=670)

        #______Menu_______
        self.l2=Label(self.frame1,text="Menu",font=("times new roman",20,"bold"),bd=3,bg="black",fg="white")
        self.l2.place(x=0,y=5,width=230)

        #_____Menu frame_____
        self.frame2 = Frame(self.frame1,bd=10,relief=RIDGE)
        self.frame2.place(x=0,y=45,width=230,height=230)

        #____Button_____
        self.cust1=Button(self.frame2,text="Customer",command=self.cust1_details,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,bg="black",fg="white",width=18,cursor="hand1")
        self.cust1.grid(row=0,column=1,pady=10)

        self.room1=Button(self.frame2,text="Room",command=self.room_details,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,bg="black",fg="white",width=18,cursor="hand1")
        self.room1.grid(row=1,column=1,pady=10)

        

        self.logout1=Button(self.frame2,text="Log out",command=self.Logout,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,bg="black",fg="white",width=18,cursor="hand1")
        self.logout1.grid(row=3,column=1,pady=10)


    def cust1_details(self):
        self.cust_win=Toplevel(self.root)
        self.frame3=Cust_window(self.cust_win)
        
        
    def room_details(self):
        self.room_win=Toplevel(self.root)
        self.frame4=RoomBooking(self.room_win)
        
    def Logout(self):
        self.root.destroy()









def main():
    root=Tk()
    obj=hotel(root)
    root.mainloop()

main()