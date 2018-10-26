class Square:
    square_list = []

    def __init__(self, s1):
        self.size = s1
        self.square_list.append(self.size)

r1 = Square(5)
r2 = Square(6)
r3 = Square(7)

print(Square.square_list)