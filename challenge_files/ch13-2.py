class Square:
    def __init__(self, l):
        self.length = l

    def change_size(self, x):
        self.length += x

sq = Square(10)
print(sq.length)
sq.change_size(10)
print(sq.length)