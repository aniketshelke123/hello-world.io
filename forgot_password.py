from tkinter import *
import random

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
