xy=[1,2,3]
xy.insert(0,0)
print(xy)



# list_1 = [1,2,3,4,5,6,7]
# del list_1
# print(list_1)


for i in range(5):
    print(i)



print("Loop finished!")



for i in range(5):
    print(i)
else:
    print("Loop finished!")


is_bool=True
if is_bool:
    print("boolean is true ")
elif is_bool==False:
    print("boolean is false")
else:
    print("invalid")


age=4
if age>=18:
    print("you are eligible for a license")
elif age>=2:
    print("not eligible")
else:
    print("invalid")










#chat gpt's code 


# Create an empty list
my_list = []

# Adding elements manually from user
a = input("Enter first element: ")
b = input("Enter second element: ")
c = input("Enter third element: ")

my_list.append(a)
my_list.append(b)
my_list.append(c)

print("Original List: ", my_list)

# Accessing element at index 1
print("Element at index 1:", my_list[1])

# Updating element at index 1
new_value = input("Enter new value to replace element at index 1: ")
my_list[1] = new_value
print("List after updating:", my_list)

# Removing element
remove_item = input("Enter value to remove from the list: ")
if remove_item in my_list:
    my_list.remove(remove_item)
    print("List after deletion:", my_list)
else:
    print("Item not found in the list!")
