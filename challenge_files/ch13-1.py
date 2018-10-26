class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2

class Square:
    def __init__(self, s):
        self.size = s

    def calculate_perimeter(self):
        return self.size * 4

rec = Rectangle(3, 4)
sq = Square(5)
print(rec.calculate_perimeter())
print(sq.calculate_perimeter())