from tkinter import *
from tkinter import ttk
base = Tk()
base.title("Sign_in & Sign_up form")
base.geometry("650x400")
base.configure(bg='#c6ebc9')
text_bg = '#c6ebc9'
font = ('Times New Roman', 15)


def workshop_reg():

    base = Tk()
    base.title("Workshop registration form")
    base.geometry('1200x700')
    base.configure(bg='#f4f6ff')
    text_font = ('Georgia', 12)
    text_bg = '#f4f6ff'
    entry_font = ('Georgia', 12, 'normal')
    I_state = ('Maharashtra', 'UP', 'Goa', 'Kerala', 'Gujarat')
    countries = ("India", 'Sri-Lanka', 'Bangladesh', 'Nepal')
    meal = ('veg', 'non-veg')

    # title for the GUi
    title = Label(base, text="~~~~~~~Workshop Registration~~~~~~~", font=('Bookman', 18), bg='#fdd365', padx=400)
    title.place(x=0, y=0)

    # registration text
    register_text = Label(base, text='Register now while seats are available', font=('Georgia', 10), bg=text_bg,
                          foreground='#221f3b')
    register_text.place(x=10, y=50)

    # lunch text
    lunch_text = Label(base, text='Lunch', font=('Georgia', 10), bg=text_bg, foreground='#221f3b')
    lunch_text.place(x=600, y=50)

    # payment widget
    lunch_text = Label(base, text='Payment Details', font=('Georgia', 10), bg=text_bg, foreground='#221f3b')
    lunch_text.place(x=600, y=170)

    # Label widgets
    first_name = Label(base, text='First Name *', font=text_font, bg=text_bg)
    first_name.place(x=15, y=90)

    last_name = Label(base, text='Last Name *', font=text_font, bg=text_bg)
    last_name.place(x=15, y=130)

    institution = Label(base, text='Company/Institution *', font=text_font, bg=text_bg)
    institution.place(x=15, y=170)

    address = Label(base, text="Address *", font=text_font, bg=text_bg)
    address.place(x=15, y=220)

    city = Label(base, text='City* ', font=text_font, bg=text_bg)
    city.place(x=15, y=320)

    state = Label(base, text='State/Province/Region *', font=text_font, bg=text_bg)
    state.place(x=15, y=370)

    country = Label(base, text='Country *', font=text_font, bg=text_bg)
    country.place(x=15, y=420)

    e_mail = Label(base, text='E-mail *', font=text_font, bg=text_bg)
    e_mail.place(x=15, y=470)

    mob = Label(base, text='contact no *', font=text_font, bg=text_bg)
    mob.place(x=15, y=520)

    meal_preference = Label(base, text='Meal preference *', font=text_font, bg=text_bg)
    meal_preference.place(x=600, y=90)

    payment_label = Label(base, text='Payment Mode *', font=text_font, bg=text_bg)
    payment_label.place(x=600, y=220)

    cheque_label = Label(base, text='DD Cheque no', font=text_font, bg=text_bg)
    cheque_label.place(x=600, y=350)

    Bank_label = Label(base, text='Drawn on(Bank name)', font=text_font, bg=text_bg)
    Bank_label.place(x=600, y=400)

    Payable_label = Label(base, text='Payable at', font=text_font, bg=text_bg)
    Payable_label.place(x=600, y=450)

    # Entry widgets

    first_name_entry = Entry(base, font=entry_font)
    first_name_entry.place(x=200, y=90, width=220, height=22)

    last_name_entry = Entry(base, font=entry_font)
    last_name_entry.place(x=200, y=130, width=220, height=22)

    institution_entry = Entry(base, font=entry_font)
    institution_entry.place(x=200, y=170, width=220, height=22)

    address_entry = Entry(base, font=entry_font)
    address_entry.place(x=200, y=220, width=220, height=70)

    city_entry = Entry(base, font=entry_font)
    city_entry.place(x=200, y=320, width=220, height=22)

    India_states = ttk.Combobox(base, font=entry_font, text='-select-', value=I_state)
    India_states.place(x=200, y=370, width=220, height=24)

    countries = ttk.Combobox(base, font=entry_font, values=countries)
    countries.place(x=200, y=420, width=220, height=24)

    e_mail_entry = Entry(base, font=entry_font)
    e_mail_entry.place(x=200, y=470, width=220, height=22)

    mob_entry = Entry(base, font=entry_font)
    mob_entry.place(x=200, y=520, width=220, height=22)

    meals_entry = ttk.Combobox(base, font=entry_font, values=meal)
    meals_entry.place(x=780, y=90, width=220, height=24)

    cash = Checkbutton(base, text='Cash', font=text_font, bg=text_bg)
    cash.place(x=780, y=220)

    cheque = Checkbutton(base, text='Cheque', font=text_font, bg=text_bg)
    cheque.place(x=780, y=260)

    demand_draft = Checkbutton(base, text='Demand Draft', font=text_font, bg=text_bg)
    demand_draft.place(x=780, y=300)

    cheque_entry = Entry(base, font=entry_font)
    cheque_entry.place(x=780, y=350, width=220, height=22)

    bank_entry = Entry(base, font=entry_font)
    bank_entry.place(x=780, y=400, width=220, height=22)

    payable_entry = Entry(base, font=entry_font)
    payable_entry.place(x=780, y=450, width=220, height=22)
    # Button Widgets

    save = Button(base, text='Save', font=text_font, bg='#beebe9')
    save.place(x=410, y=590, width=160, height=30)

    reset = Button(base, text='Reset', font=text_font, bg='#beebe9')
    reset.place(x=660, y=588, width=160, height=30)

    base.mainloop()


label_1 = Label(base, text="Enter user ID:", font=font, bg=text_bg)
label_1.place(x=190, y=100)

txt1 = Entry(base, font=('Times New Roman', 12, 'normal'))
txt1.place(x=340, y=105, width=200, height=23)

label_2 = Label(base, text="Enter password:", font=font, bg=text_bg)
label_2.place(x=190, y=150)

txt2 = Entry(base, width=20, show="*")
txt2.place(x=340, y=156, width=200, height=23)

robot_check = Checkbutton(base, text="I am not a robot", bg=text_bg, font=font)
robot_check.place(x=340, y=200)

sign_in = Button(base, text="Sign-in", font=font, bg='#d4e2d4')
sign_in.place(x=220, y=240)

register = Button(base, text="Reset", font=font, bg='#d4e2d4', command=workshop_reg)
register.place(x=340, y=240)

click_here_for_sign_up = Label(base, text='Click here for Sign-up', foreground='blue', font=font, bg=text_bg)
click_here_for_sign_up.place(x=230, y=300)

base.mainloop()
