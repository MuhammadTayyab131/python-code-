class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

class Employ(Person):
  def __init__(self,fname,lname, join_date):
    super().__init__(fname,lname)
    self.employ_join_date = join_date

  def welcome(self):
    print(self.firstname, self.lastname, "joined this company on " , self.employ_join_date)


x = Student("Mike", "Olsen", 2024)
x.welcome()

y = Employ ("Muhammad","Tayyab", 2025)
y.welcome()






class MyNumbers:
  def iter_number (self):
    for x in range(1,21):
      print(x)


z = MyNumbers()
z.iter_number()
