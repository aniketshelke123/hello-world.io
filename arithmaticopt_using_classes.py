# - Define a class "ArithOperations" with 6 data-members: n1,n2, add, sub, mul, div
# - Define constructor and input values in constructor.
# - Define one single member-function to perform all arithmetic operations.
# - Define destructor to show all resulting values.
# - Declare two objects of above class.
# - And make proper use/call to constructor, normal member-function and destructor.

class arithmaticOpt():
    addition = None
    subtract = None
    multiply = None
    division = None

    def __init__(self, n1, n2):
        self.num1 = n1
        self.num2 = n2

    def __del__(self):
       print("end")

def arithmatic_calculation(self):
   # a1 = arithmaticOpt()

    addition = self.num1 + self.num2
    subtraction = self.num1 - self.num2
    multiplication = self.num1 * self.num2
    division = self.num1 / self.num2
    return addition, subtraction, multiplication, division

t1 = arithmaticOpt(1,2)
(a, b, c, d) = print(arithmatic_calculation())
print(a)
print(b)
print(c)
print(d)