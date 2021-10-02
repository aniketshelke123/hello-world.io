
from tkinter import *
from tkinter.filedialog import asksaveasfile


base = Tk()
base.title("Notepad")
base.geometry("600x600")
t1 = Text(base, width=600, font=('Verdana', 15, 'normal'))
t1.place(x=0, y=0, height=600)


def cut():
    t1.event_generate("<<Cut>>")


def copy():
    t1.event_generate("<<Copy>>")


def paste():
    t1.event_generate("<<Paste>>")


def ex_it():
    base.quit()


def zoom_out():
    base.attributes('-fullscreen', True)


def zoom_in():
    base.attributes('-fullscreen', False)


def save():
    data = [('All tyes(*.*)', '*.*')]
    file = asksaveasfile(filetypes=data, defaultextension=data)


def op_en():
    from os import startfile
    startfile("C:\\Users\\Lenovo\\PycharmProjects\\tes")


mb = Menu(base)  # prepares a menubar, and placed in base
m2 = Menu(mb, tearoff=0)
m2.add_command(label="Undo", accelerator='Ctrl+Z')
m2.add_separator()
m2.add_command(label="Cut", accelerator='Ctrl+X', command=cut)
m2.add_command(label="Copy", accelerator='Ctrl+C', command=copy)
# m2.bind("<Control-c>", copy)
m2.add_command(label="Paste", accelerator='Ctrl+V', command=paste)
m2.add_command(label='Delete')


m1 = Menu(mb, tearoff=0)
m1.add_command(label="New", accelerator='Ctrl + N')
m1.add_command(label="Open", accelerator='Ctrl + O', command=op_en)
m1.add_command(label="Save", accelerator='Ctrl + S', command=save)
m1.add_command(label="Save As..")
m1.add_separator()
m1.add_command(label="Print Setup")
m1.add_command(label="Print", accelerator='Ctrl + P')
m1.add_command(label="Exit", command=ex_it)


m3_1 = Menu(mb, tearoff=0)
m3_1.add_command(label='Zoom In', command=zoom_in)
m3_1.add_command(label='Zoom Out', command=zoom_out)
m3_1.add_command(label='Restore Default')

m3 = Menu(mb, tearoff=0)
m3.add_cascade(label="Zoom", menu=m3_1)
m3.add_separator()
m3.add_command(label="Status Bar")


m4 = Menu(mb, tearoff=0)
m4.add_command(label="Word Wrap")
m4.add_command(label="Font.")


m5 = Menu(mb, tearoff=0)
m5.add_command(label="View Help")
m5.add_separator()
m5.add_command(label="About Notepad")


mb.add_cascade(label="File", menu=m1)
mb.add_cascade(label="Edit", menu=m2)
mb.add_cascade(label='View', menu=m3)
mb.add_cascade(label='Format', menu=m4)
mb.add_cascade(label='Help', menu=m5)
base.config(menu=mb)
base.mainloop()

