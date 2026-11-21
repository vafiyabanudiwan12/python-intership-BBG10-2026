class temperature:
    def __init__(self, celsius):
        self.celsius = celsius
        
    @property
    def celsius(self):
        return self._celsius 
    @celsius.setter
    def celsius(self, value):
        if value<-273.15:
            raise ValueError("invaild temperature")
        self._celsius = value
    @property
    def kelvin(self):
        return self._celsius + 273.15
    
t = temperature(25)
    
print("celsius:", t.celsius)        
print("kelvin:", t.kalvin)            