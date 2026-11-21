class employee:
    def calculate_salary(self):
        return 30000
class Developer(employee):
    def calculate_salary(self):
        return 
    super().calculate_salary() +  10000
class Designer(employee):
    def calculate_salary(self):
        return
    super().calculate_salary()  + 50000
e1  = Developer()
e2  = Designer()
print("Developer salary:",e1.calculate_salary())
print("Designer salary:", e2.calculate_salary())

    
    
    