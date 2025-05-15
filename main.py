print("hellow world")
print("Hello, Tayyab! Welcome to Python in VS Code.")
fruits = ["apple","banana","mango"]

x,y,z = fruits
print(x)
print(y)
print(z)
x = "I "
y = "am "
z = "tayyab"
print(x+y+z)
print('hello','world')
message = "hello how are you?"
print(message.upper())

a=3
b=3.4
c="abc"


print(type(a))
print(type(b))
s = '''hello
world
hello'''
print(s)
print(message [0:5])


# checking Indentation
if 2 < 5:

  print ("2 is less then 5")
print('hello' , 'world')



# global variable 
x = "amazing"
def my_function():
 global x
x = "fantastic"
  
my_function ()
print("this world is "+ x)



#  list functions 
my_list = [10,20,30,40,'fifty']
print(my_list)
print(my_list[0])
my_list[1]=15
print(my_list)
my_list.append(100)
print(my_list)

# tuple same hi hai bas us main modification nai hoti

# range 
r = range(10, 20, 30)
print(list (r))

#creating dictionary 
student = {
  "Name" : "Muhammad Tayyab",
  "Age"  : 20,
  "City" : "Lahore"
}

print(student["Age"])

for i in range (1,11,3):
  print(i)

# Convert from one type to another:
# x = 1
# y = 2.98
# z = 2+j3

# print()



my_tuple = (10,20,30)
my_list = [10,2.89,"ello",True]
print(my_list)
t = '''i am tayyab
i live in lahore
'''
print(t)


# sting ko index main kesay dekhty hain





name = "Muhammad tayyab" 
age = 20
city = "Lahore"

print(f"My Name is {name}, I am {age} year old, I live in {city}")

print("My Name is %s, I am %d year old, I live in %s" %(name,age,city))

print("My Name is {}, I am {} year old, I live in {}".format(name,age,city))

my_name = "tayyab"
MyName = "tayyab"
MY_NAME = "TAYYAB"

print(my_name)
print(MyName)
print(MY_NAME)


a = 10
b = 20

a , b = b , a 

print("now a = {}".format(a))
print("now b = {}".format(b))

h = "How are you"
g = "I am fine"
j = h +" , "+ g
print(j)

v = 50
def price_function():
 
 global v
 v = v+49

price_function()

print("price of this product is: ${}".format(v))


a = 12
b = 12.98
c = 12 + 4j

x = float(a)
y = int(b)
z = complex(c)

print(x)
print(y)
print(z)

a=10
b=20

# a,b=b,a
a=a+b 
b=a-b 
a=a-b

print("now a is :{}".format(a))
print("now b is :{}".format(b))


my_string="mian tayyab"
print(my_string[1::3])
print(len(my_string))
print(my_string.strip())
print(my_string.replace("t", "T"))
b=my_string.split ()
print(b)
s = my_string.center(40,"_")
print(s)

print(f"My Name is  {name},\f I am {age:.2f} year old,\f  I live in {city}")

print(f"My Name is  {name}, I am {age:.2f} year old,  I live in {city}")

a = "hello 123 how are you are you fine where you are from  Hi hello 987"

x = a.count("o")
v = a.encode()
print(x)
print(v)
p = a.endswith(("987"))   # agar startswith likhien to strat wala btaye ga 
print(p)

list_ky_lafaz  = ["hello","world","!"]
print(" ".join(list_ky_lafaz))

count = "123456789"
print(count.find("5"))
print(count.index("6"))

d = "kya is main sirf alphabet hi hain"
print(d.isalpha)

My_list = ["blue", "green", "black","white"]
print(len(My_list))

# list_1 = ["abc",123,True,"move"]
# print(list_1)
# print(type(list_1))

# L_list = list(("red","green","yellow"))
# print(L_list)
# print(L_list(1))




my_string="my name is tayyab"
if "tayyab" in my_string:
  print("tayyab is present")





# my_name= input("enter a name >>")
# age =int(input("enter a age >>"))
# print(f"your age is :{age}")


origional_string="zulqarnain"

repl_str = origional_string.replace("zulqarnain","tayyab")
print(repl_str)


# a=input,b=input,c=input  teen input leny hain aur in main sy greater btana hai y using if else 

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))

if a > b and a > c :
  greatest_no = a

elif b > a and b > c :
  greatest_no = b

elif c>a and c>b:
  greatest_no=c

  


print("The greatest no is ",greatest_no)

changed_string=my_string[-1]
print(changed_string)

num_1 = 2
num_2 = 3
#temp_1= a+=b
num_1=+num_2
print(a)



my_string_origional=input("enter a string value")

print(type(my_string_origional))


string = "Hello, World!"
reversed_string = string[::-1]
print(reversed_string)


my_list_2 = ["hello","world","ok","fine"]
print(len(my_list_2))

list_1 = ["hello","how"]
list_2 = [1,2,3,4,5]
list_3 = [True,False,True]

print(type(list_3))


p = list(("hello","hello","hello"))

print(p)

# s = "abcd"
# a, b , c, d

for char in "Hello":
    print(char)


my_string = "abcdef"

# for index, char in enumerate(my_string):
#     print(f"Character '{char}' is at index {index}")

result = string(enumerate(my_string))


num = 2

