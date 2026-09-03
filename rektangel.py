class Rektangel:
    def __init__(self, höjd, bredd):
        self.höjd = höjd
        self.bredd = bredd

    def area(self):
        return self.höjd * self.bredd

    def omkrets(self):
        return 2 * (self.höjd + self.bredd)

    def set_höjd(self, höjd):
        self.höjd = höjd

    def visa_info(self):
        print("self.höjd, self.bredd")

Rektangel1 = Rektangel(3, 4)
Rektangel1.set_höjd(7)

print(Rektangel1.visa_info())
print("Area:", Rektangel1.area())
print("Omkrets:", Rektangel1.omkrets())