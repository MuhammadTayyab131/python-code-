# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Derived class: Student
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def show_info(self):
        super().show_info()
        print(f"Grade: {self.grade}")

# Derived class: Teacher
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_info(self):
        super().show_info()
        print(f"Subject: {self.subject}")

# Using the classes
student1 = Student("Ali", 15, "9th")
teacher1 = Teacher("Ms. Sara", 30, "Mathematics")

print("Student Info:")
student1.show_info()

print("\nTeacher Info:")
teacher1.show_info()


class Animal:
    def __init__(self,name):
        self.name=name

    def sound (self):
        print("sound of some animals")

    def show_info (self):
        print(f"Name: {self.name}")


class Dog(Animal) :
    def __init__(self,name):
        super().__init__(name)
        
    def sound (self):
        print(f"{self.name} sounds like \"wooof\" ")

    def color (self) :
        print(f"color of {self.name} is black and brown")

class Cat(Animal) :
    def __init__(self,name):
        super().__init__(name)
        
    def sound (self):
        print(f"{self.name} sounds like \"Meow\" ")

    def color (self) :
        print(f"color of {self.name} is white")

dog = Dog("oskar")
cat = Cat("bella")

dog.show_info()
dog.sound()
dog.color()
cat.show_info()
cat.sound()
cat.color()



animals = [Dog("oskar"), Cat("bella")]
for animal in animals:
    animal.sound()


# Single Inheritance Class:

class Vehicle :
    def start (self):
        print("Vehicle is started")

class car(Vehicle):
    def drive (self):
        print("car is driving")

car1 = car()
car1.start()
car1.drive()
        
# Multiple Inheritance Class:

class Flyer :
    def fly (self):
        print("Duck is flying")

class Swimmer :
    def swim (self):
        print("Duck is swmming")

class Duck (Flyer,Swimmer) :
    pass

duck1 = Duck ()
duck1.fly()
duck1.swim()


# Multilevel Inheritance — Task:

class Person :
    def walk(self):
        print("A person is walking")

class Student(Person):
    def study (self):
        print("Student is studing")

class CollegeStudent (Student):
    def project(self):
        print("College student is doing a project")

clg_stud = CollegeStudent()
clg_stud.walk()
clg_stud.study()
clg_stud.project()



# Hierarchical Inheritance — Task:


class Shape:
    def display(self):
        print("this is a Shape")

class Circle(Shape):
    def area (self):
        print("Area of circle is 78.5")

class Rectangle(Shape):
    def area (self):
        print("Area of Rectangle is 40")

class Triangle (Shape):
    def area (self):
        print("Area oftriangle is 30.0")


c = Circle() 
r = Rectangle()
t = Triangle()

c.display()
c.area()

r.display()
r.area()

t.display()
t.area()

# new tasks 




