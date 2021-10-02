from tkinter import *

base = Tk()
base.title("calculator design ")
base.geometry('600x500')

label_1 = Label(base, text='Enter first number:')
label_1.place(x=120, y=80)

blank_entry_box1 = Entry(base, width='20')
blank_entry_box1.place(x=260, y=80)

label_2 = Label(base, text='Enter second number:')
label_2.place(x=120, y=120)

blank_entry_box2 = Entry(base, width='20')
blank_entry_box2.place(x=260, y=120)

button_1 = Button(base, text='ADD')
button_1.place(x=120, y=180)

button_2 = Button(base, text='SUBTRACT')
button_2.place(x=175, y=179)

button_3 = Button(base, text='MULTIPLY')
button_3.place(x=265, y=178)

button_4 = Button(base, text='DIVIDE')
button_4.place(x=355, y=177)

button_5 = Button(base, text='RESULT ')
button_5.place(x=220, y=250)
base.mainloop()