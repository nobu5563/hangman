class Shape:
    def what_am_i(self):
        print("I am shape")

class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2

class Square(Shape):
    def __init__(self, s):
        self.size = s

    def calculate_perimeter(self):
        return self.size * 4

rec = Rectangle(5, 6)
sq = Square(7)
rec.what_am_i()
sq.what_am_i()



