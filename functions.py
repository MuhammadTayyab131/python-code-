# i = 0
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1


# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)
# print("--------------------------------------------------")

# b = int (input("jahan tak apko even numbers chahiye wo number daliye: "))
# for x in range(0, b, 2):
#   print(x)



# b = "Hello, World!"
# print(b[2:3]+b[6:8])
# a = "hello world"


# a = "hi world"
# reversed_a = a[::-1]

# print("Reversed string:", reversed_a)

# for x in range(1,11):
#   print(f"2 X {x} = {x*2}")



# i = 1
# while i < 11:
#   print(f"2 X {i} = {i*2}")
#   i += 1


def number_checker(num):
    if num <= 0 :
       print("Invalid entery! Enter number greater than zero")
    elif num % 2 == 0 :
      print(f"Your given number {num} is even")
    elif num % 2 == 1 :
      print(f"Your given number {num} is odd")
    else :
      print("Ivalid Data ")  


a = int(input("Enter any number greater than Zero:  "))
number_checker(a)


def squ (i):
   return i*i
 

num_1 = int(input("Enter any number whome you want square: "))
result = squ(num_1)
print(f"Square of {num_1} is : ",result)

      
def cube (x):
   return x*x*x

num_2 = int(input("enter any nuber whome you want qube: "))
result = cube(num_2)
print(f"qube of {num_2} is: ",result)

a = lambda i : i*i*i

# print("cube with lambda funtion",a(4))
o = int(input("enter a number for lambda funtion cube: "))
print(f"lambda funtion cube of {o} is: ",a(o))


