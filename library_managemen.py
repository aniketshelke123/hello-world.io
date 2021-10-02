import pprint

all_students = {}
all_books = {}
all_issued_books = {}
all_returned_books = {}
student_history = {}
book_history = {}


class StudentInfo:
    s_name = None
    s_enroll = None
    s_mob = None
    s_email = None

    def __init__(self, s_name, s_enroll, s_mob, s_email):
        self.s_name = s_name
        self.s_enroll = s_enroll
        self.s_mob = s_mob
        self.s_email = s_email

    def add_new_student(self):
        all_students[self.s_name] = [f"enroll_no = {self.s_enroll} || mobile = {self.s_mob} ||"
                                     f" e-mial = {self.s_email}"]


class NewBookInfo:
    book_num = None
    book_name = None
    book_author = None

    def __init__(self, book_name, book_num, book_author):
        self.book_name = book_name
        self.book_num = book_num
        self.book_author = book_author

    def add_new_book(self):
        all_books[self.book_name] = [f"book_id = {self.book_num} || book_author = {self.book_author}"]


class IssueBookInfo:
    s_name = None
    s_enroll = None
    book_num = None
    book_name = None
    issue_date = None

    def __init__(self, s_name, s_enroll, book_num, book_name, issue_date):
        self.s_name = s_name
        self.s_enroll = s_enroll
        self.book_num = book_num
        self.book_name = book_name
        self.issue_date = issue_date

    def issue_book(self):
        for key, value in all_books.items():
            if self.book_name == key:
                    all_issued_books[self.book_name] = [f" book_id = {self.book_num} || enroll_no = {self.s_enroll} "
                                                    f"|| {self.s_name} ||  {self.issue_date}"]
                    student_history[self.s_name] = [f"enrol_no = {self.s_enroll} || book_id = {self.book_num} ||"
                                                 f"{self.book_name} || {self.issue_date}"]
                    book_history[self.book_name] = [f"{self.s_name} || enroll_no = {self.s_enroll} || book_id ="
                                                f" {self.book_num} || {self.issue_date}"]
                    return True
        return False


class ReturnBookInfo:
    s_name = None
    s_num = None
    book_name = None
    book_num = None
    return_date = None
    book_author = None

    def __init__(self, s_name, s_enroll, book_num, book_name, book_author, return_date):
        self.s_name = s_name
        self.s_enroll = s_enroll
        self.book_num = book_num
        self.book_name = book_name
        self.book_author = book_author
        self.return_date = return_date

    def return_book(self):
        for key, value in all_issued_books.items():
            if self.book_name == key:
                all_returned_books[f"{self.book_name}"] = [f"{self.s_name} || enroll_no = {self.s_enroll} ||"
                                                        f"book_ID = {self.book_num} || ret_date = {self.return_date}"]
                #all_books[self.book_name] = [f"book_id = {self.book_num} || book_author = {self.book_author}"]
                return True
        return False


def search_student():
    print("Search by student name: ")
    s_name = input("Enter student name: ")
    for key, value in all_students.items():
        if s_name == key:
            return True, value
    return False, value


def search_book():
    print("Search by book name")
    b_name = input("Enter book name: ")
    for key, value in all_books.items():
        if b_name == key:
            return True, value
    return False, value


def search_student_history():
    print("Search by student name")
    name = input("Enter Student name: ")
    for key, value in student_history.items():
        if name == key:
            return True, value
    return False, value


def search_book_history():
    print("search by book name")
    b_name = input("Enter book name: ")
    for key, value in book_history.items():
        if b_name == key:
            return True, value
    return False, value


def check_not_ret_book():
    print("check by book name")
    b_name = input("Enter book name: ")
    for key, value in all_issued_books.items():
        if b_name == key:
            return True, value
    return False, value


while True:
    print("1 - issue book")
    print("2 - Add new student")
    print("3 - Add new book")
    print("4 - Return book")
    print("5 - Search Book Info")
    print("6 - Search Student Info")
    print("7 - Student History")
    print("8 - Book History")
    print("9 - Check for not returned books")
    print("0 - exit")
    ch = int(input("Provide your choice : "))

    if ch == 1:
        s_name = input("Enter student name: ")
        s_enroll = input("Enter student enroll (starts with EN): ")
        book_num = int(input("Enter book ID: "))
        book_name = input("Enter book name: ")
        issue_date = input("Enter issue date in format dd/mm/yy: ")

        i1 = IssueBookInfo(s_name, s_enroll, book_num, book_name, issue_date)
        if i1.issue_book():
            print("=========================================\n")
            pprint.pprint(all_issued_books)
            print("~~~~~~Book issued successfully~~~~~~")
        else:
            print("=========================================")
            print("\n>>>> Book NOT available in library  !!!")
        print("\n========================================")

    if ch == 2:
        s_name = input("Enter student name: ")
        s_enroll = input("Enter enroll number (start with EN): ")
        s_mob = input("Enter mobile number: ")
        s_email = input("Enter email address: ")
        s1 = StudentInfo(s_name, s_enroll, s_mob, s_email)
        s1.add_new_student()
        print("=============================================\n")
        pprint.pprint(all_students)
        print("\n~~~~~~New student successfully added~~~~~~")
        print("=============================================")

    if ch == 3:
        book_name = input("Enter book name: ")
        book_num = input("Enter book ID: ")
        book_author = input("Enter book author: ")
        n1 = NewBookInfo(book_name, book_num, book_author)
        n1.add_new_book()
        print("===========================================\n")
        pprint.pprint(all_books)
        print("\n~~~~~~New Book added to library~~~~~")
        print("===========================================")

    if ch == 4:
        s_name = input("Enter student name: ")
        s_enroll = input("Enter student enroll: ")
        book_num = input("Enter book ID: ")
        book_name = input("Enter book name: ")
        book_author = input("Enter book author: ")
        return_date = input("Enter return date:")
        r1 = ReturnBookInfo(s_name, s_enroll, book_num, book_name, book_author, return_date)
        if r1.return_book():
            print("===========================================\n")
            pprint.pprint(all_returned_books)
            print("\n~~~~~~Book returned successfully~~~~~")
        else:
            print("===========================================\n")
            print(">>>> This book haven't been issued  !!!")
        print("\n===========================================")

    if ch == 5:
        t, value = search_book()
        if t:
            print("=========================================\n")
            print("book Available in library!!")
            print(value)
        else:
            print("===========================================")
            print("\n>>>>  No book Found!!!!")
        print("\n==========================================")

    if ch == 6:
        ret, value = search_student()
        if ret:
            print("========================================\n")
            print(">>>> Student found!!!")
            print(value)
        else:
            print("=======================================")
            print("\n>>>>  Student Not Found !!!")
        print("\n========================================")

    if ch == 7:
        a, value = search_student_history()
        if a:
            print("========================================\n")
            print(">>>>  Student History:")
            print(value)
        else:
            print("===========================================\n")
            print(">>>> This student hasn't issued any book yet!!!")
        print("\n===========================================")

    if ch == 8:
        a, value = search_book_history()
        if search_book_history():
            print("\n")
            print("Book History:")
            pprint.pprint(value)

        else:
            print("\n")
            print("This Book haven't been issued yet!!!")
        print("\n===========================================")

    if ch == 9:
        f, value = check_not_ret_book()
        if f:
            print("============================================\n")
            print(">>>>  book not returned !!! ")
            pprint.pprint(value)
        else:
            print("\n>>>>  Book not found!!!")
        print("\n============================================")

    if ch == 0:
        break



