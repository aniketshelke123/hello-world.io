# - Define a class "StudentInfo" with 3 attributes.
# - Define a method to accept the values of these attributes.
# - Define another method to show the values of these attributes.
# - Declare 2 objects of this class to accept and display information of two students

class studentInfo:
    sroll = None
    sname = None
    smobno = None

    def __init__(self, p, q, r):
        self.sroll = p
        self.sname = q
        self.smobno = r
    def __del__(self):
        print("ends")

    def showInfo(self):
        print("roll no is: ", self.sroll)
        print("name is : ", self.sname)
        print("mobile no is: ", self.smobno)

t1 = studentInfo(10, "Sav", 4558554)
t2 = studentInfo(20, "gojo", 455452)

print("info of first student")
t1.showInfo()
print("\n")
print("info of second student")
t2.showInfo()
print("\n")
print("main area ends")


