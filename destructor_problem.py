# - Define a class EmployeInfo with 3 attributes.
# - Define a parameterized constructor to initialize these attributes.
# - Define a destructor to display the values of attributes.
# - Declare 2 objects of this class and use constructor and destructor properly.

class employeeInfo:
    emp_name = None
    emp_id = None

    def __init__(self, p, q):
        self.emp_name = p
        self.emp_id = q

    def __del__(self):
        print("emp_name = ", self.emp_name)
        print("emp_id = ",self.emp_id)


def show_info():
    obj1 = employeeInfo("Sav", 1234)
    obj2 = employeeInfo("Satori", 5879)
    # return t1, t2


print("main area starts")
print(show_info())

print("main area ends")
