class Employee:

    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"
        Employee.num_of_emp += 1


    def full_name(self):
        return f" {self.first}{self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * 0.5)


emp_1 = Employee("aniket", "shelke", 50000)
emp_2 = Employee("test", "main", 40000)

print(Employee.full_name(emp_1))
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(Employee.apply_raise(emp_1))
print(Employee.num_of_emp)