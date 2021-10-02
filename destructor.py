class Test:
    def __init__(self):
        print("This is constructor")

    def __del__(self):
        print("This is destructor")


def sample():
    print("sample starts")

    print("sample ends")

print("main area starts")
t1 = Test()
print("main area ends")
del t1