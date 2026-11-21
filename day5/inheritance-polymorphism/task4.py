class Bird:
    def fly(self):
        print("Bird is flying")
class Airplane:
    def fly(self):
        print("Airplane is flying")

class Drone:
    def fly(self):
      print("Drone is flying")
    
def make_fly(odj):
        odj.fly()

b = Bird()
a = Airplane()    
d = Drone()

make_fly(b)
make_fly(a)
make_fly(d)
    
                        