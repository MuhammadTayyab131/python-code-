txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))

t = "hello i am tayyab"
b = t.title()
print(b)

txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(x)

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)
print(len(txt))




my_string = "abcdef"


for index, char in enumerate(my_string):
        print(f"Character '{char}' is at index {index}")




# my_string = "abcdef"

# my_dict = {char: index for index, char in enumerate(my_string)}
# print(my_dict)

# print(type(my_dict))



my1_string = "abcdef"
my_dict = {}

for index, char in enumerate(my1_string):
    my_dict[char] = index

print(my_dict)


string_1 = "apple banana apple orange"

# output => ["apple", "banana", "mango", "orange"]

# next 
# covert into dict

# {"apple": 0,....}

# dict ku tuple mai 

list_1 = string_1.split()
print(list_1)

dict_1 = {}
for i,x in enumerate(list_1):
      dict_1[x] = i+1

print(dict_1)

key_tuple = tuple(dict_1.keys())
value_tuple = tuple(dict_1.values())
print("keys",key_tuple)
print("values",value_tuple)


# if "apple" in dict_1:
#     print("Key 'apple' exists in the dictionary")
# else:
#     print("Key 'apple' does not exist.")


# if dict_1.get("apple"):
#      print("Key 'apple' exists in the dictionary")
# else:
#      print("Key 'apple' does not exist.")

# print('apple' in dict_1)