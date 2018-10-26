class Horse:
    def __init__(self, n, o):
        self.name = n
        self.owner = o

class Rider:
    def __init__(self, n):
        self.name = n


take = Rider("Take Yutaka")
kita = Horse("KitasanBlack", take)
print(kita.owner.name)