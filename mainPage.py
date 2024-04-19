from tkinter import*
import subprocess

root = Tk()
root.geometry("770x500")
root.title("MINI SYSTEM - WoWz coffee shop")
root.configure(bg="#AD8E70")

shopName = Label(root, text="WoWz coffee shop", font=("Arial Black", 30), bg="#AD8E70", fg="white")
shopName.pack(padx=15,pady=10)

image = PhotoImage(file="coffee logo 3.png")
labelpic = Label(root, image=image,bg="#AD8E70")
labelpic.pack(padx=0,pady=10)

def run_anotherFile():
    subprocess.run(["python","menuorderConfirmpage.py"]) #the path is not final this is only copy version

btn_toOrder=Button(root, text="CLICK TO ORDER", font=("Arial Black", 25), bg="#CDB699",activebackground="#CDB699", fg="white",activeforeground="white",command=run_anotherFile)
btn_toOrder.pack()

root.mainloop()

