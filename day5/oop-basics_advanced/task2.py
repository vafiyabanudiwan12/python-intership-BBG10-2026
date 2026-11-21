class counter:
 count = 0
def  _init_(self):
    counter.count += 1
    @classmethod
    def get_conut(cls):
        return cls.count 
    c1 = counter()
    c2 = counter()
    c3 = counter()
    c4 = counter()
    c5 = counter() 
    
    print("Total objects:", counter.get_count())
    