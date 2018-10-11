class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def rectangle_calculate_perimeter(self):
        return self.width * 2 + self.len * 2

class Square(Shape):
    def __init__(self, s1):
        self. s1 = s1

    def square_calculate_perimeter(self):
        return self.s1 * 4

    def square_change_size(self, c):
        self.s1 += c
        #print(self.s1)

class Horse:
    def __init__(self, n, a):
        self.name = n
        self.age = a

class Rider:
    def __init__(self, n, w, h):
        self.name = n
        self.weight = w
        self.horse = h


rectangle = Rectangle(10, 3)
print(rectangle.rectangle_calculate_perimeter())
rectangle.what_am_i()

square = Square(12)
print(square.square_calculate_perimeter())
square.square_change_size(-5)
print(square.s1)
square.what_am_i()

kitasan_black = Horse("Kitasan black", 5)
rider = Rider("Yutaka Take", 57, kitasan_black)
print(rider.horse.name, rider.horse.age)
print(rider.name, rider.weight)
