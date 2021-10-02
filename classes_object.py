
class StudentInfo:
    sroll = None
    sname = None

    def accept_details(amey):
        print("Enter roll number ")
        amey._sroll = input()
        print("Enter name")
        amey.__sname = input()
        amey.__foo = 200

    def show_details(self):
        print("Roll number is : ", self._sroll)
        print("Name is : ", self.__sname)

print("main area starts")
s1 = StudentInfo()
s1.accept_details()
s1.show_details()
print(s1._StudentInfo__foo)
print("main area ends")
