from tkinter import *


base = Tk()
base.title("Windows refresh")
base.geometry('400x400')
mb = Menu(base, tearoff=0)

# base.iconbitmap('C:\\Users\\Lenovo\\Downloads\\UIHere.png')
photo = PhotoImage(file="C:\\Users\\Lenovo\\Downloads\\UIHere.png")
base.iconphoto(False, photo)


def method1(event):
    mb.tk_popup(event.x_root, event.y_root)


m1 = Menu(mb, tearoff=0)
m1.add_radiobutton(label="Large icons")
m1.add_radiobutton(label="Medium icons")
m1.add_radiobutton(label="Small icons")
m1.add_separator()
m1.add_checkbutton(label="Auto Arrange icons")
m1.add_checkbutton(label="Align icons to grid")
m1.add_separator()
m1.add_checkbutton(label="Show Desktop icons")
m2 = Menu(mb, tearoff=0)
m2.add_radiobutton(label="Name")
m2.add_radiobutton(label="Size")
m2.add_radiobutton(label="Item Type")
m2.add_radiobutton(label="Date Modified")


m4 = Menu(mb, tearoff=0)
m4.add_radiobutton(label="Start Synchronizing...")
m4.add_radiobutton(label="Learn More...")

m5 = Menu(mb, tearoff=0)
m5.add_cascade(label="Folder")
m5.add_cascade(label="Shortcut")
m5.add_separator()
m5.add_cascade(label="Microsoft Access Database")
base.iconbitmap('C:\\Users\\Lenovo\\Downloads\\UIHere.png')


m5.add_cascade(label="Bitmap image")
m5.add_cascade(label="Microsoft Word Document")
m5.add_cascade(label="Microsoft PowerPoint Presentation")
m5.add_cascade(label="Microsoft Publisher Document")
m5.add_cascade(label="WinRAR archive")
m5.add_cascade(label="Text Document")
m5.add_cascade(label="Microsoft Excel Worksheet")
m5.add_cascade(label="WinRAR ZIP archive")

mb.add_cascade(label="View", menu=m1)
mb.add_cascade(label="Sort by", menu=m2)
mb.add_cascade(label="Refresh")
mb.add_separator()
mb.add_cascade(label="Paste")
mb.add_cascade(label="Paste shortcut")
mb.add_separator()

mb.add_cascade(label="NVIDIA Control Panel")
mb.add_separator()

mb.add_cascade(label="Shared Folder Synchronization", menu=m4)
mb.add_separator()

mb.add_cascade(label="New", menu=m5)
mb.add_separator()

mb.add_cascade(label="Display settings")
mb.add_cascade(label="Personalize")

base.bind("<Button-3>", method1)
base.mainloop()
