


def number_checker(num):
    if num <= 0 :
       print("Invalid entery! Enter number greater than zero")
    elif num % 2 == 0 :
      print(f"Your given number {num} is even")
    elif num % 2 == 1 :
      print(f"Your given number {num} is odd")
    else :
      print("Ivalid Data ")  

def squ (i):
   return i*i
       

a = lambda i : i*i*i




num = int(input("Enter any number: "))

number_checker(num)

print(f"Square of {num} is : ",squ(num))

print(f"Cube of {num} is: ",a(num))


# #first function call

# a = int(input("Enter any number greater than Zero:  "))
# number_checker(a)


# #second function call
# num_1 = int(input("Enter any number whome you want square: "))
# result = squ(num_1)
# print(f"Square of {num_1} is : ",result)


# # third function call


# o = int(input("enter a number for lambda funtion cube: "))
# print(f"lambda funtion cube of {o} is: ",a(o))



# sum ka function har function ky sath
#lambda ky sath even odd


check_even_odd_1 = lambda number: "Even" if number % 2 == 0 else "Odd"

print(check_even_odd_1 (7))  # You can change the number


def check_even_odd_2 (number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Call the function and print the result
result = check_even_odd_2 (6)  # You can change the number
print(result)

a,b,c,x = 3,4,5,6

quad = a*x^2 + b*x +c

print(type(quad))
