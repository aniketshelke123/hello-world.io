
from tkinter import *

# step 1: declaring base
base = Tk()
base.title("This is First gui")
base.geometry("600x500")

# step 2: declaring and packing widgets
btn1 = Button(base, text="Submit")
btn1.pack()

txt1 = Entry(base, width=15)
txt1.pack()

ch1 = Checkbutton(base, text="PIZZA")
ch1.pack()

# step 3: making the base visible
base.mainloop()
