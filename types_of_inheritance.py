# 🔹 1. Single Inheritance — Task
# Create a Parent class with a method greet(). Then create a Child class that inherits it and adds introduce().

class Parent :
    def greet (self):
        print("Assalam U Alikum From Parents!")

class Child(Parent):
    def info (self):
        print("I am Tayyab")        

all = Child()
all.greet()
all.info()


# 🔹 2. Multiple Inheritance — Task
# Create class Artist with draw() and class Coder with code(). Create a class CreativePerson that inherits both and uses both methods.

class Draw:
    def draw (self):
        print("i am drawing a picture")
class Coder :
    def code (self):
        print("i am writing a code")
class CreativePerson(Draw,Coder):
    pass

both = CreativePerson()
both.draw()
both.code()


# 🔹 3. Multilevel Inheritance — Task
# Create class Grandparent with legacy(), then Parent that inherits and adds guidance(), and Child that adds dream().



class GrandParent:
    def legacy (self):
        print("You have only earned a money, but I have earned a Legacy.")

class parnett(GrandParent):
    def guidance (self):
        print("Stick to the words of your ancestors.")

class Child (parnett):
    def dream (self):
        print("I want to be cricketer")


offspring = Child()
offspring.legacy()
offspring.guidance()
offspring.dream()


# 🔹 4. Hierarchical Inheritance — Task
# Create a class Animal with breathe(). Then make Fish and Bird inherit from Animal and each add their own method.


class Animal:
    def breathe(self):
        print("Animal is breathing")

class Fish(Animal):
    def method (self):
        print("Fish is swimming")     

class Bird(Animal):
    def method (self):
        print("Bird is flying")


animal_1 = Fish()           
animal_2 = Bird()

animal_1.breathe()
animal_1.method()

animal_2.breathe()
animal_2.method()


# 🔹 5. Hybrid Inheritance — Task
# Create class Employee with work(), class Trainer with train(), and class Manager that inherits from both. Add a final class TeamLead that inherits from Manager.


class Employee:
    def work(self):
        print("Employee is working")

class Trainer:
    def train(self):
        print("trainer is training")

class Manager(Employee, Trainer):
    def manage(self):
        print("Manager is managing")

class Team_Lead(Manager):
    def leading(self):
        print("Team Lead is leading the team")

papa_of_all = Team_Lead()
papa_of_all.work()
papa_of_all.train()
papa_of_all.manage()
papa_of_all.leading()


class Bank:
    def bank(self):
        print("HBL: (Habib Bank limited)")
class School:
    def school(self):
        print("APS: (Army Public School)")
class Vehical:
    def vehical(self):
        print("BMW: (Bayerische Motoren Werke)")                 

class MushtarkaChild(Bank,School,Vehical):
    pass

a = MushtarkaChild()
a.bank()
a.school()
a.vehical()


