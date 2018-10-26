class Square:
    square_list = []

    def __init__(self, s1):
        self.size = s1
        self.square_list.append(self.size)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.size, self.size, self.size, self.size)

sq = Square(40)
print(sq)