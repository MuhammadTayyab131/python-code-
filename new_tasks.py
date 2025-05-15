

# string = "apple banana apple orange"


# list = string.split()
# print(list)
# dict = {}
# for i,x in enumerate(list):
#       dict[x] = i+1

# print(dict)

# k_tuple = tuple(dict.keys())

# print("keys",k_tuple)




# # function's body


# def str_dic_tup (str):
#     lis = str.split()
#     print("str to lis\t",lis)

# dict = {}
# for i,v in enumerate(list):
#       if v not in dict:
#            dict[v] = i
      
# print("list to dict\t",dict)    


# tup = tuple(dict.keys())
# print("key values of dict\t",tup)



# # calling function
# str = "apple banana apple orange"
# str_dic_tup(str)

# # CRUD in list


# my_list = []

# my_list.append("Tayyab")
# my_list.append("kaleem")
# my_list.append("abrar")


# print("Original List:  ",my_list)
# print("element on 1 index: ",my_list[1])
# my_list[1] = "Hello"
# print("List after updating:   ",my_list)
# my_list.remove("abrar")
# print("After deleting an element list is:    ", my_list)



# my_list = []

# my_list.append(1)
# my_list.append(2)
# my_list.append(3)


# print("Original List:  ",my_list)
# print("element on 1 index: ",my_list[1])
# my_list[1] = "Hello"
# print("List after updating:   ",my_list)
# my_list.remove(3)
# print("After deleting an element list is:    ", my_list)




# a = list(input("Enter list Elements:  "))
# a_list = []

# a_list.extend(a)

# d = int(input("enter index bumber you want see: "))

# print(f"The Element on idex no {d} is:  ",a_list[d])

# e = int(input("Enter the index number you want to update: "))
# n = int(input("Enter new Element: "))

# a_list[e] = n

# print("list after update:  ",a_list)

#function body
# def even_odd (num):
#     even = []
#     odd = []
#     for i in num:
#       if i % 2 == 0:
#         even.append(i)
#       else:
#         odd.append(i)

     

#     print("even list:  ",even)        
#     print("odd list:  ",odd)

# # calling function
# my_array = [0,1,2,3,4,5,6,7,8,9]
# even_odd (my_array)


# new_list = [1,2,3,4,5,6,7,8,9,10]
# # new_list[3] = 15
# new_list.insert(3, 15)
# print(new_list)

# my_tuple = (1,2,3,3)


# my_set = {1,2,3,4,5,6,7}
# my_set.add(8)
# print(my_set)


# check_even_odd_1 = lambda number: "Even" if number % 2 == 0 else "Odd"

# # print(check_even_odd_1 (7))


# e_o = lambda x : "even" if x %2==0 else "odd"
# # x = int(input("enter any number"))
# print(e_o(x = int(input("enter any number: "))))

# squ_odd = lambda v : v*v if v %2!=0 else v
# print(squ_odd(list(input("enter a list"))))


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)



# # Defining a Car class with more attributes and a drive method
# class Car:
#     def __init__(self, brand, model, year, color,tyre):
#         self.brand = brand      # Car's brand
#         self.model = model      # Car's model
#         self.year = year        # Car's manufacturing year
#         self.color = color      # Car's color
#         self.tyre = tyre        #size of tyre
#     def description(self):
#         return f"{self.year} {self.color} {self.brand} {self.model} {self.tyre}"

#     def drive(self):
#         return f"The {self.brand} {self.model} is now driving..."

# # Creating objects with more info
# car1 = Car("Toyota", "Corolla", 2020, "White", "22inches")
# car2 = Car("Honda", "Civic", 2022, "Black", "22inches")

# # Printing descriptions
# print(car1.description())
# print(car2.description())

# # Calling the drive method
# print(car1.drive())
# print(car2.drive())


# #new class

# class student:
#    def __init__(self,name,age,grades):
#       self.name = name
#       self.age = age
#       self.grades = grades
#    def details(self) :
#          return f"Student Name: {self.name}\nAge: {self.age}\nGrades: {self.grades}"
      
# # creating objects info
# stu_1 = student("Tayyab","21","E")
# stu_2 = student("Kaleem","18","B+")

# # printing students data

# print(stu_1.details())
# print(stu_2.details())




class Letter:
    def hello(self):
        print("hello world")

x = Letter()
x.hello()



