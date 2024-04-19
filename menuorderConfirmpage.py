from tkinter import *

# order confirmation
def OrderConfirm():
    # Creating a new window
    new_window = Toplevel()
    new_window.geometry("900x500")
    new_window.title("MINI SYSTEM - WoWz coffee shop")
    new_window.configure(bg="#AD8E70")
    from tkinter import messagebox
    
    # Adding a label widget to display the input value
    lbl_orderConfirm = Label(new_window, text="ORDER CONFIRMATION", font=("Arial Black", 27), bg="#AD8E70", fg="white")
    lbl_orderConfirm.grid(row=0, column=1,columnspan=3,sticky="w",padx=210)

    lbl_qty = Label(new_window, text="Qty",font=("Arial Black", 20), bg="#AD8E70", fg="white")
    lbl_qty.grid(row=1, column=1,sticky="nw", padx=30)

    lbl_size = Label(new_window, text="Size", font=("Arial Black",20), bg="#AD8E70", fg="white")
    lbl_size.grid(row=1, column=1, sticky="nw", padx=120)

    lbl_name = Label(new_window, text="Name", font=("Arial Black",20), bg="#AD8E70", fg="white")
    lbl_name.grid(row=1, column=1, sticky="nw",padx=220)

    lbl_price = Label(new_window, text="Price", font=("Arial Black", 20),bg="#AD8E70", fg="white")
    lbl_price.grid(row=1, column=1, sticky="nw",padx=600)

    lbl_cancel = Label(new_window, text="Cancel", font=("Arial Black", 20),bg="#AD8E70", fg="white")
    lbl_cancel.grid(row=1, column=1, sticky="nw",padx=750)

#name 1
    def UnorderItem():
        for widget in new_window.grid_slaves():
            if int(widget.grid_info()["row"]) == 2:
                widget.destroy()

    if input_name1s.get().upper()== "M":
        Name1 = Label(new_window, text="SPANISH LATTE", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name1.grid(row=2, column=1, sticky="nw",padx=220)

        Name1price = Label(new_window, text="₱85", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name1price.grid(row=2, column=1, sticky="nw",padx=610)

        btn_name1s = Button(new_window, text="Remove", font=("Arial Black", 12), bg="#F15A59", fg="white", command=UnorderItem)
        btn_name1s.grid(row=2, column=1, sticky="nw",padx=760,pady=7)

    elif input_name1s.get().upper() == "L":
        Name1 = Label(new_window, text="SPANISH LATTE", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name1.grid(row=2, column=1, sticky="nw",padx=220)

        Name1price = Label(new_window, text="₱99", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name1price.grid(row=2, column=1, sticky="nw",padx=610)

        btn_name1s = Button(new_window, text="Remove", font=("Arial Black", 12), bg="#F15A59", fg="white", command=UnorderItem)
        btn_name1s.grid(row=2, column=1, sticky="nw",padx=760,pady=7)

    else:
        messagebox.showinfo("Error", "Please enter 'M' or 'L' for size.")
  
    if int(input_name1q.get()) > 10:
        messagebox.showerror("Error", "Please enter a quantity less than or equal to 10.")
    else:
        input_name1getQty = Label(new_window, text=input_name1q.get(), font=("Arial Black", 18), bg="#AD8E70", fg="white")
        input_name1getQty.grid(row=2, column=1, sticky="nw", padx=43)

    input_name1getSize = Label(new_window, text=input_name1s.get(), font=("Arial Black", 18), bg="#AD8E70", fg="white")
    input_name1getSize.grid(row=2, column=1, sticky="nw", padx=140)

    #name2
    def UnorderItem():
        for widget in new_window.grid_slaves():
            if int(widget.grid_info()["row"]) == 3:
                widget.destroy()

    if input_name2s.get().upper()== "M":
        Name2 = Label(new_window, text="HAZELNUT", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name2.grid(row=3, column=1, sticky="nw",padx=220)

        Name2price = Label(new_window, text="₱85", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name2price.grid(row=3, column=1, sticky="nw",padx=610)

        btn_name2s = Button(new_window, text="Remove", font=("Arial Black", 12), bg="#F15A59", fg="white", command=UnorderItem)
        btn_name2s.grid(row=3, column=1, sticky="nw",padx=760,pady=7)

    elif input_name2s.get().upper() == "L":
        Name2 = Label(new_window, text="HAZELNUT", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name2.grid(row=3, column=1, sticky="nw",padx=220)

        Name2price = Label(new_window, text="₱99", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name2price.grid(row=3, column=1, sticky="nw",padx=610)

        btn_name2s = Button(new_window, text="Remove", font=("Arial Black", 12), bg="#F15A59", fg="white", command=UnorderItem)
        btn_name2s.grid(row=3, column=1, sticky="nw",padx=760,pady=7)

    else:
        messagebox.showerror("Error", "Please enter 'M' or 'L' for size.")
  
  
    if int(input_name2q.get()) > 10:
        messagebox.showerror("Error", "Please enter a quantity less than or equal to 10.")
    else:
        input_name2getQty = Label(new_window, text=input_name2q.get(), font=("Arial Black", 18), bg="#AD8E70", fg="white")
        input_name2getQty.grid(row=3, column=1, sticky="nw", padx=43)

    input_name1getSize = Label(new_window, text=input_name2s.get(), font=("Arial Black", 18), bg="#AD8E70", fg="white")
    input_name1getSize.grid(row=3, column=1, sticky="nw", padx=140)

    #name3
    def UnorderItem():
        for widget in new_window.grid_slaves():
            if int(widget.grid_info()["row"]) == 4:
                widget.destroy()

    if input_name3s.get().upper()== "M":
        Name3 = Label(new_window, text="CAPPUCCINO", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name3.grid(row=4, column=1, sticky="nw",padx=220)

        Name3price = Label(new_window, text="₱85", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name3price.grid(row=4, column=1, sticky="nw",padx=610)

        btn_name3s = Button(new_window, text="Remove", font=("Arial Black", 12), bg="#F15A59", fg="white", command=UnorderItem)
        btn_name3s.grid(row=4, column=1, sticky="nw",padx=760,pady=7)

    elif input_name3s.get().upper() == "L":
        Name3 = Label(new_window, text="CAPPUCCINO", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name3.grid(row=4, column=1, sticky="nw",padx=220)

        Name3price = Label(new_window, text="₱99", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name3price.grid(row=4, column=1, sticky="nw",padx=610)

        btn_name3s = Button(new_window, text="Remove", font=("Arial Black", 12), bg="#F15A59", fg="white", command=UnorderItem)
        btn_name3s.grid(row=4, column=1, sticky="nw",padx=760,pady=7)

    else:
        messagebox.showerror("Error", "Please enter 'M' or 'L' for size.")

    if int(input_name3q.get()) > 10:
        messagebox.showerror("Error", "Please enter a quantity less than or equal to 10.")
    else:
        input_name3getQty = Label(new_window, text=input_name3q.get(), font=("Arial Black", 18), bg="#AD8E70", fg="white")
        input_name3getQty.grid(row=4, column=1, sticky="nw", padx=43)

    input_name3getSize = Label(new_window, text=input_name3s.get(), font=("Arial Black", 18), bg="#AD8E70", fg="white")
    input_name3getSize.grid(row=4, column=1, sticky="nw", padx=140)

    #name4
    def UnorderItem():
        for widget in new_window.grid_slaves():
            if int(widget.grid_info()["row"]) == 5:
                widget.destroy()

    if input_name4s.get().upper()== "M":
        Name4 = Label(new_window, text="STRAWBERRY", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name4.grid(row=5, column=1, sticky="nw",padx=220)

        Name4price = Label(new_window, text="₱85", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name4price.grid(row=5, column=1, sticky="nw",padx=610)

        btn_name4s = Button(new_window, text="Remove", font=("Arial Black", 12), bg="#F15A59", fg="white", command=UnorderItem)
        btn_name4s.grid(row=5, column=1, sticky="nw",padx=760,pady=7)

    elif input_name4s.get().upper() == "L":
        Name4 = Label(new_window, text="STRAWBERRY", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name4.grid(row=5, column=1, sticky="nw",padx=220)

        Name4price = Label(new_window, text="₱99", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name4price.grid(row=5, column=1, sticky="nw",padx=610)

        btn_name4s = Button(new_window, text="Remove", font=("Arial Black", 12), bg="#F15A59", fg="white", command=UnorderItem)
        btn_name4s.grid(row=5, column=1, sticky="nw",padx=760,pady=7)

    else:
        messagebox.showerror("Error", "Please enter 'M' or 'L' for size.")

    if int(input_name4q.get()) > 10:
        messagebox.showerror("Error", "Please enter a quantity less than or equal to 10.")
    else:
        input_name4getQty = Label(new_window, text=input_name4q.get(), font=("Arial Black", 18), bg="#AD8E70", fg="white")
        input_name4getQty.grid(row=5, column=1, sticky="nw", padx=43)

    input_name4getSize = Label(new_window, text=input_name4s.get(), font=("Arial Black", 18), bg="#AD8E70", fg="white")
    input_name4getSize.grid(row=5, column=1, sticky="nw", padx=140)

    #name5
    def UnorderItem():
        for widget in new_window.grid_slaves():
            if int(widget.grid_info()["row"]) == 6:
                widget.destroy()

    if input_name4s.get().upper()== "M":
        Name5 = Label(new_window, text="CHOCOLATE", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name5.grid(row=6, column=1, sticky="nw",padx=220)

        Name5price = Label(new_window, text="₱85", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name5price.grid(row=6, column=1, sticky="nw",padx=610)

        btn_name5s = Button(new_window, text="Remove", font=("Arial Black", 12), bg="#F15A59", fg="white", command=UnorderItem)
        btn_name5s.grid(row=6, column=1, sticky="nw",padx=760,pady=7)

    elif input_name5s.get().upper() == "L":
        Name5 = Label(new_window, text="CHOCOLATE", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name5.grid(row=6, column=1, sticky="nw",padx=220)

        Name5price = Label(new_window, text="₱99", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name5price.grid(row=6, column=1, sticky="nw",padx=610)

        btn_name5s = Button(new_window, text="Remove", font=("Arial Black", 12), bg="#F15A59", fg="white", command=UnorderItem)
        btn_name5s.grid(row=6, column=1, sticky="nw",padx=760,pady=7)

    else:
        messagebox.showerror("Error", "Please enter 'M' or 'L' for size.")

    if int(input_name5q.get()) > 10:
        messagebox.showerror("Error", "Please enter a quantity less than or equal to 10.")
    else:
        input_name5getQty = Label(new_window, text=input_name5q.get(), font=("Arial Black", 18), bg="#AD8E70", fg="white")
        input_name5getQty.grid(row=6, column=1, sticky="nw", padx=43)

    input_name5getSize = Label(new_window, text=input_name5s.get(), font=("Arial Black", 18), bg="#AD8E70", fg="white")
    input_name5getSize.grid(row=6, column=1, sticky="nw", padx=140)

    #name6
    def UnorderItem():
        for widget in new_window.grid_slaves():
            if int(widget.grid_info()["row"]) == 7:
                widget.destroy()

    if input_name6s.get().upper()== "M":
        Name6 = Label(new_window, text="ICED MATCHA LATTE", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name6.grid(row=7, column=1, sticky="nw",padx=220)

        Name6price = Label(new_window, text="₱85", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name6price.grid(row=7, column=1, sticky="nw",padx=610)

        btn_name6s = Button(new_window, text="Remove", font=("Arial Black", 12), bg="#F15A59", fg="white", command=UnorderItem)
        btn_name6s.grid(row=7, column=1, sticky="nw",padx=760,pady=7)

    elif input_name6s.get().upper() == "L":
        Name6 = Label(new_window, text="ICED MATCHA LATTE", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name6.grid(row=7, column=1, sticky="nw",padx=220)

        Name6price = Label(new_window, text="₱99", font=("Arial Black", 18), bg="#AD8E70", fg="white")
        Name6price.grid(row=7, column=1, sticky="nw",padx=610)

        btn_name6s = Button(new_window, text="Remove", font=("Arial Black", 12), bg="#F15A59", fg="white", command=UnorderItem)
        btn_name6s.grid(row=7, column=1, sticky="nw",padx=760,pady=7)

    else:
        messagebox.showerror("Error", "Please enter 'M' or 'L' for size.")

    if int(input_name6q.get()) > 10:
        messagebox.showerror("Error", "Please enter a quantity less than or equal to 10.")
    else:
        input_name5getQty = Label(new_window, text=input_name6q.get(), font=("Arial Black", 18), bg="#AD8E70", fg="white")
        input_name5getQty.grid(row=7, column=1, sticky="nw", padx=43)

    input_name6getSize = Label(new_window, text=input_name6s.get(), font=("Arial Black", 18), bg="#AD8E70", fg="white")
    input_name6getSize.grid(row=7, column=1, sticky="nw", padx=140)

    #lower button
    def backtomenu():
        # Destroying the current window
        new_window.destroy()
        # Opening the previous window
        root.deiconify()
        
    btn_backtomain = Button(new_window,text="Back to menu", font= ("Arial Black", 18), bg="#CDB699", fg="white", command=backtomenu)
    btn_backtomain.grid(row=8, column=1, sticky='sw', padx=15, pady=3)

    def calculate_total_price():
    # get user input
        sizes = [input_name1s.get(), input_name2s.get(), input_name3s.get(), input_name4s.get(), input_name5s.get(), input_name6s.get()]
        qtys = [input_name1q.get(), input_name2q.get(), input_name3q.get(), input_name4q.get(), input_name5q.get(), input_name6q.get()]

    # calculate total price
        total_price = 0
        for i in range(len(sizes)):
            if sizes[i] == "M":
                price = 85
            elif sizes[i] == "L":
                price = 99

            total_price += int(qtys[i]) * price

    # display total price
        total_price_label = Label(new_window, text="Total Price: PHP 0", font=("Arial Black", 20), bg="#AD8E70", fg="white")
        total_price_label.config(text="Total Price: PHP {}".format(total_price))
        total_price_label.grid(row=8, column=1, sticky="nw", padx=298)

    btn_Totalall = Button(new_window, text ="Total",font= ("Arial Black", 18), bg="#CDB699", fg="white", command=calculate_total_price)
    btn_Totalall.grid(row=8, column=1, sticky="nw",padx=758)

#the main window
root = Tk() 
root.geometry("900x500")
root.title("MINI SYSTEM - WoWz coffee shop")
root.configure(bg="#AD8E70")
import subprocess



lbl_Menu = Label(root, text="MENU", font=("Arial Black", 30), bg="#AD8E70", fg="white")
lbl_Menu.grid(row=0, column=1,columnspan=3, sticky="w")

coffeeName = Label(root, text="Name", font=("Arial Black", 25), bg="#AD8E70", fg="white")
coffeeName.grid(row=1, column=0, sticky="nw", padx=15, pady=6)

coffeeSize_price = Label(root, text="Size & Price", font=("Arial Black", 25), bg="#AD8E70", fg="white")
coffeeSize_price.grid(row=1, column=1,columnspan=3, sticky="w")

coffeeSize_price = Label(root, text="", font=("Arial Black", 25), bg="#AD8E70", fg="white")
coffeeSize_price.grid(row=1, column=2, columnspan=3,sticky="w")

#coffe name
Name1 = Label(root, text="SPANISH LATTE", font=("Arial Black", 20), bg="#AD8E70", fg="white")
Name1.grid(row=2, column=0, sticky="nw", padx=15, pady=1.5)

Name2 = Label(root, text="HAZELNUT", font=("Arial Black", 20), bg="#AD8E70", fg="white")
Name2.grid(row=3, column=0, sticky="nw", padx=15, pady=1.5)

Name3 = Label(root, text="CAPPUCCINO", font=("Arial Black", 20), bg="#AD8E70", fg="white")
Name3.grid(row=4, column=0, sticky="nw", padx=15, pady=1.5)

Name4 = Label(root, text="STRAWBERRY", font=("Arial Black", 20), bg="#AD8E70", fg="white")
Name4.grid(row=5, column=0, sticky="nw", padx=15, pady=1.5)

Name5 = Label(root, text="CHOCOLATE", font=("Arial Black", 20), bg="#AD8E70", fg="white")
Name5.grid(row=6, column=0, sticky="nw", padx=15, pady=1.5)

Name6 = Label(root, text="ICED MATCHA LATTE", font=("Arial Black", 20), bg="#AD8E70", fg="white")
Name6.grid(row=7, column=0, sticky="nw", padx=15, pady=1.5)

#button for size and price
#---------------------------------------name1----------------------------------------------------#
lbl_name1 = Label(root,text="[M] ₱85", font=("Arial Black", 10), bg="#321E1E", fg="white")
lbl_name1.grid(row=2, column=1, sticky="w",padx=40)

lbl_name1 = Label(root,text="[L] ₱99", font=("Arial Black", 10), bg="#321E1E", fg="white")
lbl_name1.grid(row=2, column=1, sticky="w",padx=110)

lbl_name1 = Label(root,text="Size:", font=("Arial Black", 10), bg="#AD8E70" ,fg="white")
lbl_name1.grid(row=2, column=2, sticky="w")

input_name1s = Entry(root,width = 13, justify="center")
input_name1s.grid(row=2, column=2, sticky="w",padx=37)

lbl_name1 = Label(root,text="Qty:", font=("Arial Black", 10), bg="#AD8E70" ,fg="white")
lbl_name1.grid(row=2, column=2, sticky="w",padx=125)

input_name1q = Entry(root,width = 13, justify="center")
input_name1q.grid(row=2, column=2, sticky="w",padx=159)

#---------------------------------------name2----------------------------------------------------#
lbl_name2 = Label(root,text="[M] ₱85", font=("Arial Black", 10), bg="#321E1E", fg="white")
lbl_name2.grid(row=3, column=1, sticky="w", padx=40)

lbl_name2 = Label(root,text="[L] ₱99", font=("Arial Black", 10), bg="#321E1E", fg="white")
lbl_name2.grid(row=3, column=1, sticky="w", padx=110)

lbl_name2 = Label(root,text="Size:", font=("Arial Black", 10), bg="#AD8E70" ,fg="white")
lbl_name2.grid(row=3, column=2, sticky="w")

input_name2s = Entry(root,width = 13,justify="center")
input_name2s.grid(row=3, column=2, sticky="w",padx=37)

lbl_name2 = Label(root,text="Qty:", font=("Arial Black", 10), bg="#AD8E70" ,fg="white")
lbl_name2.grid(row=3, column=2, sticky="w",padx=125)

input_name2q = Entry(root,width = 13,justify="center")
input_name2q.grid(row=3, column=2, sticky="w",padx=159)

#---------------------------------------name3----------------------------------------------------#
lbl_name3 = Label(root,text="[M] ₱85", font=("Arial Black", 10), bg="#321E1E", fg="white")
lbl_name3.grid(row=4, column=1, sticky="w", padx=40)

lbl_name3 = Label(root,text="[L] ₱99", font=("Arial Black", 10), bg="#321E1E", fg="white")
lbl_name3.grid(row=4, column=1, sticky="w", padx=110)

lbl_name3 = Label(root,text="Size:", font=("Arial Black", 10), bg="#AD8E70" ,fg="white")
lbl_name3.grid(row=4, column=2, sticky="w")

input_name3s = Entry(root,width = 13,justify="center")
input_name3s.grid(row=4, column=2, sticky="w",padx=37)

lbl_name3 = Label(root,text="Qty:", font=("Arial Black", 10), bg="#AD8E70" ,fg="white")
lbl_name3.grid(row=4, column=2, sticky="w",padx=125)

input_name3q = Entry(root,width = 13,justify="center")
input_name3q.grid(row=4, column=2, sticky="w",padx=159)
#---------------------------------------name4----------------------------------------------------#
lbl_name4 = Label(root,text="[M] ₱85", font=("Arial Black", 10), bg="#321E1E", fg="white")
lbl_name4.grid(row=5, column=1, sticky="w", padx=40)

lbl_name4 = Label(root,text="[L] ₱99", font=("Arial Black", 10), bg="#321E1E", fg="white")
lbl_name4.grid(row=5, column=1, sticky="w", padx=110)

lbl_name4 = Label(root,text="Size:", font=("Arial Black", 10), bg="#AD8E70" ,fg="white")
lbl_name4.grid(row=5, column=2, sticky="w")

input_name4s = Entry(root,width = 13,justify="center")
input_name4s.grid(row=5, column=2, sticky="w",padx=37)

lbl_name4 = Label(root,text="Qty:", font=("Arial Black", 10), bg="#AD8E70" ,fg="white")
lbl_name4.grid(row=5, column=2, sticky="w",padx=125)

input_name4q = Entry(root,width = 13,justify="center")
input_name4q.grid(row=5, column=2, sticky="w",padx=159)
#---------------------------------------name5----------------------------------------------------#
lbl_name5 = Label(root,text="[M] ₱85", font=("Arial Black", 10), bg="#321E1E", fg="white")
lbl_name5.grid(row=6, column=1, sticky="w", padx=40)

lbl_name5 = Label(root,text="[L] ₱99", font=("Arial Black", 10), bg="#321E1E", fg="white")
lbl_name5.grid(row=6, column=1, sticky="w", padx=110)

lbl_name5 = Label(root,text="Size:", font=("Arial Black", 10), bg="#AD8E70" ,fg="white")
lbl_name5.grid(row=6, column=2, sticky="w")

input_name5s = Entry(root,width = 13,justify="center")
input_name5s.grid(row=6, column=2, sticky="w",padx=37)

lbl_name5 = Label(root,text="Qty:", font=("Arial Black", 10), bg="#AD8E70" ,fg="white")
lbl_name5.grid(row=6, column=2, sticky="w",padx=125)

input_name5q = Entry(root,width = 13,justify="center")
input_name5q.grid(row=6, column=2, sticky="w",padx=159)
#---------------------------------------name6----------------------------------------------------#
lbl_name6 = Label(root,text="[M] ₱85", font=("Arial Black", 10), bg="#321E1E", fg="white")
lbl_name6.grid(row=7, column=1, sticky="w", padx=40)

lbl_name6 = Label(root,text="[L] ₱99", font=("Arial Black", 10), bg="#321E1E", fg="white")
lbl_name6.grid(row=7, column=1, sticky="w", padx=110)

lbl_name6 = Label(root,text="Size:", font=("Arial Black", 10), bg="#AD8E70" ,fg="white")
lbl_name6.grid(row=7, column=2, sticky="w")

input_name6s = Entry(root,width = 13,justify="center")
input_name6s.grid(row=7, column=2, sticky="w",padx=37)

lbl_name6 = Label(root,text="Qty:", font=("Arial Black", 10), bg="#AD8E70" ,fg="white")
lbl_name6.grid(row=7, column=2, sticky="w",padx=125)

input_name6q = Entry(root,width = 13,justify="center")
input_name6q.grid(row=7, column=2, sticky="w",padx=159)
#---------------------------------------END OF SIZE & PRICE----------------------------------------------------#

def Backtomainpage():
    subprocess.run(["Python","mainPage.py"])

def Clearall():
    input_name1q.delete(0,END)
    input_name1s.delete(0,END)
    input_name2q.delete(0,END)
    input_name2s.delete(0,END)
    input_name3q.delete(0,END)
    input_name3s.delete(0,END)
    input_name4q.delete(0,END)
    input_name4s.delete(0,END)
    input_name5q.delete(0,END)
    input_name5s.delete(0,END)
    input_name6q.delete(0,END)
    input_name6s.delete(0,END)

# def orderConfirm():
#     subprocess.run(["Python","DSA&Comprog2_Final_PIT.py\orderConfirmPage.py"])

btn_backtomain = Button(root,text="Back", font= ("Arial Black", 20), bg="#CDB699", fg="white", command=Backtomainpage)
btn_backtomain.grid(row=8, column=0, sticky='sw', padx=15, pady=2)

btn_ClearALL = Button(root,text="Clear all", font= ("Arial Black", 20), bg="#CDB699", fg="white", command=Clearall)
btn_ClearALL.grid(row=8, column=1, sticky='w', padx=25, pady=2)

btn_orderConfirm = Button(root,text="Next", font= ("Arial Black", 20), bg="#CDB699", fg="white", command= OrderConfirm)
btn_orderConfirm.grid(row=8, column=2,sticky='se',padx=155,pady=2)

root.mainloop()