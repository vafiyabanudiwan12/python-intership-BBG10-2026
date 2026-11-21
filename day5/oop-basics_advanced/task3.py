import math
class circle:
    def __init__(self, radius):
        self. radius = radius
        @property
        def  area(self):
            return math.pi * self.radius **2
        
        @property
        def circumference(self):
            return 2 * math.pi * self.radius
        c = circle(5)
        print("Area:", c.area)
        print("circmference:",c.circumfernce)
        