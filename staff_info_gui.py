from tkinter import *

base = Tk()
base.title("This is staff info ")
base.geometry("500x400")

label_1 = Label(base, text="Enter your name: ")
label_1.place(x=120, y=60)

blank_white_box1 = Entry(base, width='20')
blank_white_box1.place(x=250, y=60)

label_2 = Label(base, text='Enter email address:')
label_2.place(x=120, y=90)

blank_white_box2 = Entry(base, width='20')
blank_white_box2.place(x=250, y=90)

label_3 = Label(base, text='Enter contact number:')
label_3.place(x=120, y=120)

blank_white_box3 = Entry(base, width='20')
blank_white_box3.place(x=250, y=120)

label_4 = Label(base, text='Enter city:')
label_4.place(x=120, y=150)

blank_white_box4 = Entry(base, width='20')
blank_white_box4.place(x=250, y=150)

button_1 = Button(base, text='Submit')
button_1.place(x=210, y=200)

base.mainloop()