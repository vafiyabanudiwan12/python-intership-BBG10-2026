class vahicle:
    def __init__(self, brand):
        self.brand = brand
class car(vahicle):
    def __init__(self, brand, model,speed):
        super().__init__(brand)
        self.model = model
class sportscar(car):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model,)
        self.speed = speed
    def display_into(self):
        print("Brand:",self.brand)
        print("model:",self.model)
        print("speed:",self.speed, "km/h")
        
        s1 = sportscar("Ferrari","488",330)
        s1.display_into()
        