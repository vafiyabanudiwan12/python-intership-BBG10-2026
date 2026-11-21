class point:
 def _init_(self, x, y):
     self.x = x
     self.y = y
     def _eq_(self, other):
         return self.x == other.x and self.y ==other.y
     def _str_(self):
         return f"({self.x}, {self.y})"
     p1= point(2,3)
     p2= point(2,3)
     print(p1)
     print(p1 == p2)
     
    