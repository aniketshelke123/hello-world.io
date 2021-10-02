class StudentInfo:
    sroll = None
    sname = None

    def __init__(self, r, n):
        self.sroll = r
        self.sname = n
    def __del__(self):
        print("this is destructor")

    def show_info(self):
        print("Roll number is :", self.sroll)
        print("Name is :", self.sname)

print("\nmain area starts")

s1 = StudentInfo(15, "Ajay") # <--- invokes parameterized constructor
s2 = StudentInfo(20, "Sumit")  # <--- invokes parameterized constructor
print("\nInfo of first student")
s1.show_info()
print("\nInfo of second student")
s2.show_info()

print("\nmain area ends")