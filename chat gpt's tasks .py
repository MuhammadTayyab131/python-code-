# task 1

a = "hello world"
print("Lenght of string is: ",len(a))

# task 2

name = "Mian Tayyab"
b = name.lower()
print("In Lowercase : ", b)
c = name.upper()
print("In Uppercase",c)

# task 3

d = "                      HELLO                        "
e = d.strip()
print("original string : ",d)
print("after removing spaces : ",e)

# task 4

rep_str = "He is bad boy."
print("original string:                     ",rep_str)
after_change = rep_str.replace("bad","good")
print("string after changing:               ",after_change)


# tsak 5

string = "I am learning Python"
split_string = string.split(" ")
print(split_string)

# tsak 6

a = "I"
b = "am"
c = "Muhammad"
d = "Tayyab"

sab_ko_mila_kar = "-".join([a,b,c,d])

print(sab_ko_mila_kar)

# task 7

g = "hello world"
print(g.find("world"))


# task 8

my_string = "Hello, Are you fine? Bye"
str_from = my_string.startswith("Hello")
end_at = my_string.endswith("bye")

print("starts with Hello : ",str_from)
print("ends at bye : ",end_at)

# task 9

fruit = "banana"
x = fruit.count("a")
print(x)

# task 10

test = " is this statement contains only alphabets"
print(test.isalpha)
test_1 = 123456789
print(test_1)




#  task of for loop from chat gpt

for _ in iter(int, 1) :
    num = int(input("Enter any number: \t"))

    if num < 0 :
        print("loop stopped! wrong input")
        break 
    if num % 2 == 0 :
        print("Please enter odd numbers")
        continue
    if num==-1:
        break
    

    print(num)














my_tuple = ("hello","hello",12,10.0,True)
print(my_tuple)
my_tuple = ("hello")

thistuple = ("Hamko", "to gardish e ", "aiyaam pe","roona aya","\nRoony waly","tujhay kis","baat py","roona aya")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i +1


tuple_1 = (1,2,3,4,5)
tuple_2 = (6,7,8,9,10)
tuple_3 = tuple_1 * 3
print (tuple_3)


string_1 = input("Enter first word:\t")
string_2 = input("Enter second word:\t")
a = string_1.split
b = sorted(a)
print(b)
c = string_2.split
d = sorted(c)
print(c)

# if a == d :
#     print("both words are anagrams")


