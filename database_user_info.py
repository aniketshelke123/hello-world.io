from tkinter import *
import sqlite3

root = sqlite3.connect("gui_stud_data.db")

# start of sign-up page.................................
base1 = Tk()
base1.title('sign-up form')
base1.geometry('650x600')
base1.configure(bg='#c6ebc9')
text_bg = '#c6ebc9'
font = ('Times New Roman', 15)
entry_font = ('Times New Roman', 15)


def enter_into_database():
    s_name = name_entry.get()
    s_roll = roll_entry.get()
    s_class = class_entry.get()
    s_branch = branch_entry.get()
    s_mob = mob_entry.get()
    s_city = city_entry.get()
    query = f"insert into stud_data values('{s_name}', {s_roll}, '{s_class}', '{s_branch}', {s_mob}, '{s_city}')"
    # query = "insert into stud_data values ('{0}', {1}, '{2}', '{3}', {4}, '{5}')".format(s_name, s_roll, s_class, s_branch, s_mob, s_city)

    root.execute(query)
    root.commit()
    root.close()
    display_saved.configure(text="Data Saved..!")
    base1.after(2000, display_saved.destroy)


name = Label(base1, text="Enter Student name", font=font, bg=text_bg)
name.place(x=100, y=80)

rollno = Label(base1, text="Enter Student rollno", font=font, bg=text_bg)
rollno.place(x=100, y=140)

s_class = Label(base1, text="Student Class", font=font, bg=text_bg)
s_class.place(x=100, y=200)

branch = Label(base1, text="Select Branch ", font=font, bg=text_bg)
branch.place(x=100, y=260)

mobile = Label(base1, text="Enter mobile no", font=font, bg=text_bg)
mobile.place(x=100, y=320)

city = Label(base1, text="Enter City", font=font, bg=text_bg)
city.place(x=100, y=380)

display_saved = Label(base1, bg=text_bg)
display_saved.place(x=210, y=480)

# entry widgets

name_entry = Entry(base1, font=entry_font)
name_entry.place(x=280, y=80, width=220, height=22)

roll_entry = Entry(base1, font=entry_font)
roll_entry.place(x=280, y=140, width=220, height=22)

class_entry = Entry(base1, font=entry_font)
class_entry.place(x=280, y=200, width=220, height=22)

branch_entry = Entry(base1, font=entry_font)
branch_entry.place(x=280, y=260, width=220, height=22)

mob_entry = Entry(base1, font=entry_font)
mob_entry.place(x=280, y=320, width=220, height=22)

city_entry = Entry(base1, font=entry_font)
city_entry.place(x=280, y=380, width=220, height=22)
# button widgets

create_button = Button(base1, width=10, text="SUBMIT", font=font, bg='#d4e2d4', command=enter_into_database)
create_button.place(x=160, y=450)

reset_button = Button(base1, width=10, text="Reset", font=font)
reset_button.place(x=360, y=450)

base1.mainloop()
