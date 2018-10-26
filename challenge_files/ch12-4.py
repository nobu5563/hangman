class Hexagon:
    def __init__(self, w1, w2, w3, w4, w5, w6):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.w4 = w4
        self.w5 = w5
        self.w6 = w6

    def calculate_perimeter(self):
        return self.w1 + self.w2 + self.w3 + self.w4 + self.w5 + self.w6

hexagon = Hexagon(1,2,3,4,5,6)
print(hexagon.calculate_perimeter())