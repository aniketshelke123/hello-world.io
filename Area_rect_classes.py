# 4. Write a program to print the area of a rectangle by creating a class named 'Area' having two functions.
# First function named
# as 'setDimensions()' takes the length and breadth of the rectangle as parameters and the second function named
# as 'getArea()' returns the area of the rectangle.
#  Length and breadth of the rectangle are entered through keyboard.


class Area:
    length = None
    breadth = None

    def set_dimension(self, l, b):
        self.length = l
        self.breadth = b

    def get_area(self):
        area_of_rect = self.length * self.breadth
        return area_of_rect


length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))

obj = Area()
obj.set_dimension(length, breadth)
print(obj.get_area())


