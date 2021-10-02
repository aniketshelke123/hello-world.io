
from tkinter import *

base = Tk()
base.title("User-form")
base.geometry("700x600")
base.configure(bg='#dbf6e9')
font_and_size = ('Times New Roman', 20)
text_background = '#dbf6e9'


def method1():
    namer = name_entry.get()
    mail = email_entry.get()
    mob = contact_entry.get()
    city = city_entry.get()
    gender = genderr.get()
    user_data_obj = open("userdata.txt", "a")
    user_data_obj.write(namer + ", " + mail + ", " + mob + ', ' + city + ', ' + gender + '\n')
    user_data_obj.close()
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    contact_entry.delete(0, END)
    city_entry.delete(0, END)
    name_entry.focus()


genderr = StringVar()

name_label = Label(base, text='Enter your name', background=text_background, font=font_and_size)
name_label.place(x=100, y=80)

name_entry = Entry(base, font=('calibre', 12, 'normal'))
name_entry.place(x=360, y=90, width=200, height=25)

email = Label(base, text='Enter your E-mail', background=text_background, font=font_and_size)
email.place(x=100, y=140)

email_entry = Entry(base, font=('calibre', 12, 'normal'))
email_entry.place(x=360, y=150, width=200, height=25)


contact_no = Label(base, text='Enter your Contact no', background=text_background, font=font_and_size)
contact_no.place(x=100, y=200)

contact_entry = Entry(base, font=('calibre', 12, 'normal'))
contact_entry.place(x=360, y=210, width=200, height=25)


city = Label(base, text='Enter your City name', background=text_background, font=font_and_size)
city.place(x=100, y=260)

city_entry = Entry(base, font=('calibre', 12, 'normal'))
city_entry.place(x=360, y=270, width=200, height=25)


gender = Label(base, text='Select your Gender', background=text_background, font=font_and_size)
gender.place(x=100, y=320)


gender_entry = Radiobutton(base, text='Male', background=text_background, font=font_and_size, variable=genderr, value='male')
gender_entry.place(x=350, y=320)


gender_entry = Radiobutton(base, text='Female', background=text_background, font=font_and_size, variable=genderr, value='female')
gender_entry.place(x=460, y=320)


save = Button(base, text='Save', font=font_and_size, background='#c8c6a7', command=method1)
save.place(x=250, y=400, width=130, height=40)
base.mainloop()
