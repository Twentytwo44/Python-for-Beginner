from tkinter import *
from tkinter import ttk
import csv
from datetime import datetime

GUI = Tk()
GUI.title("โปรแกรมบันทึกค่าใช้จ่าย by Twentytwo")
GUI.geometry("500x300+50+30")

#B1 = Button(GUI,text="HELLO")
#B1.pack(ipadx=50,ipady=20)

Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH, expand=1)
word1 = "Expense List"
word2 = "Add Expense"

Tab.add(T1, text="{:^20s}".format(word2))
Tab.add(T2, text="{:^20s}".format(word1))
#Tab.add(T2, text="{:^20s}".format(word1),image = -----, compound=top)

# name = PhotoImage(file="name.png")
# Logo = tkk.Label(F1,image= name)
# Logo.pack()



F1 = Frame(T1)
F1.place(x=100,y=50)

days = {"Mon":"จันทร์",
        "Tue":"อังคาร",
        "Wed":"พุธ",
        "Thu":"พฤหัสบดี",
        "Fri":"ศุกร์",
        "Sat":"เสาร์",
        "Mon":"อาทิตย์"}


def Save(event=None):
    expense = v_expense.get()
    price = v_price.get()
    volume = v_volume.get()
    ap = int(price) * int(volume)
    print("รายการ : {} {} บาท {} ชิ้น {} บาท ".format(expense,price,volume,ap) )
    v_expense.set("")
    v_price.set("")
    v_volume.set("")
    today = datetime.now().strftime("%a")
    dt = datetime.now().strftime("%Y-%m-%d-{}".format(days[today]))
    
    with open("savedata.csv","a",encoding="utf=8",newline="") as f:
        fw = csv.writer(f)
        data = [dt,expense,price,volume]
        fw.writerow(data)
    
    E1.focus()

GUI.bind("<Return>",Save)    

    
FONT1 = (None,20)



L = ttk.Label(F1,text="รายการค่าใช้จ่าย",font=FONT1).pack()
v_expense = StringVar() 
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()    



L = ttk.Label(F1,text="ราคาบาท",font=FONT1).pack()
v_price = StringVar() 
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()    



L = ttk.Label(F1,text="จำนวน",font=FONT1).pack()
v_volume = StringVar() 
E3 = ttk.Entry(F1,textvariable=v_volume,font=FONT1)
E3.pack()    


B2 = ttk.Button(F1,text="Save",command=Save)
B2.pack(ipadx=50,ipady=20)






GUI.mainloop()
