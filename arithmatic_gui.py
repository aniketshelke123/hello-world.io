from tkinter import *


main = Tk()
main.title("Arithmatic operations")
main.geometry('800x500')
main.minsize(100, 100)
main.configure(bg="#dbf6e9")
style = ('Comic Sans MS', 13)


def add():
    val_1 = int(e1.get())
    val_2 = int(e2.get())
    result = val_1 + val_2
    print(result)
    e3.insert(0, result)


def sub():
    val_1 = int(e1.get())
    val_2 = int(e2.get())
    result = val_1 - val_2
    print(result)
    e3.insert(0, result)

def mul():
    val_1 = int(e1.get())
    val_2 = int(e2.get())
    result = val_1 * val_2
    print(result)
    e3.insert(0, result)

def div():
    val_1 = int(e1.get())
    val_2 = int(e2.get())
    result = val_1 / val_2
    print(result)
    e3.insert(0, result)


def delete():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)


Label(main, text="------ CALCULATOR ------", bg='#e84545', font=style).place(x=290, y=60)


l1 = Label(main, text=" FIRST NO ", font=style, bg="white")
l1.place(x=180, y=130)
l2 = Label(main, text="SECOND NO ", font=style, bg="white")
l2.place(x=180, y=190)

e1 = Entry(main, width=40, borderwidth=4, relief=GROOVE)
e1.place(x=320, y=135)
e2 = Entry(main, width=40, borderwidth=4, relief=GROOVE)
e2.place(x=320, y=190)

b1 = Button(main, text="ADD", font=style, bg="orange", width=7, command=add)
b1.place(x=200, y=240)
b2 = Button(main, text="SUB", font=style, bg="orange", width=7, command=sub)
b2.place(x=290, y=240)
b3 = Button(main, text="MULT", font=style, bg="orange", width=7, command=mul)
b3.place(x=380, y=240)
b4 = Button(main, text="DIV", font=style, bg="orange", width=7, command=div)
b4.place(x=470, y=240)

b4 = Button(main, text="Reset", font=style, bg="orange", width=7, command=delete)
b4.place(x=320, y=400)

l3 = Label(main, text="RESULT ", font=style, bg="white")
l3.place(x=200, y=330)

e3 = Entry(main, width=20, borderwidth=4, font=style, relief=GROOVE)
e3.place(x=320, y=340)

main.mainloop()
