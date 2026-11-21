class car:
 def _init_(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
    
    def display_info(self):
        print(f"Brand: {self.brand}, model: {self.model}, year: {self,year}")
    car1 = car("Toyota","fortuner",2022)
    car2 = car("honda","city", 2023)
    car3 = car("tota","nexon", 2024)
        
    car1.display_info()
    car2.display_info()
    car3.display_info()
    
    