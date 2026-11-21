class person:
    def __init__(self, name, age):
        self.name = name
        self.age =  age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
class student(person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
    def study(self):
        print(self.name, "is studying", self.course)
        s1 = student("Rahul", 20, "python")
        s1.display
        print("course:", s1.course)
        s1.study()
                 
          