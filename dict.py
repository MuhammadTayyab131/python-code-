cricketer  = {
"Team": "Pakistan",
"Role": "Medium Fast Bowler",
"Name": "Muhammad Tayyab",
"Age" : 22 
}

x = cricketer.keys()

print(x) 

cricketer["BBF"] = "4-16"

print(x) 

for keys, values in cricketer.items():
    print(f"{keys}:{values}")

# print(cricketer)    
# print(type(cricketer))


v = cricketer.items
cricketer.update({"Age":21})
print(cricketer["Age"])






cricket_team = {
    "player_1": {
        "name": "Babar Azam",
        "age": 29,
        "role": "Batsman",
        "matches": 85,
        "Highest score": "158(139)"
    },
    "player_2": {
        "name": "Shaheen Afridi",
        "age": 23,
        "role": "Bowler",
        "matches": 50,
        "best_figures": "6-35"
    },
    "player_3": {
        "name": "Muhammad Tayyab",
        "age": 21,
        "role": "Medium-fast Bowler",
        "matches": 2,
        "best_figures": "4-45"
    }
}

# for keys, values in cricket_team.items():
#     print(f"{keys}:{values}")


# print(cricket_team["player_3"]["best_figures"])


# for keys , values in cricket_team.items():
#     print(x)
    
#     for y in values:
#         print(y + ':', values[y])


for x in cricket_team.values():
    for i in x.values():
        print(i)


marks = {
    "Ali": 85,
    "Zulqurnaian": 92,
    "Tayyab": 78
}

name = input("Enter the student's name : ")
print(marks.get(name, f"No record found for student named {name}."))


sentence = input("Enter a sentence: ")

# Convert the sentence to lowercase and split into words
words = sentence.lower().split()

# Create an empty dictionary to store word counts
word_count = {}

# Count how many times each word appears
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word counts
print("\nWord Frequency:")
for word, count in word_count.items():
    print(f"{word}: {count}")



