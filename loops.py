
# for x in range(1,11):
#   print(f"2 X {x} = {x*2}")



# i = 1
# while i < 11:
#   print(f"2 X {i} = {i*2}")
#   i += 1


attempts = 0
max_attempts = 3

while True:
    password = input("Enter password: ")
    attempts += 1

    if password == "mian0909":
        print("Access Granted!")
        break
    elif attempts >= max_attempts:
        print("Access Denied!")
        break
    else:
        print(f"Wrong password! You have {max_attempts - attempts} tries left.")



# age = int(input("enter your age: "))
# while age>0 and age<=120:
#    print("valid age ")
#    break

# else :
#    print("invalid age")


# total_sum = 0


# for num in range(1, 101):
#     if num % 2 == 0:
#         total_sum += num
# print("Sum of all even numbers: ", total_sum)



# n = int(input("How many elements do you want in tuple :   "))
# my_tuple = []
# for i in range(n):
#     elements = int(input(f"Enter your {i+1} elements :  "))
#     my_tuple.append(elements)
# my_tuple = tuple(my_tuple)
# print("The tuple is : ",my_tuple)
# max_value = my_tuple[0]
# for value in my_tuple:
#     if value > max_value:
#         max_value = value
# print("The maximum value in the tuple is:", max_value)



# my_tuple = (10, 20, 4, 45, 99)

tuples=(1,2,3,4,5,2,8,4)
max_number=tuples[0] #to check or compare with the first index
min_number=tuples[0]
for num in tuples:
   if num>max_number:
      max_number=num
   elif num<min_number:
      min_value=num
print(min_number)
print(max_number)


info = {
    "name": "Tayyab",
    "age": 21,
    "city": "Lahore"
}

ask = input("What do you want to know? (name / age / city): ").lower()

if ask in info:
    print(f"{ask.capitalize()}: {info[ask]}")
else:
    print("Sorry, this information is not available.")



class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Sound of some animals")

    def show_info(self):
        print(f"Name: {self.name}")

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)  # alternate to super()

    def sound(self):
        print(f"{self.name} sounds like \"woof\"")

class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)  # alternate to super()

    def sound(self):
        print(f"{self.name} sounds like \"meow\"")

# Creating objects
dog = Dog("oskar")
cat = Cat("bella")

# Output
dog.show_info()
dog.sound()

cat.show_info()
cat.sound()
