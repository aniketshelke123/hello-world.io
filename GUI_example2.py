from tkinter.ttk import *
from tkinter import *

base = Tk()
base.title("you can write anything here ")
base.geometry("500x300")

lb1 = Label(base, text="Enter User ID")
lb1.grid(row=0, column=0)

photo = PhotoImage(file=r'C:\Users\Lenovo\Downloads\UIHere.png')

txt1 = Entry(base, width=15)
txt1.grid(row=0, column=1)

lb2 = Label(base, text="Enter Password Here")
lb2.grid(row=1, column=0)

txt2 = Entry(base, width=15, show='*')
txt2.grid(row=1, column=1)

btn1 = Button(base, image=photo)
btn1['text'] = "Save Data"
btn1['font'] = ("Arial Bold", 15)
btn1.place(x=100, y=150)

btn2 = Button(base)
btn2.configure(text="Submit", font=("Arial Bold", 20))
btn2.place(x=200, y=120)
base.mainloop()