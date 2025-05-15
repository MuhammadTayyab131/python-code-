# string_1 = input("Enter first word:\t")
# string_2 = input("Enter second word:\t")
# a = string_1.split
# b = sorted(a)
# print(b)
# c = string_2.split
# d = sorted(c)
# print(c)

# if a == d :
#     print("both words are anagrams")


s1=input("enter a string:\t").lower().strip()
s2=input("enter another string:\t").lower().strip()


if sorted(s1)==sorted(s2):
    print("both are anagram")
    if s1[::-1]==s2:
        print("both are anagram and also palindrome")
else:
    print("both are not anagram")



s = {"apple", "banana", "cheeeeerry", True, 1, 2}

print(s)


my_list = (1,2,3,4,5,6)
my_set = {1,2,3,4,5,6}
new_list=list(my_set)
print(type(new_list))


thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(type(thisdict))
print(thisdict)
