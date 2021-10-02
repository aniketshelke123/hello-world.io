from tkinter import *

base = Tk()
base.title('Calci gui')
base.geometry('360x400')
base.configure(bg='#f4f9f9')
text_font = ('Helvetica', 12, 'bold')

solution_box = Text(base, bg='#e7e6e1', font=('Helvetica', 12, 'normal'))
solution_box.place(x=15, y=15, width=320, height=70)
# def method1():
#     onee = int(one.get())


one = Button(base, text=1, font=text_font, bg='#a3ddcb')
one.place(x=20, y=120, width=80, height=50)

two = Button(base, text=2, font=text_font, bg='#a3ddcb')
two.place(x=105, y=120, width=80, height=50)

three = Button(base, text=3, font=text_font, bg='#a3ddcb')
three.place(x=190, y=120, width=80, height=50)

four = Button(base, text=4, font=text_font, bg='#a3ddcb')
four.place(x=20, y=175, width=80, height=50)

five = Button(base, text=5, font=text_font, bg='#a3ddcb')
five.place(x=105, y=175, width=80, height=50)

six = Button(base, text=6, font=text_font, bg='#a3ddcb')
six.place(x=190, y=175, width=80, height=50)

seven = Button(base, text=7, font=text_font, bg='#a3ddcb')
seven.place(x=20, y=230, width=80, height=50)

eight = Button(base, text=8, font=text_font, bg='#a3ddcb')
eight.place(x=105, y=230, width=80, height=50)

nine = Button(base, text=9, font=text_font, bg='#a3ddcb')
nine.place(x=190, y=230, width=80, height=50)

zero = Button(base, text=0, font=text_font, bg='#a3ddcb')
zero.place(x=20, y=285, width=80, height=50)

dot = Button(base, text='.', font=text_font, bg='#a3ddcb')
dot.place(x=105, y=285, width=80, height=50)

equals = Button(base, text='=', font=text_font, bg='#fd8c04')
equals.place(x=190, y=285, width=80, height=50)

ac = Button(base, text='AC', font=text_font, bg='#fd8c04')
ac.place(x=280, y=115, width=60, height=40)

add = Button(base, text='+', font=text_font, bg='#fecd1a')
add.place(x=280, y=160, width=60, height=40)

sub = Button(base, text='-', font=text_font, bg='#fecd1a')
sub.place(x=280, y=205, width=60, height=40)

mul = Button(base, text='x', font=text_font, bg='#fecd1a')
mul.place(x=280, y=250, width=60, height=40)

div = Button(base, text='/', font=text_font, bg='#fecd1a')
div.place(x=280, y=295, width=60, height=40)
base.mainloop()
