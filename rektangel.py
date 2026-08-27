class Rektangel:
    def __init__(self, x, y, höjd, bredd):
        self.x = x
        self.y = y
        self.höjd = höjd
        self.bredd = bredd

    def area(self):
        return self.höjd * self.bredd

    def omkrets(self):
        return 2 * (self.höjd + self.bredd)

r = Rektangel(10, 20, 5, 8)

print("Area:", r.area())
print("Omkrets:", r.omkrets())