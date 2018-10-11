class Hexagon:
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 6

hexagon = Hexagon(4)
print(hexagon.calculate_perimeter())
