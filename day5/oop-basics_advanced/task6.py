class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def __eq__(self, other):
        return self.area() == other.area()
    
r1 = rectangle(4, 6)
r2 = rectangle(3, 8)

print("rectangle 1 area:", r1.area())
print("rectangle 2 area:",r2.area())

print("both rectangle equal:", r1 == r2)
