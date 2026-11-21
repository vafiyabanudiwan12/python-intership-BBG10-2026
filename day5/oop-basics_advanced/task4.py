class Employee:

    def __init__(self, salary):
        self._salary = salary
        
        def get_salary(self):
         return self._salary
    
    def set_salary(self, new_salary):
        if new_salary > self._salary:
            self._salary = new_salary
            print("Salary increased successfully")
        else:
          print("Salary cannot be decreased")
        
    e = Employee(30000) 
    
    print("Old salary:", e.get_salary())
    
    e.set_salary(40000)
    
    print("New salary:", e.get_salary())
                      
            