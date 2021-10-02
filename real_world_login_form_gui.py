from tkinter import *
import random
base = Tk()
base.title("Sign_in & Sign_up form")
base.geometry("650x400")
base.configure(bg='#c6ebc9')
text_bg = '#c6ebc9'
font = ('Times New Roman', 15)


photo = PhotoImage(file=r'C:\Users\Lenovo\Downloads\UIHere.png')

def sign_in():
    with open('user_info.txt', 'r') as f_file:
        user_data_list = list(f_file.readlines())
        f_file.close()
        for data in user_data_list:
            ls = data.split(",")
            if ls[0] == user_id.get():
                if ls[1] == password.get():
                    login = 'Login Successfull..!!'
                    log = Label(base, font=font, fg="red", bg=text_bg, text=login)
                    log.place(x=250, y=270)
                    base.after(2000, log.destroy)
            else:
                login = 'Login Failed...!!'
                log = Label(base, font=font, fg='red', bg=text_bg, text=login )
                log.place(x=250, y=270)
                base.after(2000, log.destroy)


# start of sign-up page.................................
def sign_up_page(event):
    base1 = Tk()
    base1.title('sign-up form')
    base1.geometry('650x600')
    base1.configure(bg='#c6ebc9')
    text_bg = '#c6ebc9'
    font = ('Times New Roman', 15)
    entry_font = ('Times New Roman', 15)

    def save_user_info():
        user = user_entry.get()
        pass_word = pass_entry.get()
        con_password = con_pass_entry.get()
        e_mail = email_entry.get()
        mobile_no = mob_entry.get()
        if pass_word == con_password:
            with open('user_info.txt', 'a') as f_file:
                f_file.write(f'{user},{pass_word},{con_password},{e_mail},{mobile_no}, \n')
                f_file.close()
                selected = 'New User created Successfully..!!'
                display_saved.configure(text=selected, font=font, foreground='#6b011f')
                base.after(2000, display_saved.destroy)
        elif pass_word != con_password:
            wrong_password = "Password doesn't Match"
            wrong = Label(base1, bg=text_bg, font=font, fg='#ce1212', text=wrong_password)
            wrong.place(x=235, y=500)
            base.after(2000, wrong.destroy)

    def reset_entry_widgets():
        user_entry.get()
        pass_entry.get()
        con_pass_entry.get()
        email_entry.get()
        mob_entry.get()
        user_entry.delete(0, END)
        pass_entry.delete(0, END)
        con_pass_entry.delete(0, END)
        email_entry.delete(0, END)
        mob_entry.delete(0, END)
        user_entry.focus()

    # label widgets

    user_id = Label(base1, text="Enter user ID:", font=font, bg=text_bg)
    user_id.place(x=100, y=80)

    password = Label(base1, text="Enter password:", font=font, bg=text_bg)
    password.place(x=100, y=140)

    confirm_pass = Label(base1, text="confirm password:", font=font, bg=text_bg)
    confirm_pass.place(x=100, y=200)

    email = Label(base1, text="Enter E-mail", font=font, bg=text_bg)
    email.place(x=100, y=260)

    mobile = Label(base1, text="Enter mobile no", font=font, bg=text_bg)
    mobile.place(x=100, y=320)

    display_saved = Label(base1, bg=text_bg)
    display_saved.place(x=210, y=480)

    # entry widgets

    user_entry = Entry(base1, font=entry_font)
    user_entry.place(x=280, y=80, width=220, height=22)

    pass_entry = Entry(base1, font=entry_font)
    pass_entry.place(x=280, y=140, width=220, height=22)

    con_pass_entry = Entry(base1, font=entry_font)
    con_pass_entry.place(x=280, y=200, width=220, height=22)

    email_entry = Entry(base1, font=entry_font)
    email_entry.place(x=280, y=260, width=220, height=22)

    mob_entry = Entry(base1, font=entry_font)
    mob_entry.place(x=280, y=320, width=220, height=22)

    # button widgets

    create_button = Button(base1, width=10, text="Sign-in", font=font, bg='#d4e2d4', command=save_user_info)
    create_button.place(x=160, y=420)

    reset_button = Button(base1, width=10, text="Reset", font=font, command=reset_entry_widgets)
    reset_button.place(x=360, y=420)

    base1.mainloop()
# end of sign-up page............................................................................

# start of forgot password....................................................................
def forgot_password(event):
    base2 = Tk()
    base2.title('Forgot password')
    base2.geometry('600x550')
    base2.configure(bg='#feffde')
    text_bg = '#feffde'
    font = ('Times New Roman', 15)
    entry_font = ('Times New Roman', 15)
    rand = random.randint(100, 500)


    def send_otp():
        with open('user_info.txt', 'r') as f_obj:
            user_data_list = list(f_obj.readlines())
            for data in user_data_list:
                ls = data.split(",")
                if ls[0] == user_entry.get():
                    otp_entry.configure(state='normal')
                    # account_sid = "AC637c30642ae5835c32fec20938064650"
                    # auth_token = "f67e0fd99943a14bcdf8a99c9b3c1c79"
                    # client = Client(account_sid, auth_token)
                    #
                    # message = client.messages \
                    #     .create(
                    #         body=rand,
                    #         from_='+13367153420',
                    #         to=ls[4]
                    #     )
                    # print(message.sid)
                    print('rand:', rand)
                    otp_send = 'OTP send..!'
                    ot = Label(base2, text=otp_send, font=("Verdana", 10, 'italic'), fg='#9b3675', bg="#fbe2e5")
                    ot.place(x=240, y=170)
                    base2.after(2000, ot.destroy)
                elif ls[0] != user_entry.get():
                    wrong = 'Wrong user_id'
                    wrong_id = Label(base2, text=wrong, font=('Verdana', 10, 'italic'), fg="#fa1e0e", bg="#fbe2e5")
                    wrong_id.place(x=240, y=170)
                    base2.after(2000, wrong_id.destroy)

    def verify_otp(event):
        if str(rand) == str(otp_entry.get()):
            pass_entry.configure(state='normal')
            con_pass_entry.configure(state='normal')
            create = 'Create New Password'
            create_password_label = Label(base2, text=create, font=entry_font, fg="#fa1e0e", bg="#fbe2e5")
            create_password_label.place(x=240, y=260)
            base2.after(3000, create_password_label.destroy)
        elif str(rand) != str(otp_entry.get()):
            print(rand)
            failed = 'Wrong OTP..'
            try_label = Label(base2, text=failed, font=entry_font, fg="#fa1e0e", bg="#fbe2e5")
            try_label.place(x=240, y=260)
            base2.after(3000, try_label.destroy)

    def new_password():
        if pass_entry.get() == con_pass_entry.get():
            new_pass = pass_entry.get()
            with open('user_info.txt') as the_file:
                all_lines = the_file.readlines()

            with open('user_info.txt', 'w') as the_file:
                for line in all_lines:
                    contents = line.split(',')
                    if contents[0] == user_entry.get():
                        contents[1] = contents[2] = new_pass
                    new_line = ','.join(contents)
                    the_file.write(new_line)

                    tex = 'New password Saved..!'
                    password_saved_Label = Label(base2, text=tex, font=('Verdana', 11, 'normal'), fg="#f58634", bg="#fbe2e5")
                    password_saved_Label.place(x=200, y=400)
                    base2.after(2000, password_saved_Label.destroy)
                    pass_entry.configure(state='disabled')
                    con_pass_entry.configure(state='disabled')
                    user_entry.configure(state='disabled')
                    otp_entry.configure(state='disabled')
                    otp.configure(state='disabled')
        else:
            tex = "Passwords doesn't match..!"
            password_saved_Label = Label(base2, text=tex, font=('Verdana', 11, 'normal'), fg="#f05454", bg="#fbe2e5")
            password_saved_Label.place(x=200, y=400)
            base2.after(2000, password_saved_Label.destroy)

    # label widgets
    user_id = Label(base2, text="Enter user ID:", font=font, bg=text_bg)
    user_id.place(x=80, y=50)

    enter_otp = Label(base2, text="Enter OTP", font=font, bg=text_bg)
    enter_otp.place(x=80, y=210)

    verify_label = Label(base2, text="Verify otp..!", font=('Times New Roman', 13, 'underline'), fg='#ff005c', bg=text_bg)
    verify_label.bind("<Button>", verify_otp)
    verify_label.place(x=460, y=210)

    password_label = Label(base2, text="Enter New password", font=font, bg=text_bg)
    password_label.place(x=80, y=310)

    con_pass_label = Label(base2, text="Confirm New password", font=font, bg=text_bg)
    con_pass_label.place(x=80, y=360)

    # entry widgets

    user_entry = Entry(base2, font=entry_font)
    user_entry.place(x=200, y=50, width=220, height=22)

    otp_entry = Entry(base2, font=entry_font)
    otp_entry.configure(state='disabled')
    otp_entry.place(x=200, y=210, width=220, height=22)

    pass_entry = Entry(base2, font=entry_font)
    pass_entry.configure(state='disabled')
    pass_entry.place(x=290, y=310, width=220, height=22)

    con_pass_entry = Entry(base2, font=entry_font)
    con_pass_entry.configure(state='disabled')
    con_pass_entry.place(x=290, y=360, width=220, height=22)

    # button widgets

    otp = Button(base2, text="Send OTP", font=font, bg='#fbe0c4', command=send_otp)
    otp.place(x=240, y=120)

    change_pass_button = Button(base2, width=16, text="Change Password", font=font, bg='#d4e2d4', command=new_password)
    change_pass_button.place(x=200, y=450)

    base2.mainloop()
# end of forgot password.............................................................................


label_1 = Label(base, text="Enter user ID:", font=font, bg=text_bg)
label_1.place(x=190, y=80)

user_id = Entry(base, font=('Times New Roman', 12, 'normal'))
user_id.place(x=340, y=85, width=200, height=23)

label_2 = Label(base, text="Enter password:", font=font, bg=text_bg)
label_2.place(x=190, y=130)

password = Entry(base, width=20, show="*")
password.place(x=340, y=136, width=200, height=23)

robot_check = Checkbutton(base, text="I am not a robot", bg=text_bg, font=font)
robot_check.place(x=340, y=180)

sign_in = Button(base, text="Sign-in", font=font, bg='#d4e2d4', command=sign_in)
sign_in.place(x=220, y=220)

register = Button(base, text="Reset", font=font, bg='#d4e2d4')
register.place(x=340, y=220)

click_here_for_sign_up = Label(base, text='New user? sign-up here', foreground='blue',
                               font=('Times New Roman', 15, 'underline'), bg=text_bg)
click_here_for_sign_up.bind('<Button>', sign_up_page)
click_here_for_sign_up.place(x=230, y=300)

forgot_pass = Label(base, text='Forgot Password', foreground='blue', font=
                               ('Times New Roman', 15, 'underline'), bg=text_bg)
forgot_pass.bind("<Button>", forgot_password)
forgot_pass.place(x=230, y=330)
base.mainloop()
