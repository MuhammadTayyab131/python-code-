my_list = ['mango', 'kiwi', 'orange', 'cherry', 'banana', 'apple']
my_list[1:4:2] = ["hello","world"]
print(my_list)

my_list.append("grapes")
print(my_list)

orig_list = []
for x in range(1,21):
    orig_list.append(x)
    
print(f"your origional list is: \f {orig_list} ")

even_list = []
for i in orig_list:
    if i%2==0 :
        even_list.append(i)

print(f"even numbers of your list: \f {even_list}")



thislist = ["OraNge","BanAna", "KIWi"]
thislist.sort(key=str.lower)
print(thislist)

fruits = ['apple', 'banana', 'cherry']
fruits[1:1] = ["orange", "grape", "mango"]
print(fruits)

for index, value in enumerate(fruits):
    print(f"Index: {index+1}, Value: {value}")

# sort reverse append extend pop remove  

# sort 1

cric_kit = ["Bat","Ball","Batting Gloves","Wicket-Keeping Gloves","Leg Guards Pads"]


cric_kit.sort()

print(cric_kit)

# reverse 2

cric_kit.reverse()

print(cric_kit)

# append 3

cric_kit.append("Abdominal Guard Box")

print(cric_kit)

# extend 4
cric_kit_2 = ["Helmet","Elbow Guard","Chest Guard","Cricket Shoes","Thigh Guard"]
cric_kit.extend(cric_kit_2)

print(cric_kit)

# pop 5 

cric_kit.pop(3)

print(cric_kit)

# remove 6

cric_kit.remove("Wicket-Keeping Gloves")

print(cric_kit)

# list hai usky andar 3 string hain teeno small mai inko upper case main karna hia
# aik string likh kar uskay vowals btanay hain

# even numbers 1

orig_list = [1,2,3,4,5,6,7,8,9,10]

print(f"your origional list is: \f {orig_list} ")

even_list = []
for i in orig_list:
    if i%2==0 :
        even_list.append(i)

print(f"even numbers of your list: \f {even_list}")

# squares of list elements 2

orig_list_2 = [1,2,3,4,5,6,7,8,9,10]

print(f"your origional list is: \f {orig_list} ")

squ_of_list = []
for i in orig_list_2:
        
     squ_of_list.append(i**2)

print(f"even numbers of your list: \f {squ_of_list}")




# my_string_for_loop="zulqarnain"

# for value in  my_string_for_loop:
    

















xy=[1,2,3]
new_list_1=xy.insert(0,0)
print(new_list_1)