# a = input("Enter your first string : \n").lower().strip()
# b = input("enter your second string : \n").lower().strip()


# a , b = b , a 

# print(f"updated a is {a}")
# print(f"updated b is {b}")

# if a == b[::-1] :
#     print("a and b are palindrome")
#     if sorted(a) == sorted(b) :
#       print("a and b are also a anagram") 

# else:
#     print("Neither a nor b is a palindrome or an anagram......")


# a=5
# b=4
# a=a+b
# b=a-b
# a=a-b
# print(a,b)


# list ky duplicate khatam karnay hain

# lists=[1,1,2,3,2,2,2,2,3,4]
# unique=[]
# for item in lists:
#         if item in unique:
#             unique.append(item)
#         else:
#             if unique==item:
#                 unique.remove()
    
# print(unique)

# items = [1, 2, 2, 3, 4, 4, 5]
# unique = []

# for item in items:
#     is_duplicate = False
    
#     for u in unique:
#         if u == item:
#             is_duplicate = True
#             break
    
#     if not is_duplicate:
#         unique.append(item)

# print("Unique items:", unique)



# a = int(input("Enter any number: "))
# if a % 2 == 0 :
#     print("This is an even number.")
# else :
#     print("This is an odd number")
# if a == 100 :
#     print("This number is equal to 100")
# elif a < 100 :
#     print("This number is less than 100")
# else :
#     print("This number is greater than 100")
# if a > 0:
#     print("It's a positive number.")
# elif a < 0:
#     print("It's a negative number.")
# else:
#     print("It's zero.")



x = int(input("How many items are your favorites?   "))
fav_items = []
for i in range (x):
    items = input(f"Enter your {i+1} item: ")
    fav_items.append(items)
fav_items=tuple(fav_items)
# print("yor fav items are: ",fav_items)
print("Your fav items are:")

for c in fav_items :
    print("- ",c)



# s = [1,2,3,[4,5], [6],[7]]
# new_list=[]


# for lists in s:
#     new_list.append(lists)
# print(new_list)



