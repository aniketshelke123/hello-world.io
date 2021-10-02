import datetime
# from twilio.rest import Client
# from datetime import datetime
# now = datetime.now()

all_studs = []
all_books = []
all_issued = []


class StudentInfo:
    s_roll = None
    s_name = None
    s_class = None
    s_mob = None
    s_email = None

    def accept_stud_info(self):
        self.s_roll = input("Enter Enrollment Number : ")
        self.s_name = input("Enter Student Name : ")
        self.s_class = input("Enter Student Class : ")
        self.s_mob = input("Enter Student Mobile Number : ")
        self.s_email = input("Enter Student Email : ")


class BookInfo:
    b_num = None
    b_title = None
    b_author = None
    b_publication = None

    def accept_book_info(self):
        self.b_num = input("Enter Book Number : ")
        self.b_title = input("Enter Book Title : ")
        self.b_author = input("Enter Book Author : ")
        self.b_publication = input("Enter Book Publication : ")


class IssueInfo:
    b_num = None
    s_roll = None
    issue_date = None
    ret_date = None

    def accept_issue_info(self):
        self.b_num = input("Enter Book number to Issue : ")
        self.s_roll = input("Enter Student Enrollment number to Issue : ")
        #self.issue_date = str(datetime.date.today())
        self.issue_date = datetime.datetime.now()
        self.ret_date = None


def issue_book():
    i1 = IssueInfo()
    i1.accept_issue_info()
    all_issued.append(i1)
    print('=' * 20, end='\n' * 2)
    print("Book Issued..>!")
    print('\n' + '=' * 20)


def return_book():
    print('=' * 20 + '\n')
    ret_bk = input("Enter Book number, which you want to return : ")
    for book in all_issued:
        if book.b_num == ret_bk and book.ret_date is None:
            book.ret_date = datetime.datetime.now()
            print("\n>> Book has been returned Successfully !!")
            break
    else:
        print("\n>> No such book belongs to library !!")
    print('\n' + '=' * 20)


def not_ret_books():
    print('=' * 20 + '\n')
    for ob in all_issued:
        if ob.ret_date is None:    # means this book is not yet returned
            print(">> This book haven't been returned !!")
            print(ob.s_roll, "\t", ob.b_num, "\t", ob.issue_date)
            break
    else:
        print("\n>> All book has already been returned....!!\n")
    print('\n' + '=' * 20)


def add_new_student():
    s1 = StudentInfo()
    s1.accept_stud_info()
    all_studs.append(s1)
    print('=' * 20 + '\n')
    print("New student added...!")
    print('\n' + '=' * 20)


def add_new_book():
    b1 = BookInfo()
    b1.accept_book_info()
    all_books.append(b1)
    print('=' * 20 + '\n')
    print("New Book added...!")
    print('\n' + '=' * 20)


def search_book():
    print('=' * 20 + '\n')
    bk_name = input(">> Enter the book name you want to search: ")
    for book in all_books:
        if book.b_title == bk_name:    # checks if book is in all_books = []
            print(">>>>  Book Found.....!!")
            print(book.b_num, "||", book.b_author, "||", book.b_publication)
            break
    else:
        print(">> NO such book found...!!")
    print('\n' + '=' * 20)


def search_stud():
    print('=' * 20 + '\n')
    st_name = input("Enter Student name you want to search: ")
    for stud in all_studs:
        if stud.s_name == st_name:  # checks for stud_name in all_studs = []
            print(">>> Student Found.....!!")
            print(stud.s_roll, "||", stud.s_name, "||", stud.s_class, "||", stud.s_email)
            break
    else:
        print("\n>> No student found...!!!")
    print('\n' + '=' * 20)


def book_history():
    print('=' * 20 + '\n')
    bk_num = input("Enter book number: ")
    for book in all_issued:
        if book.b_num == bk_num:  # checks in all_issued for book history
            print(book.b_num, "||", book.s_roll, "||", book.issue_date, "||", book.ret_date)
            break
    else:
        print("\n>>> Book haven't been issued yet....!!!")
    print('\n' + '=' * 20)


def stud_history():
    print('=' * 20 + '\n')
    st_num = input("Enter student Enroll number: ")
    for stud in all_issued:
        if stud.s_roll == st_num:  # check student num in all_issued = []
            print(stud.b_num, "||", stud.s_roll, "||", stud.issue_date, "||", stud.ret_date)
            break
    else:
        print("\n>>> Student haven't issued any book...!!")
    print('\n' + '=' * 20)


def send_remainder():
    pass
    # account_sid = "AC637c30642ae5835c32fec20938064650"
    # auth_token = "f67e0fd99943a14bcdf8a99c9b3c1c79"
    # client = Client(account_sid, auth_token)
    #
    # message = client.messages \
    #     .create(
    #         body='This is reminder message from library , kindly return the book within 2 days',
    #         from_='+13367153420',
    #         to='+919423873496'
    #     )
    # print(message.sid)


# main area starts from here
while True:
    print("1 - Issue Book")
    print("2 - Return Book")
    print("3 - Check for not returned books")
    print("4 - Add new Student")
    print("5 - Add new Book")
    print("6 - Search Book Info")
    print("7 - Search Student Info")
    print("8 - Book History")
    print("9 - Student History")
    print("0 - Send return remainders")
    print("* - EXIT")
    ch = input("Provide your choice : ")

    if ch == "1":
        issue_book()
    elif ch == "2":
        return_book()
    elif ch == "3":
        not_ret_books()
    elif ch == "4":
        add_new_student()
    elif ch == "5":
        add_new_book()
    elif ch == "6":
        search_book()
    elif ch == "7":
        search_stud()
    elif ch == "8":
        book_history()
    elif ch == "9":
        stud_history()
    elif ch == "0":
        pass
        # send_remainder()
        #print(">> Message send successfully..!!!")
    elif ch == "*":
        exit(0)
